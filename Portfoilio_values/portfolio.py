def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    total_value = 0
    for stock, quantity in stocks.items():
        total_value += quantity * prices.get(stock, 0)
    return total_value


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    return ((current_value - initial_value) / initial_value) * 100


def get_most_profitable_stock(prices: dict, initial_prices: dict) -> str:
    most_profitable_stock = max(prices, key=lambda stock:
                                                        (prices.get(stock, 0) - initial_prices.get(stock, 0)) *
                                                         100 / initial_prices.get(stock, 0))
    return most_profitable_stock
