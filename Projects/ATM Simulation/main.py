#Python ATM Simulation Using OOP (Encapsulation)

class ATM:
  def __init__(self, bank_name):
    print(f"Welcome to {bank_name}Bank 🏦")
    self.bank_name =bank_name #Public
    self.__pin="0000" #Private
    self.__balance=2000 #Protected

  #class methods
  def __ask_pin(self): #Private method
      import getpass
      pin= getpass.getpass("Enter your 4 digit PIN: ")

      if pin ==self.__pin:
        return True
      else:
        return False
  def check_balance(self):
    if self.__ask_pin():
      print(f"Your Current balance is ₹{self.__balance}")
    else:
      print("Invalid PIN")

  def withdraw_amount(self):
    if self.__ask_pin():
      amount=int(input("Enter the amount you want to withdraw: "))
      if 0<amount<=self.__balance:
        print(f"AMount ₹{amount} withdrawl successfull")
        self.__balance-=amount
      else:
        print("Insufficient Balance")
    else:
      print("Invalid PIN")
  def change_pin(self):
    if self.__ask_pin():
      old_pin = input("Enter your old PIN: ")
      if old_pin == self.__pin:
        new_pin = input("Create your new PIN: ")
        pin_again= input("Enter again: ")
        if new_pin == pin_again:
          print("PIN changed successfully")
          self.__pin = new_pin
        else:
          print("PIN does not match")
      else:
        print("Invalid PIN")
    else:
      print("Invalid PIN")

#ATM object
sbi=ATM("SBI")

# ATM Menu
while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Withdraw Amount")
    print("3. Change PIN")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sbi.check_balance()

    elif choice == "2":
        sbi.withdraw_amount()

    elif choice == "3":
        sbi.change_pin()

    elif choice == "4":
        print("Thank you for using SBI ATM!")
        break

    else:
        print("Invalid choice. Please try again.")
