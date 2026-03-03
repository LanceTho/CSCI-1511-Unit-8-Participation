
# rewrite to use functions 



def convert_to_fahrenheit(temp_celsius: float) -> float:
    """Converts a temperature in celsius into fahrenheit

    Args:
        temp_celsius (float): temperature in celsius

    Returns:
        float: temperature in fahrenheit
    """
    return (temp_celsius * 9/5) + 32

def display_results(temp_celsius: float, temp_fahrenheit: float) -> None:
    """Displays the temperature in celsius and its equivalent temperature in fahrenheit

    Args:
        temp_celsius (float): temperature in celsius
        temp_fahrenheit (float): temperature in fahrenheit
    """
    print(f"{temp_celsius} degrees Celsius is equal to {temp_fahrenheit} degrees Fahrenheit.")

def process_conversion(temp_celsius: float) -> None:
    """Processes the whole conversion process between celsius and fahrenheit

    Args:
        temp_celsius (float): temperature in celsius
    """
    temp_fahrenheit: float = convert_to_fahrenheit(temp_celsius)

    display_results(temp_celsius, temp_fahrenheit)

if __name__ == "__main__":
    temp_celsius: float = float(input("Enter temperature in Celsius: "))
    process_conversion(temp_celsius)
