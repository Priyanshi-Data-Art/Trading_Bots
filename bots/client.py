from dotenv import load_dotenv
from binance.client import Client
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def client_connection():
    client=Client(API_KEY,API_SECRET,testnet=True)
    return client