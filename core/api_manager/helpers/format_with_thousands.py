def format_with_thousands(number):
    # Format number with thousands separator
    formatted_number = '{:,.2f}'.format(number)

    # Replace commas with spaces
    formatted_number = formatted_number.replace(',', ' ')

    return formatted_number