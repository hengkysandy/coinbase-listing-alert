#*/10 * * * * /bin/python3.7 /path/to/main.py
import time
import requests
import telebot
import pymongo
from pymongo import MongoClient 

cluster = MongoClient('mongodb+srv://<USERNAME>:<PASSWORD>@<MONGODB_HOST>/<MONGODB_DB>?retryWrites=true&w=majority')
db = cluster['<MONGODB_DB>']
collection = db['<MONGODB_COLLECTION>']

message_id = '<YOUR_TELEGRAM_CHANNEL_ID>'

API_KEY = '<TELEGRAM_API_KEY>'
bot = telebot.TeleBot(API_KEY)

def get_listed_asset_coinbase():
    result = ''
    coins = []
    assets = requests.get('https://api.pro.coinbase.com/currencies').json()
    for asset in assets:
        coins.append(asset['id'])
    return coins

def main():
    mongo_coinbase_key = "coinbase_assets"
    current_coinbase_assets = collection.find_one({"_id": mongo_coinbase_key}).get('value').split('|')
    new_coins = get_listed_asset_coinbase()
    if len(current_coinbase_assets) != len(new_coins):
        msg = '`New Listing on #Coinbase!\n'
        for coin in new_coins:
            if coin not in current_coinbase_assets:
                msg += coin + '\n'
        msg += '`'
        
        joined_coins = '|'.join(new_coins)
        collection.update_one({"_id": mongo_coinbase_key}, {"$set" : {"value" : joined_coins}})
        
        bot.send_message(message_id, msg, parse_mode='Markdown')
                
        
main()