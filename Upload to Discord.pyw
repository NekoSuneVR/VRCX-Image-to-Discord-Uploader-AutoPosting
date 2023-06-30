import os
import json
import requests
from PIL import Image
import threading
import time
from dotenv import load_dotenv
import getpass

# Load environment variables from .env file
load_dotenv(".env")

# Replace YOUR_TOKEN_HERE with your actual Discord bot token
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Get the current user's username
username = getpass.getuser()

# Specify the directory to monitor
directory_to_monitor = f"C:/Users/{username}/Pictures/VRChat"

def extract_image_metadata(file_path):
    with Image.open(file_path) as img:
        description = img.info.get('Description')

        #if not description:
        #    raise ValueError("The selected image has no metadata.")

        metadata = json.loads(description)
        world_name = metadata['world']['name']
        world_id = metadata['world']['id']
        players = metadata['players']
        player_names = [player['displayName'] for player in players]

        return world_name, world_id, player_names

def create_payload(file_path):
    timestamp = os.stat(file_path).st_ctime
    world_name, world_id, player_names = extract_image_metadata(file_path)

    payload = {
        "content": f"Photo taken at **{world_name}** *({world_id})* with **{', '.join(player_names)}** at <t:{int(timestamp)}:f>"
    }

    return payload

def upload_image_to_discord(file_path):
    try:
        # Get webhook URL from environment variable
        webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

        # Check if webhook URL is available
        if not webhook_url:
            raise ValueError("Discord webhook URL is not set in .env file.")


        # Create payload
        payload = create_payload(file_path)

        # Read file before sending payload
        with open(file_path, 'rb') as f:
            image_data = f.read()

        # Send payload to webhook with image attached
        files = {'file': (os.path.basename(file_path), image_data)}
        response = requests.post(webhook_url, data=payload, files=files, stream=True)

        if response.ok:
            print("Image uploaded successfully")
        else:
            print("Failed to upload image:", response.text)

    except Exception as e:
        print("Error:", str(e))

def check_for_new_files(directory):
    # Get the current files in the directory
    current_files = set()

    while True:
        # Traverse all subdirectories within the directory
        for root, dirs, files in os.walk(directory):
            # Update the current files with the files in the subdirectory
            current_files.update(files)

        # Wait for a specified interval
        time.sleep(1)

        # Traverse all subdirectories within the directory again
        for root, dirs, files in os.walk(directory):
            # Get the updated files in the subdirectory
            updated_files = set(files)

            # Find the newly created files
            new_files = updated_files - current_files

            # Process the new files
            for file in new_files:
                file_path = os.path.join(root, file)
                upload_image_to_discord(file_path)

            # Update the current files with the updated files
            current_files.update(updated_files)

# Start checking for new files in the directory
check_for_new_files(directory_to_monitor)
