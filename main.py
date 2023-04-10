def st_to_asc(input_string):
    ascii_list = [ord(char) for char in input_string]
    return ascii_list

def dec_to_etc(decimal):
    hex_val = hex(decimal)
    oct_val = oct(decimal)
    bin_val = bin(decimal)
    ascii_val = chr(decimal)
    return hex_val, oct_val, bin_val, ascii_val

def hex_to_etc(hex_val):
    decimal_val = int(hex_val, 16)
    oct_val = oct(decimal_val)
    bin_val = bin(decimal_val)
    ascii_val = chr(decimal_val)
    return decimal_val, oct_val, bin_val, ascii_val

def oct_to_etc(octal_val):
    decimal_val = int(octal_val, 8)
    hex_val = hex(decimal_val)
    bin_val = bin(decimal_val)
    ascii_val = chr(decimal_val)
    return decimal_val, hex_val, bin_val, ascii_val

def bny_to_etc(binary_val):
    decimal_val = int(binary_val, 2)
    hex_val = hex(decimal_val)
    oct_val = oct(decimal_val)
    ascii_val = chr(decimal_val)
    return decimal_val, hex_val, oct_val, ascii_val

def firstmenu():
    print("Conversion Menu:")
    print("1. Convert String to ASCII")
    print("2. Convert Decimal to Hexadecimal, Octal, Binary, and ASCII")
    print("3. Convert Hexadecimal to Decimal, Octal, Binary, and ASCII")
    print("4. Convert Octal to Decimal, Hexadecimal, Binary, and ASCII")
    print("5. Convert Binary to Decimal, Hexadecimal, Octal, and ASCII")
    print("6. Exit")

while True:
    firstmenu()
    secondmenu = input("Enter a choice: ")

    if secondmenu == '1':
        input_string = input("Enter a string: ")
        ascii_list = st_to_asc(input_string)
        print("Conversion result:", ascii_list)

    elif secondmenu == '2':
        decimal_val = int(input("Enter a decimal value: "))
        hex_val, oct_val, bin_val, ascii_val = dec_to_etc(decimal_val)
        print("Conversion result:")
        print("Hexadecimal:", hex_val[2:])
        print("Octal:", oct_val[2:])
        print("Binary:", bin_val[2:])

    elif secondmenu == '3':
        hex_val = input("Enter a hexadecimal value: ")
        decimal_val, oct_val, bin_val, ascii_val = hex_to_etc(hex_val)
        print("Conversion result:")
        print("Decimal:", decimal_val)
        print("Octal:", oct_val[2:])
        print("Binary:", bin_val[2:])

    elif secondmenu == '4':
        octal_val = input("Enter an octal value: ")
        decimal_val, hex_val, bin_val, ascii_val = oct_to_etc(octal_val)
        print("Conversion result:")
        print("Decimal:", decimal_val)
        print("Hexadecimal:", hex_val[2:])
        print("Binary:", bin_val[2:])

    elif secondmenu == '5':
        binary_val = input("Enter a binary value: ")
        decimal_val, hex_val, oct_val, ascii_val = bny_to_etc(binary_val)
        print("Conversion result:")
        print("Decimal:", decimal_val)
        print("Hexadecimal:", hex_val[2:])
        print("Octal:", oct_val[2:])

    elif secondmenu == '6':
        print("Good bye")
        break

    else:
        print("Error, try insert between 1-6 or else this will appear again")