
# Coinbase Listing Alert

This tool helps you to get notified when everytime new coin / token listed on Coinbase, it gaves significant impact on the price.

## How to Use

1. Clone the repository.
2. Install the dependencies: `pip3 install -r requirements.txt`
3. Create your own telegram channel and Telegram API Key
5. Create your own mongodb atlas account and create collection name with format
```
{"_id":"coinbase_assets","value":"BTC|ETH|DOT"}
```
4. Run the project in cronjob that will run every 10 minutes, by using the following command: 
```
#*/10 * * * * /bin/python3.7 main.py
```
