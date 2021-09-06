# Binance Announcements Scraper

## About The Project
This tool analyses the changes in Binance announcements page and sends an alert to Telegram.
Can easily be modified to signal your trading bots or any other kind of system.


## Getting Started

### Dependencies

1. Install Python3 Dependencies
    ```sh
    pip install -r requirements.txt
    ```

    > **_NOTE:_**  Prefered Method to avoid dependencies clash would be using venv or Docker container.
2. Create Telegram Bot for sending notifications
	1. 	Start a chat with the [Telegram BotFather](https://telegram.me/BotFather)
	2. 	Send the message `/newbot` and follow the instructions from Telegram BotFather
	3. 	Copy the API Token (22222222:APITOKEN from example below) and keep it safe to later use in the config parameter `bot_token`
		```
        Done! Congratulations on your new bot. You will find it at t.me/yourbots_name_bot. You can now
        add a description, about section and profile picture for your bot, see /help for a list of
        commands. By the way, when you've finished creating your cool bot, ping our Bot Support if 
        you want a better username for it. Just make sure the bot is fully operational before you 
        do this.
        
        Use this token to access the HTTP API: 22222222:APITOKEN
        
        For a description of the Bot API, see this page: https://core.telegram.org/bots/api Father 
        bot will return you the token (API key)
        ```
	4. 	Start a conversation with your bot by click `/START`button
2. Get your Telegram user id
	1. 	Start a chat with the [Telegram User Info Bot](https://telegram.me/userinfobot)
	2. 	Get your "Id" from bot reply, you will use it for the config parameter `user_id`.

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/lkology/binance-announcements-scraper.git
   ```
2. Copy default config file
   ```sh
   
   # linux: Copy file over.
   cp config.default.json config.user.json
   
   # windows: either copy the file in explorer and rename to 'config.user.json' or use
   copy config.default.json config.user.json
   ```
3. Override default values for Telegram parameters in `config.user.json`
   
### Usage
The tool can be run periodically with a cron jon or scheduled task on windows.
   ```sh
   root@bcd2d15321a9:/app# python3 main.py
    Starting...
    Catalog 'New Cryptocurrency Listing':
    Catalog 'Latest Binance News': Found 1 new article(s)
        Found new article Introducing Binance Recurring Buy
    Catalog 'Latest Activities': No new articles found.
    Catalog 'New Fiat Listings': No new articles found.
    Catalog 'API Updates': No new articles found.
    Catalog 'Crypto Airdrop': No new articles found.
   ```

### License 
Distributed under the MIT License. See `LICENSE` for more information.