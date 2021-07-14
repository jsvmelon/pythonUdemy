import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name: str, balance: int):
        self._name = name
        self.__balance = balance
        self._transaction_log = [(Account._current_time(), balance)]
        print("Account created for {} with an initial balance of {}".format(self._name, balance))

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.__balance += amount  # this is discouraged
            self.show_balance()
            self._transaction_log.append((Account._current_time(), amount))
        else:
            print("The deposit amount must be positive and non zero")

    def withdraw(self, amount: int) -> None:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.show_balance()
            self._transaction_log.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and less or equal to balance")

    def show_balance(self) -> None:
        print("Balance is {}".format(self.__balance))

    def show_log(self):
        for date, amount in self._transaction_log:
            if amount > 0:
                transaction_type = "deposited"
            else:
                transaction_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".
                  format(amount, transaction_type, date, date.astimezone()))


if __name__ == "__main__":
    js_account = Account("Jean-Sacha", 10000)
    js_account.show_balance()

    js_account.deposit(102)
    js_account.deposit(2)
    js_account.deposit(34)
    js_account.deposit(67)
    js_account.show_balance()
    js_account.withdraw(500)
    js_account.show_balance()
    js_account.withdraw(34234234234)

    js_account.show_log()

    steph = Account("Steph", 800)
    steph._Account__balance = 200  # name mangling changes the name of __balance
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_log()
    print(steph.__dict__)
