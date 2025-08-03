def safe_divide(numerator, denominator):
    try:
        # Converting inputs to float
        num = float(numerator)
        den = float(denominator)

        # Attempting division
        result = num / den
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."