def format_with_thousands(number):
    parts = str(number).split('.')
    integer_part = parts[0]
    decimal_part = parts[1] if len(parts) > 1 else '00'

    formatted_integer = ''
    for i, digit in enumerate(reversed(integer_part)):
        if i > 0 and i % 3 == 0:
            formatted_integer = ' ' + formatted_integer
        formatted_integer = digit + formatted_integer

    formatted_decimal = decimal_part.ljust(2, '0')  # Ensure there are always 2 decimal places

    formatted_number = formatted_integer + '.' + formatted_decimal
    return formatted_number
