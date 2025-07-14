import streamlit as st
from scripts.strategy_rules import recommend_strategy
from scripts.simulate_what_if import simulate_strategy


# Title
st.title("📈 Options Strategy Recommender")

# Subheader
st.subheader("Select a stock and input parameters")

# User inputs
stock_symbol = st.text_input("Enter stock ticker symbol (e.g., AAPL)", value="AAPL")
price = st.number_input("Current stock price", min_value=0.0, value=150.0)
volatility = st.slider("Implied volatility (%)", 0.0, 100.0, 25.0)

# Placeholder output
if stock_symbol and price > 0:
    strategy = recommend_strategy(price, volatility)

    st.markdown(f"📈 **Recommended Strategy:** `{strategy}`")
else:
    st.markdown("🔍 Strategy suggestion will appear here…")

st.subheader("📊 What-if Scenario Simulation")
price_change = st.slider("Change in stock price ($)", -50.0, 50.0, 0.0, step=0.1)
vol_change = st.slider("Change in implied volatility (%)", -50.0, 50.0, 0.0, step=0.1)

if stock_symbol and price > 0 and (price_change != 0.0 or vol_change != 0.0):
    simulated_strategy = simulate_strategy(price, volatility, price_change, vol_change)
    st.markdown(f"🔮 **Simulated Strategy (What-If):** `{simulated_strategy}`")
