print("welcome to the tip calculator.")

bill = float(input("what was the total bill? $"))


tip_in_percentage = int(input(
    "What percenatage tip would you like to give? 10,12, or 15?\n"))

split_bill_by_people = int(input("how many people to split your bill by? \n"))


tip_as_percent = tip_in_percentage/100

total_tip = bill*tip_as_percent

total_bill = bill * total_tip

bill_per_person = total_bill/split_bill_by_people

final_bill = round(bill_per_person, 2)

print(f"eac h person pay: $ {final_bill}")
