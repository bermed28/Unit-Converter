# Filename: project_1.py

### ADD YOUR NAME, STUDENT ID AND SECTION NUMBER BELOW ###
# NAME: LOL SCREW YOU JUANO PRIME
# STUDENT ID: YOU-AR-SOFT
# SECTION: LOL
############      DEFINE CONSTANTS BELOW      ############
KILOMETERS_IN_MILE = 1.60934
MILES_IN_KILOMETER = 0.62137
POUNDS_IN_KILOGRAM = 0.45359237
KILOGRAMS_IN_POUND = 2.20462262185

############       ADD YOUR CODE BELOW        ############

def convert_miles_to_kilometers():
    miles = input("Enter the miles to be converted: ")
    if is_float(miles):
        # Convert string to numeric miles
        miles = float(miles)
        # Conversion should be rounded to 2 decimal places.
        km =  round(miles * KILOMETERS_IN_MILE, 2)
        print(miles, "miles are equivalent to", km, "kilometers")
    else:
        print("Illegal unit of conversion. Input miles are not a number.")


def kilometersToMiles():
    kilometers = input("Enter the kilometers to be converted: ")
    if is_float(kilometers):
        # Convert string to numeric miles
        kilometers = float(kilometers)
        # Conversion should be rounded to 2 decimal places.
        miles = round(kilometers * MILES_IN_KILOMETER, 2)
        print(kilometers, "kilometers are equivalent to", miles, "miles")
    else:
        print("Illegal unit of conversion. Input kilometers are not a number.")


def poundsToKilograms():
    pounds = input("Enter the pounds to be converted: ")
    if is_float(pounds):
        # Convert string to numeric miles
        pounds = float(pounds)
        # Conversion should be rounded to 2 decimal places.
        kg = round(pounds * POUNDS_IN_KILOGRAM, 2)
        print(pounds, "pounds are equivalent to", kg, "kilograms")
    else:
        print("Illegal unit of conversion. Input pounds are not a number.")


def kilogramsToPounds():
    kg = input("Enter the kilograms to be converted: ")
    if is_float(kg):
        # Convert string to numeric miles
        kg = float(kg)
        # Conversion should be rounded to 2 decimal places.
        lbs = round(kg * KILOGRAMS_IN_POUND, 2)
        print(kg, "kilograms are equivalent to", lbs, "pounds")
    else:
        print("Illegal unit of conversion. Input kilograms are not a number.")

def celsiusToFahrenheit():
    c = input("Enter the degrees in Celsius to be converted: ")
    if is_float(c):
        # Convert string to numeric miles
        c = float(c)
        # Conversion should be rounded to 2 decimal places.
        conversion = (1.8 * c) + 32
        f = round(conversion, 2)
        print(c, "degrees Celsius are equivalent to", f, "degrees Fahrenheit")
    else:
        print("Illegal unit of conversion. Input degrees Celsius are not a number.")

def fahrenheitToCelsius():
    f = input("Enter the degrees in Fahrenheit to be converted: ")
    if is_float(f):
        # Convert string to numeric miles
        f = float(f)
        # Conversion should be rounded to 2 decimal places.
        conversion = (f - 32) / 1.8
        c = round(conversion, 2)
        print(f, "degrees Fahrenheit are equivalent to", c, "degrees Celsius")
    else:
        print("Illegal unit of conversion. Input degrees Fahrenheit are not a number.")


def mphToKmh():
    mph = input("Enter the Miles Per Hour to be converted: ")
    if is_float(mph):
        # Convert string to numeric miles
        mph = float(mph)
        # Conversion should be rounded to 2 decimal places.
        kmh = round(mph * KILOMETERS_IN_MILE, 2)
        print(mph, "Miles Per Hour are equivalent to", kmh, "Kilometers Per Hour")
    else:
        print("Illegal unit of conversion. Input Miles Per Hour are not a number.")

def kmhToMph():
    kmh = input("Enter the Kilometers Per Hour to be converted: ")
    if is_float(kmh):
        # Convert string to numeric miles
        kmh = float(kmh)
        # Conversion should be rounded to 2 decimal places.
        mph = round(kmh * MILES_IN_KILOMETER, 2)
        print(kmh, "Kilometers Per Hour are equivalent to", mph, "Miles Per Hour")
    else:
        print("Illegal unit of conversion. Input Kilometers Per Hour are not a number.")

def process_conversion(numericOption):
    if numericOption == 1:
        convert_miles_to_kilometers()
    elif numericOption == 2:
        kilometersToMiles()
    elif numericOption == 3:
        poundsToKilograms()
    elif numericOption == 4:
        kilogramsToPounds()
    elif numericOption == 5:
        celsiusToFahrenheit()
    elif numericOption == 6:
        fahrenheitToCelsius()
    elif numericOption == 7:
        mphToKmh()
    elif numericOption == 8:
        kmhToMph()
    # Add code to handle other menu selections.

############ DO NOT MODIFY THE SECTION BELOW  ############

def is_float(s):
    try:
        float(s)
        # Return True if no exception is thrown
        return True
    except ValueError:
        return False


def print_program_menu():
    print("\n--------")
    print( "Welcome to the unit conversion program. Please, choose an option:")
    print("1. Miles to kilometers")
    print("2. Kilometers to miles")
    print("3. Pounds to kilograms ")
    print("4. Kilograms to pounds")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    print("7. Miles/hour to kilometers/hour")
    print("8. Kilometers/hour to miles/hour")
    print("9. Exit")


def identify_option(option):
    # Verify that a number was input
    if option.isdigit():
        numericOption = int(option)
        # Check if the selection is within permitted range
        if numericOption >= 1 and numericOption <= 9:
            return numericOption
        else:
            return -1 # Invalid option
    else:
        return -1 # Invalid option


def main():
    done = False
    while not done:
        print_program_menu()
        userOption = input("Enter option: ")
        optionInfo = identify_option(userOption)
        if optionInfo != -1:
            # Option was valid
            if optionInfo == 9:
                done = True
                print ("Thanks for using the unit conversion program!")
            else:
                process_conversion(optionInfo)
        else:
            # Option was invalid
            print ("Invalid option\n")


# This line makes python start the program from the main function
if __name__ == "__main__":
    main()
