print(f"Byte Conversion Tool")
#Option1 = kilobytes
#Option2 = megabytes
#Option3 = terabyte
#Option4= terabyte_to_megabyte

def byteConversion():

    select_a_number = int(input('Enter a number to convert: '))

    print(f"Press 1 to convert from Kilobytes to bytes")
    print(f"Press 2 to convert from megabyte to bytes")
    print(f"Press 3 to convert from terabyte to bytes")
    print(f"Press 4 to convert from terabyte to megabyte")

    menu_option = int(input("Enter a number you wish to convert based on the options above: "))

    kilobytes = select_a_number*1024
    megabyte = select_a_number*1048576
    terabyte = select_a_number*1099511627776
    terabyte_to_megabyte = select_a_number*1000000

    if(menu_option == '1'):
        #if user selects option 1 to convert kilobytes to bytes:
        print(f"You have {kilobytes} bytes.")

    elif (menu_option == '2'):
        #else if user selects option 2 to convert megabyte to bytes:

        print(f"You have {megabyte} bytes.")

    elif(menu_option == '3'):
        #else if user selects option 3 to convert terabyte to bytes:

        print(f"You have {terabyte} bytes.")

    elif(menu_option == '4'):
        #else if user selects option 4 to convert terabyte to megabyte:
        print(f"You have {terabyte_to_megabyte} bytes.")
    else:
        print(f"That is not a valid selection.")

byteConversion()
