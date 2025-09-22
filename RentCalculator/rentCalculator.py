##Inputs
# Total rent
# Total Food ordered
#Electricity
#Charge per unit

# total amount per person

rent = int(input('Total Rent='))
food = int(input('Amount for Food ordered='))
electricity = int(input('Electricity units utilized='))
perUnit = int(input('Per Unit charge='))
person = int(input("'Total People living="))


total_bill = electricity * perUnit

output = (food+rent+total_bill) // person

print("Total Amount per person is $", output)

