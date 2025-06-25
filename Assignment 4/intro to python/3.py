def main():
    Temp = float(input("Enter the temperature in Fahrenhiet :"))
    celcius = (Temp - 32) * 5.0/9.0
    print(f"Temperature in Fahrenhiet {Temp} = {celcius:.2f}°C")

if __name__ == '__main__':
    main()