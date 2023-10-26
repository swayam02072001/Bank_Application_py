class Bank():
    Bank_name = "SBI"
    Branch_Name = "MARATHAHALLI"
    IFSC = "SBIN000123"
    ROI = 0.02

    def __init__(self, name, accno, mno, bal, pin):
        self.name = name
        self.accno = accno
        self.mno = mno
        self.bal = bal
        self.pin = pin

    @staticmethod
    def validate():
        return int(input("Enter the 4 digit PIN: "))

    def deposit(self):
        if self.pin == self.validate():
            amount = float(input("Enter the amount to deposit: "))
            self.bal += amount
            print("The money you entered is credited to your account successfully")
        else:
            print("----Incorrect PIN----")

    def withdraw(self):
        if self.pin == self.validate():
            money = float(input("Enter the amount to withdraw: "))
            if self.bal >= money:
                self.bal -= money
                print("Money withdrawal Successful")
            else:
                print("Insufficient Balance")
        else:
            print("----Incorrect PIN----")

    def check_bal(self):
        if self.pin == self.validate():
            print(f'{self.name}\'s balance is {self.bal}')
        else:
            print("Incorrect PIN")

    def change_pin(self):
        if self.pin == self.validate():
            pin1 = int(input("Enter the new PIN: "))
            pin2 = int(input("Enter the new PIN again: "))
            if pin1 == pin2:
                self.pin = pin1
                print("PIN changed successfully")
            else:
                print("PIN does not match")
        else:
            print("Incorrect pin")

    @classmethod
    def change_ROI(cls):
        new_roi = float(input("Enter the new ROI value: "))
        cls.ROI = new_roi


b1 = Bank('abi', 5454545454545, 255465546, 65000, 5555)
b2 = Bank('abhi', 8511541511515, 2644454114, 55000, 2525)

b1.check_bal()
b1.deposit()
b1.check_bal()

b1.check_bal()
b1.withdraw()
b1.check_bal()

print(b1.pin)
b1.change_pin()
print(b1.pin)

b1.check_bal()

print(Bank.ROI)
Bank.change_ROI()
print(Bank.ROI)
