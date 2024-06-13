import pandas as pd

def calculate_imn(max_leverage):
    """
    Calculate the Impact Margin Notional (IMN) for USD-Margined contracts.
    
    Parameters:
        max_leverage (int): The maximum leverage level.
        
    Returns:
        int: The Impact Margin Notional (IMN).
    """
    initial_margin_rate = 1 / max_leverage
    imn = 200 / initial_margin_rate #Given that USD-M Contracts example was gievn in the Binance Doc
    return int(imn)

def get_impact_prices(bid_orderbook, ask_orderbook, imn):
    """
    Get the impact bid and ask prices from the order books.
    
    Parameters:
        bid_orderbook (pd.DataFrame): The bid order book with 'Price' and 'Quantity' columns. (Assuming that it is arranged in a pandas df)
        ask_orderbook (pd.DataFrame): The ask order book with 'Price' and 'Quantity' columns. (Assuming that it is arranged in a pandas df)
        imn (int): The Impact Margin Notional.
        
    Returns:
        tuple: The impact bid price and impact ask price.
    """
    ## Impact bid price =IMN / [(IMN-multiplier *∑px-1*qx-1)/px+multiplier * ∑qx-1]
    # Calculate accumulated value for bid orderbook
    bid_orderbook['Accumulated'] = bid_orderbook['Price'] * bid_orderbook['Quantity'].cumsum()
    bid_idx = bid_orderbook['Accumulated'].ge(imn).idxmax()
    impact_bid_price = bid_orderbook.loc[bid_idx, 'Price']

    # Calculate accumulated value for ask orderbook
    ask_orderbook['Accumulated'] = ask_orderbook['Price'] * ask_orderbook['Quantity'].cumsum()
    ask_idx = ask_orderbook['Accumulated'].ge(imn).idxmax()
    impact_ask_price = ask_orderbook.loc[ask_idx, 'Price']

    return impact_bid_price, impact_ask_price


def calculate_funding_rate(impact_bid_price, impact_ask_price, index_price):
    """
    Calculate the funding rate for a perpetual future.
    
    Parameters:
        impact_bid_price (float): The impact bid price.
        impact_ask_price (float): The impact ask price.
        index_price (float): The index price.
        
    Returns:
        float: The funding rate.
    """
    # Funding Rate (F) = Average Premium Index (P) + clamp (interest rate - Premium Index (P), 0.05%, -0.05%)
    premium_index = (max(0, impact_bid_price - index_price) - 
                     max(0, index_price - impact_ask_price)) / index_price
    
    interest_rate = 0.0003 # In Binance, the interest rate is fixed (0.03% daily and 0.01% per funding cycle [8 hours cycle])
    
    # Clamp function to restrict values within a range
    def clamp(value, min_value, max_value):
        return max(min_value, min(value, max_value))
    
    clamped_value = clamp(interest_rate - premium_index, -0.0005, 0.0005)
    funding_rate = premium_index + clamped_value
    
    return funding_rate

# Example usage:
impact_bid_price = 49900
impact_ask_price = 50200
index_price = 50000

funding_rate = calculate_funding_rate(impact_bid_price, impact_ask_price, index_price)

print(f"Funding Rate: {funding_rate}")