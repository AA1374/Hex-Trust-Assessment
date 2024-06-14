def calculate_implied_funding_rate(calendar_future_price, spot_price, time_to_maturity_days):
    """
    Calculate the implied funding rate for a calendar future.
    
    Parameters:
        calendar_future_price (float): The price of the calendar future.
        spot_price (float): The spot price of the underlying asset.
        time_to_maturity_days (int): The time to maturity of the calendar future in days.
        
    Returns:
        float: The implied funding rate.
    """
    # Convert time to maturity from days to years
    time_to_maturity_years = time_to_maturity_days / 365.0
    
    # Calculate the implied funding rate
    implied_funding_rate = (calendar_future_price / spot_price) ** (1 / time_to_maturity_years) - 1

    return implied_funding_rate

# Example usage:
calendar_future_price = 1050
spot_price = 1000
time_to_maturity_days = 30

implied_funding_rate = calculate_implied_funding_rate(calendar_future_price, spot_price, time_to_maturity_days)

print(f"Implied Funding Rate: {implied_funding_rate:.3f}")