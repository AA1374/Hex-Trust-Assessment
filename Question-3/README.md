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

\[
\text{Implied Funding Rate} = \left(\frac{\text{calendar\_future\_price}}{\text{spot\_price}}\right)^{\frac{1}{\text{time\_to\_maturity\_years}}} - 1
\]

Where:
- \(\text{calendar\_future\_price}\) is the price of the calendar future.
- \(\text{spot\_price}\) is the spot price.
- \(\text{time\_to\_maturity\_years}\) is the time to maturity of the future in years.
