import pytz
import datetime


class Account:
    """ Simple account class with balance """
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._tranaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._tranaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.show_balance()
            self._tranaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than your balance")

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transaction(self):
        for date, amount in self._tranaction_list:
            if amount > 0:
                tran_type = "Deposited"
            else:
                tran_type = "WithDrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    raj = Account("Raj", 0)
    raj.show_balance()

    raj.deposit(1000)

    raj.withdraw(500)

    raj.withdraw(500)

    raj.withdraw(1)

    raj.show_transaction()

    kiki = Account("Kiki", 800)
    kiki.__balance = 200
    kiki.deposit(100)
    kiki.withdraw(200)
    kiki.show_transaction()
    print(kiki.__dict__)
    kiki._Account__balance = 50
    kiki.show_balance()