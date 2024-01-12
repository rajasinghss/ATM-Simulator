import time as t


user_pin = 1234
user_balance = 728764.59
user_name = "Kumar Raja"
print("\n========= Welcome to your bank account =========\n\n\t\t",
      user_name, end="\n\n")

choice = 9

while (True):
    print("0. Logout and Exit")
    print("1. View Account Balance")
    print("2. Withdraw Cash")
    print("3. Deposit Cash")
    print("4. Change PIN")
    print("5. Return Card")
    choice = int(input("\nEnter number to proceed > "))
    print("\n")

    if choice == 0:
        print("Exiting...\n")
        t.sleep(2)
        print("You have been logged out Successfully. \n\tThank you!\n\n\tVisit Again.\n")
        break

    elif choice in (1, 2, 3, 4, 5):
        num_of_tries = 3
        while (num_of_tries != 0):
            input_pin = int(input("Please enter your 4-digit PIN > "))

            if input_pin == user_pin:
                print("Account auhtorized!\n\n")

                if choice == 1:
                    print("Loading Account Balance...")
                    t.sleep(2)
                    print("Your Current Balance is ₹ ",
                          '%.2f' % user_balance, end="\n\n")
                    break
                elif choice == 2:
                    print("Opening Cash Withdrawal...")
                    t.sleep(1.5)

                    while(True):
                        withdraw_amt = float(
                            input("Enter the amount you wish to withdraw > "))

                        if withdraw_amt > user_balance:
                            print("Can't withdraw ₹ ", withdraw_amt)
                            print(
                                "\nThe amount you input is more than your bank balance. Please input the currect amount.")
                            continue

                        else:
                            print("Withdrawing ₹ ", withdraw_amt)
                            confirm = input("Confirm? Y/N > ")
                            if confirm in ('Y', 'y'):
                                user_balance -= withdraw_amt
                                print("Amount withdrawn - ₹ ", withdraw_amt)
                                print("Remaining balance - ₹ ",
                                      '%.2f' % user_balance, end="\n\n\n")
                                break

                            else:
                                print("Cancelling transaction...")
                                t.sleep(1)
                                print("Transaction Cancelled!\n\n")
                                break

                    break

                elif choice == 3:
                    print("Loading Cash Deposit...")
                    t.sleep(1.5)

                    deposit_amt = float(
                        input("Enter the amount you wish to deposit > "))
                    print("Depositing ₹", deposit_amt)
                    confirm = input("Confirm? Y/N > ")
                    if confirm in ('Y', 'y'):
                        user_balance += deposit_amt
                        print("Amount deposited - ₹ ", deposit_amt)
                        print("Updated balance - ₹ ",
                              '%.2f' % user_balance, end="\n\n\n")
                    else:
                        print("Cancelling transaction...")
                        t.sleep(1)
                        print("Transaction Cancelled!\n\n")

                    break

                elif choice == 4:
                    print("Loading PIN Change...")
                    t.sleep(1.5)

                    pin_new = int(input("Enter your new PIN > "))

                    print("Changing PIN to", pin_new)
                    confirm = input("Confirm? Y/N > ")
                    if confirm in ('Y', 'y'):
                        user_pin = pin_new
                        print("PIN changed successfully! \n\n")
                    else:
                        print("Cancelling PIN change...")
                        t.sleep(1)
                        print("Process Cancelled!\n\n")

                    break

                else:
                    print("Loading Card Return...")
                    t.sleep(1.5)

                    print("Returning your ATM Card")
                    confirm = input("Confirm? Y/N > ")
                    if confirm in ('Y', 'y'):
                        print("Card returned successfully! \n\n")
                    else:
                        print("Cancelling process...")
                        t.sleep(1)
                        print("Process Cancelled!\n\n")

                    break

            else:
                num_of_tries -= 1
                print("PIN incorrect! Number of tries left -",
                      num_of_tries, end="\n\n")

        else:
            print("Exiting...")
            t.sleep(2)
            print("You have been logged out. Thank you!\n\n")
            break

    else:
        print("Invalid input!")
        print("\t\t0. Enter 0 to Logout and Exit!")
        continue
