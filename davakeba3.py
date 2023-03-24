class Celsius:
    def __init__(self,temperature):
        self.__temperature = temperature

    def get_temp(self):
        return self.__temperature

    def set_temp(self, new_temperature):
        self.__temperature = new_temperature

    def del_temp(self):
        del self.__temperature

    temperature_prop = property(get_temp, set_temp, del_temp)

c1 = Celsius(10)
print(c1.temperature_prop)
c2 = Celsius(23)
print(c2.temperature_prop)

#2dav
class Bank_Account:
    def __init__(self, account_name, balance=0):
        self.__account_name = account_name
        self.__balance = balance

    def get_accountname(self):
        return self.__account_name
    def set_accountname(self,new_accountname):
        self.__account_name = new_accountname

    def __str__(self):
        return f" გამარჯობა {self.__account_name} თქვენს ანგარიშზე არის: {self.__balance}"

    def deposit(self, raodenoba):
        self.__balance += raodenoba
        print(f"თანხის შეტანა დასრულდა, ამჟამად თქვენ ანგარიშზე გაქვთ {self.__balance}:")

    def withdrow(self, raodenoba):
        self.__balance -= raodenoba
        print(f"თანხის გამოტანა შესრულებულია ამჟამად თქვენ ანგარიშზე გაქვთ {self.__balance}")

acc1 = Bank_Account("ანა–მარია", 1200)
print(acc1)
acc1.deposit(input("რიცხვი: "))
print(acc1)
acc1.withdrow(input("რიცხვი: "))
print(acc1)

