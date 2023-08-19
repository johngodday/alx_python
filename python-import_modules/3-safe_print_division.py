def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print('Inside result: {}'.format(result))
    
    return result


print(safe_print_division(5, 5))