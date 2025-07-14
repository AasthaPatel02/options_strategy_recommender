def simulate_strategy(price, volatility, price_change, vol_change):
    new_price = price + price_change
    new_volatility = volatility + vol_change

    # Example logic based on new simulated conditions
    if new_volatility > 50:
        return "Straddle"
    elif new_price > price * 1.1:
        return "Covered Call"
    elif new_price < price * 0.9:
        return "Protective Put"
    else:
        return "Iron Condor"
