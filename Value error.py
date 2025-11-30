try:
    number = int(input("Enter a number: "))
    print("Number entered: ", number)

except ValueError as ex:
    print('exception:', ex)