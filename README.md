

# **VRChat Screenshot Uploader**

This is a simple Python script that allows you to upload VRChat screenshots to a Discord channel using a webhook. The images have to be modified by [VRCX](https://github.com/pypy-vrc/VRCX) before being uploaded, as this adds metadata that is used to display information about the world and players in the Discord message.

## Usage

1. Install the required libraries using the '**install_dependencies.py**' script: `python install_dependencies.py`
2. Modify DISCORD_WEBHOOK_URL in the **.env** file with your actual Discord webhook URL (optional).
3. Start the application by double-clicking the **Upload to Discord.pyw** file.

then take pictures Realtime then will upload to Discord Server using Webhooks.

## Note

-   The VRChat image must be modified by [VRCX](https://github.com/pypy-vrc/VRCX) to contain the necessary metadata.
-   Make sure put Discord Webhook URL in .env file or wont Run/Send
## Requirements

-   Python 3.6 or later
-   `requests` library
-   `pillow` library
-   `python-dotenv` library

These can be installed using the `install_dependencies.py` script.

**License**

This script is licensed under the MIT license. See the [LICENSE](https://github.com/Fynn9563/VRCX-Image-to-Discord-Uploader/blob/main/LICENSE) file for more information.

**MESSAGE:** want say thank you to Fynn9563 told me about this and i modify his code as i had permission do it make it so auto uploads realtime everytime take pictures.

**WITH LITTLE HELP OF CHAT GPT** other that working just normal.
