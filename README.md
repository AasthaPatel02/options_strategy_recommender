#  Options Strategy Recommender

A Streamlit web app that recommends options trading strategies based on real-time stock prices and implied volatility. Perfect for learning, prototyping, and showcasing your understanding of market dynamics and options logic.

---

## Link to Application:

Click the link below to see a live demo of the app:

https://optionsstrategyrecommender-jorgzmrcct2juzrff2sbka.streamlit.app/


---

##  App Features

- Enter any stock ticker (e.g., `AAPL`, `TSLA`)
- Fetches real-time stock price and implied volatility using `yfinance`
- Recommends a suitable options strategy (e.g., Covered Call, Straddle)
- Simulates “What-if” scenarios by adjusting price and volatility

---

##  Tech Stack

| Tool              | Purpose                                |
|-------------------|----------------------------------------|
| `Streamlit`       | Frontend framework for interactive UI  |
| `yfinance`        | Fetch real-time market data            |
| `Python`          | Strategy logic and simulations         |
| `GitHub`          | Source control and collaboration       |
| `Streamlit Cloud` | App deployment                         |

---


##  Sample Use Case

> Input: `TSLA`  
> Price: `$850`, Implied Volatility: `70%`  
> Recommended Strategy: **Straddle**  
> Adjust price + IV to simulate market movement and preview new recommendations dynamically.

---

## How It Works

1. **Price/IV Retrieval**: `yfinance` gets the latest stock price and implied volatility.
2. **Strategy Selection**: Logic inside `app.py` maps market conditions to strategies.
3. **What-If Engine**: Simulations re-evaluate conditions after applying user-specified changes.

---


##  Built By

**Aastha Patel**  
Connect with me on [LinkedIn](https://www.linkedin.com/in/aastha-patel-b48b56208/)

---

##  To Run Locally

```bash
git clone https://github.com/AasthaPatel02/options_strategy_recommender.git
cd options_strategy_recommender
pip install -r requirements.txt
streamlit run app.py
