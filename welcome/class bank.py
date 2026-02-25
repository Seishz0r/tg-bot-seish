class bankAcc:
    Owner = None
    Balance = 0

    def __init__(self, owner, balance = 0):
        self.set_owner(owner)
        self.get_balance()
        self.bankomat(owner)

    def bankomat(self, owner):
        action = input('Что вы хотите сделать: пополнить снять баланс стоп: ')
        while action != 'стоп':
            if action == 'пополнить':
                amount = int(input('Введите сумму: '))
                self.deposit(amount)
                print('Средства внесенны на баланс')
                break
            if action == 'снять':
                amount = int(input('Введите сумму: '))
                self.withdraw(amount)
                print('Средства сняты с баланса')
                break
            if action == 'баланс':
                self.get_balance()
                break
            if action == 'стоп':
                break



    def set_owner(self, owner, balance = 0):
        self.Owner = owner
        self.Balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.Balance += amount
        else:
            print('Нельзя внести отрицательную сумму!')

    def withdraw(self, amount):
        if amount <= self.Balance:
            self.Balance -= amount
        elif amount <= 0:
            print('Нельзя снять отрицательную сумму!')
        else:
            print('Недостаточно средств!')

    def get_balance(self):
        print(self.Owner, 'Ваш баланс:', self.Balance)

acc = bankAcc('Alex')
acc.get_balance()