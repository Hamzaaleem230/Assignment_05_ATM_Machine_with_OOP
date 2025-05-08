# 💳 OOP Assignment in Python: ATM Machine

class ATM:
    def __init__(self, balance: float = 1000, pin: int = 1234):
        self.balance = balance
        self.pin = pin

    # 🔐 1. check_pin(input_pin) – check if the entered PIN is correct
    def check_pin(self, input_pin):
        if input_pin == self.pin:
            print("✅ PIN is correct. Access granted!")
            return True
        else:
            print("❌ Incorrect PIN. Access denied.")
            return False

    # 💰 2. check_balance() – print the current balance
    def check_balance(self):
        print(f"💵 Your current balance is: ${self.balance}")

    # ➕ 3. deposit(amount) – add the amount to balance if PIN is correct
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ ${amount} deposited successfully.")
            print(f"📈 Updated balance: ${self.balance}")
        else:
            print("⚠️ Invalid deposit amount. Please enter a positive number.")

    # ➖ 4. withdraw(amount) – withdraw the amount if balance is sufficient and PIN is correct
    def withdraw(self, amount):
        if amount <= 0:
            print("⚠️ Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("🚫 Insufficient balance. Please try a lower amount.")
        else:
            self.balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")
            print(f"📉 Remaining balance: ${self.balance}")

    # 🔚 5. exit() – end the program
    def exit(self):
        print("🙏 Thank you for using our ATM services. Goodbye! 👋")
        exit()

# -----------------------------------------------------------------------------

# 🧑‍💻 Bonus Task: Menu-based system with emojis and friendly prompts
def main():
    atm = ATM()
    print("🎉 Welcome to the Python ATM Machine 🏧")

    try:
        user_pin = int(input("🔑 Please enter your 4-digit PIN: "))
    except ValueError:
        print("❌ Invalid input! Numbers only.")
        return

    if not atm.check_pin(user_pin):
        return

    while True:
        print("\n📋 Please choose an option:")
        print("1️⃣ Check Balance")
        print("2️⃣ Deposit Money")
        print("3️⃣ Withdraw Money")
        print("4️⃣ Exit")

        choice = input("👉 Enter your choice (1-4): ")

        if choice == "1":
            atm.check_balance()

        elif choice == "2":
            try:
                amount = float(input("💸 Enter amount to deposit: $"))
                atm.deposit(amount)
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

        elif choice == "3":
            try:
                amount = float(input("🏧 Enter amount to withdraw: $"))
                atm.withdraw(amount)
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

        elif choice == "4":
            atm.exit()
            break

        else:
            print("⚠️ Invalid choice. Please select between 1 and 4.")

# 🚀 Run the program
if __name__ == "__main__":
    main()
