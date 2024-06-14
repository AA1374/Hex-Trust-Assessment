# Task 1: What is the funding rate associated with a perpetual future?
The funding rate in perpetual futures is a periodic payment exchanged between traders holding long and short positions. This mechanism ensures that the price of the perpetual futures contract remains close to the underlying asset's spot price.

## Funding Rate Calculation Logic

### Components of the Funding Rate:
1. **Interest Rate**: Fixed at 0.03% daily and 0.01% per funding cycle (8-hour cycle).
2. **Premium Index**: Reflects the difference between the perpetual futures price and the underlying asset's spot price.

### Key Definitions:
- **Impact Margin Notional (IMN)**: Defined as 200 USDT divided by the initial margin rate at the maximum leverage level.
- **Premium Index (P)**: Calculated as:
Premium Index (P) = [ Max(0, Impact Bid Price - Price Index ) - Max(0, Price Index - Impact Ask Price)] / Price Index

### Impact Prices:
- **Impact Bid Price**: The average fill price to execute the Impact Margin Notional at the Bid Price.
- **Impact Ask Price**: The average fill price to execute the Impact Margin Notional at the Ask Price.
- **Price Index**: The weighted average value of the underlying asset listed on major spot exchanges.

### Funding Rate Formula:
The funding rate (F) is calculated using the following formula:

Funding Rate (F) = Average Premium Index (P) + clamp (interest rate - Premium Index (P), 0.05%, -0.05%)

### Notes:
- The `clamp` function ensures that the funding rate adjustment is within the range of -0.05% to 0.05%.
- The `Interest Rate` component is fixed, while the `Premium Index` varies based on market conditions and the difference between bid/ask prices and the price index.

By understanding and using these components, traders can better anticipate the costs or earnings associated with holding perpetual futures positions.

# Task 2: How would you calculate an implied funding rate (or implied interest rate) for a calendar future? 

The implied funding rate can be derived from the difference between the calendar futures price and the spot price, adjusted for the time to maturity.

The formula for the implied funding rate is:

`implied_funding_rate = (calendar_future_price / spot_price) ** (1 / time_to_maturity_years) - 1`

Where:
- `calendar_future_price` is the price of the calendar future.
- `spot_price` is the spot price.
- `time_to_maturity_years` is the time to maturity of the future in years.

# Task 3:
I am facing problems trying to get the Perpetual Futures data, however, assuming that I had all the data in the Jupyter Notebook, my approach to tackle this problem would be as follows:

1. Retrieve all the Price data for BTCUSDT spot price, calendar futures and perpetual futures along with the associated Funding Rate.
2. Merge the 3 Price Data and then align the Funding Rate Data with the combined graph to analyze the spreads between Spot vs Calendar Futures, and Spot vs Perps.
3. Calculate the spread between calendar and perpetual futures prices 
4. Analyze the impact of funding rates on perpetual futures prices
5. Then based on the analysis from the Funding Rate and Price Data, I would define a min_threshold for my trading strategy.
6. Finally, I would generate trading signals based on spread
     - Generate trading signals based on the calculated spread:
      ```python
      if spread > spread_threshold:
          signal = -1  # Short calendar futures, long perpetual
      elif spread < -spread_threshold:
          signal = 1  # Long calendar futures, short perpetual
      else:
          signal = 0  # No action

7. Then I would backtest this strategy on the historical data to check its performance.