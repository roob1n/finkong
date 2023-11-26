def format_currency(value):
    # Format the value as "CHF 1'200.00"
    formatted_value = f"CHF {value:,.2f}".replace(',', "'")
    return formatted_value