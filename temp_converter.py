
# rewrite to use functions 



def convert_to_fahrenheit(temp_celsius: float) -> float:
    return (temp_celsius * 9/5) + 32

def display_results(temp_celsius: float, temp_fahrenheit: float) -> None:
    print(f"{temp_celsius} degrees Celsius is equal to {temp_fahrenheit} degrees Fahrenheit.")

def process_conversion(temp_celsius: float) -> None:
    temp_fahrenheit: float = convert_to_fahrenheit(temp_celsius)

    display_results(temp_celsius, temp_fahrenheit)

if __name__ == "__main__":
    temp_celsius: float = float(input("Enter temperature in Celsius: "))
    process_conversion(temp_celsius)
