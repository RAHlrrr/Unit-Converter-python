def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    print("Welcome to the Temperature Converter!")
    while True:
        try:
            value = float(input("Enter a temperature value: "))
            source_unit = input("Enter source unit (Celsius or Fahrenheit): ").strip().lower()
            target_unit = input("Enter target unit (Celsius or Fahrenheit): ").strip().lower()

            if source_unit == "celsius" and target_unit == "fahrenheit":
                result = celsius_to_fahrenheit(value)
                print(f"{value} Celsius is equal to {result:.2f} Fahrenheit.")
            elif source_unit == "fahrenheit" and target_unit == "celsius":
                result = fahrenheit_to_celsius(value)
                print(f"{value} Fahrenheit is equal to {result:.2f} Celsius.")
            else:
                print("Invalid source or target units. Please enter 'Celsius' or 'Fahrenheit'.")

        except ValueError:
            print("Invalid input. Please enter a valid numeric temperature value.")
        
        another_conversion = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
        if another_conversion != "yes":
            break

temperature_converter()
