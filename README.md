# IP_change_notifier
A simple discord bot which notifies you if the server the bot is hosted on 
changes IP address and sends you the new one.  This can be useful if you are
using a home server which has a dynamic IP.


## Hosting the bot

[Article on creating a bot token](https://www.writebots.com/discord-bot-token/)

Once you have your token, download the JomBot repo and unzip it. Create a file
called just `.env` with the layout

```
# .env
DISCORD_TOKEN=INSERT YOUR DISCORD TOKEN HERE
```

and put the file in the same directory as the bot.py file.

Now you have to download all the libraries required. To do that run the command

```python
pip install -r requirements.txt
```

To run the bot you'll want to simply run `python3 bot.py` and it should be
working. Note that the bot will only be running for as long as your terminal is
open, so I'd recommend using tmux to create terminal instances so it will be
running as long as your server is on. 

Then you want to send the command `!send_ip` in the channel you want the IP
address to be sent to when it updates.  This will start the bot checking for
any changes to the IP address.  Make sure you send the command in the same
server the bot is running in.  You can run the `send_ip` command at any time
to get the current IP address.
