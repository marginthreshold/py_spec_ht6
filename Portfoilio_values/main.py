from portfolio import calculate_portfolio_value, calculate_portfolio_return, get_most_profitable_stock

stocks = {"AAPL": 20, "GOOGL": 10, "MSFT": 100}
prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
initial_prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 750.50}

initial_value = calculate_portfolio_value(stocks, initial_prices)
current_value = calculate_portfolio_value(stocks, prices)

print("Общая стоимость портфеля акций:", current_value)
print("Доходность портфеля:", calculate_portfolio_return(initial_value, current_value), "%")
print("Наиболее прибыльная акция:", get_most_profitable_stock(prices, initial_prices))
