#Tip calculator entry level python project


print("Welcome to the tip calculator!.")
bill = input("What was the total bill $")
tip = input("what percentage tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")
bill_as_float = float(bill)
tip_as_float = float(tip)
people_as_int = int(people)
tip_as_float = tip_as_float/100
tip_as_float = tip_as_float+1
total_bill = bill_as_float*tip_as_float
each_person = total_bill/people_as_int
each_person_rounded = round(each_person, 2)
print(f"each person should pay ${each_person_rounded}")


#Dft