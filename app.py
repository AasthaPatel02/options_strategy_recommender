import streamlit as st


from scripts.strategy_rules import recommend_strategy
from scripts.simulate_what_if import simulate_strategy
from scripts.fetch_stock_data import get_stock_data

# Title
st.title("📈 Options Strategy Recommender")

# Subheader
st.subheader("Select a stock and input parameters")

# User input for ticker
stock_symbol = st.text_input("Enter stock ticker symbol (e.g., AAPL)", value="AAPL", key="ticker_input")

# Fetch price/IV based on ticker
if stock_symbol:
    fetched_price, fetched_iv = get_stock_data(stock_symbol)
else:
    fetched_price, fetched_iv = None, None

# Display price and volatility (fetched or manual fallback)
if fetched_price:
    price = st.number_input("Current stock price", value=fetched_price, key="price_fetched")
    volatility = st.slider("Implied volatility (%)", 0.0, 100.0, value=fetched_iv, key="vol_fetched")
else:
    price = st.number_input("Current stock price", value=0.0, key="price_default")
    volatility = st.slider("Implied volatility (%)", 0.0, 100.0, 25.0, key="vol_default")

# Show strategy
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
