name=input("Enter patient name: ")
age=int(input("Enter patient age: "))
days=int(input("Enter the number of days patient was admitted: "))
room=input("Enter room type (General/Semi-Private/Private): ")
tests=int(input("Enter number of diagnostic tests conducted: "))
medicines=int(input("Enter number of medicines purchased: "))

def calculate_room_rent(room,days):
    if room_type == "General":
        return days * 1500
    elif room_type == "Semi-Private":
        return days * 2500
    elif room_type == "Private":
        return days * 4000

def calculate_test_charges(tests):
    return tests * 500

def calculate_medicine_charges(medicines):
    return medicines * 200

def calculate_subtotal(room_rent, test_charges, medicine_charges):
    return room_rent + test_charges + medicine_charges

def calculate_discount(subtotal,age):
    if (age<12):
        return (subtotal*75)/100
    elif (age>=60):
        return (subtotal*80)/100
    else:
        return subtotal
def additional_discount(subtotal):
    if(subtotal>50000):
        return (subtotal*95)/100
    else:
        return subtotal
total=additional_discount(calculate_discount(age,calculate_subtotal(calculate_medicine_charges(medicines),calculate_test_charges(tests),calculate_room_rent(room,days))))
print("Patient name:",name)
print("Total bill:",total)

            
   

