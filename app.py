import streamlit as st
import yfinance as yf

# --- Strategy Recommendation Logic ---
def recommend_strategy(price, volatility):
    if price < 50 and volatility < 20:
        return "Buy Call"
    elif price < 50 and volatility >= 20:
        return "Bull Call Spread"
    elif price >= 50 and volatility < 20:
        return "Covered Call"
    else:
        return "Iron Condor"

# --- What-if Simulation Logic ---
def simulate_strategy(price, volatility, price_change, vol_change):
    new_price = price + price_change
    new_volatility = volatility + vol_change
    return recommend_strategy(new_price, new_volatility)

# --- Fetch Price and IV from yfinance ---
def get_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1d")
        price = round(hist["Close"].iloc[-1], 2) if not hist.empty else None

        # Estimate volatility from option chain (crude approximation)
        options = stock.options
        if options:
            opt_chain = stock.option_chain(options[0])
            iv_calls = opt_chain.calls['impliedVolatility'].mean()
            iv = round(iv_calls * 100, 2) if not opt_chain.calls.empty else 25.0
        else:
            iv = 25.0  # fallback

        return price, iv
    except Exception:
        return None, None

# --- Streamlit App UI ---
st.title("📈 Options Strategy Recommender")
st.subheader("Select a stock and input parameters")

# Input stock ticker
stock_symbol = st.text_input("Enter stock ticker symbol (e.g., AAPL)", value="AAPL", key="ticker_input")

# Fetch price & IV from data
if stock_symbol:
    fetched_price, fetched_iv = get_stock_data(stock_symbol)
else:
    fetched_price, fetched_iv = None, None

# Display stock inputs
if fetched_price:
    price = st.number_input("Current stock price", value=fetched_price, key="price_fetched")
    volatility = st.slider("Implied volatility (%)", 0.0, 100.0, value=fetched_iv, key="vol_fetched")
else:
    price = st.number_input("Current stock price", value=0.0, key="price_default")
    volatility = st.slider("Implied volatility (%)", 0.0, 100.0, 25.0, key="vol_default")

# Recommended strategy
if stock_symbol and price > 0:
    strategy = recommend_strategy(price, volatility)
    st.markdown(f"📈 **Recommended Strategy:** `{strategy}`")
else:
    st.markdown("🔍 Strategy suggestion will appear here…")

# What-if simulation
st.subheader("📊 What-if Scenario Simulation")
price_change = st.slider("Change in stock price ($)", -50.0, 50.0, 0.0, step=0.1, key="whatif_price")
vol_change = st.slider("Change in implied volatility (%)", -50.0, 50.0, 0.0, step=0.1, key="whatif_vol")

if stock_symbol and price > 0 and (price_change != 0.0 or vol_change != 0.0):
    simulated_strategy = simulate_strategy(price, volatility, price_change, vol_change)
    st.markdown(f"🔮 **Simulated Strategy (What-If):** `{simulated_strategy}`")

