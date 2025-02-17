print("Bank of python")

pin = int(input("Enter the pin number: "))

while pin !=1234:
    pin = int(input("Incorrect pin, Enter the pin number again: "))

    if pin == 1234:
        print("Pin accepted! Enjoy your money")
