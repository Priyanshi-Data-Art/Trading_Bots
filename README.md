# Trading_Bot 
This is a small python project where I connected to Binance Futures Testnet using API keys and placed orders from python code. 
Main purpose of this project was to understand how real trading APIs work. 

## What it can do? 
Connect to Binance Futures Testnet 
Place MARKET order 
Place LIMIT order (GTC) 
Basic input validation (BUY/SELL, quantity, price) 
Logs all responses and errors in a log file 

## Tech Stack:- 
Python 
python_binance library 
python_dotenv 
logging 

## Setup Steps
1. First, download or clone the project from GitHub:
   git clone https://github.com/YourUsername/Trading_Bot_Assessment.git
    cd Trading_Bot_Assessment
2. Make a Python virtual environment (this keeps project packages separate):
  python -m venv venv
  - Activate it:
  - **Windows:** venv\Scripts\activate
  - **Mac/Linux:** source venv/bin/activate

3. Install all the required Python packages:
   pip install -r requirements.txt

4. Create a file called .env in the main project folder and add Binance testnet keys:
5. Now you are ready to run the project!

## How to Run Examples
1. Activate your virtual environment.  
2. Run the CLI file:
   python cli.py
3. Follow the instructions in terminal:  
   - Symbol (e.g., BTCUSDT)  
   - Order type (MARKET/LIMIT)  
   - Side (BUY/SELL)  
   - Quantity  
   - Price (for LIMIT only)  
4. Order details will print and also save in trading_bot.log.

## Assumptions
Testnet only (no real money)
Only MARKET & LIMIT orders supported
API keys stored in .env (not shared)

## Logs:- All order response stored in trading_bot.log file to debug the error 
