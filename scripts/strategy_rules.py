def recommend_strategy(price, volatility):
    if volatility < 20:
        return "Covered Call"
    elif volatility >= 50:
        return "Iron Condor"
    elif 20 <= volatility < 35:
        return "Bull Call Spread"
    elif 35 <= volatility < 50:
        return "Bear Put Spread"
    else:
        return "Straddle"
