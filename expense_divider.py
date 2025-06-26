while True:
    try:
        print("Hi! Welcome to the Expense Divider & Tip Calculator.")
        total_bill = float((input("Please, tell me the total bill: ")))
        tip_value = int(input("How much tip would you like to give? 5%, 10%, 12% or 15% "))
        amount_of_consumers = int(input("Please, provide the number of consumers: "))
        if amount_of_consumers <= 0:
            print("The number of consumers must be greater than zero.")
            continue

        if tip_value == 5:
            tip_amount = total_bill * 0.05
        elif tip_value == 10:
            tip_amount = total_bill * 0.10
        elif tip_value == 12:
            tip_amount = total_bill * 0.12
        elif tip_value == 15:
            tip_amount = total_bill * 0.15
        else:
            print("Please, write one of the provided tip amounts.")
            continue

        final_amount_consumers = (total_bill + tip_amount) / amount_of_consumers
        print(f"Thank you for all the information. The total bill is {total_bill:.2f}, the tip is {tip_amount:.2f} and the amount that each consumer have to pay is {final_amount_consumers:.2f}.")

        break
    
    except ValueError:
        print("Invalid input. Please enter numeric values only.")