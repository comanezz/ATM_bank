class User():
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def show_details(self):
    print('"Personal details:"')
    print(f'Name: {self.name}')
    print(f'Age: {self.age}')
    print(f'Gender: {self.gender}')

class Bank(User):
  def __init__(self, name, age, gender):
    super().__init__(name, age, gender)
    self.balance = 100

  def deposit(self, amount):
    self.balance += + amount
    print(f'Your account balance is {self.balance}')

  def withdraw(self, amount):
    if amount > self.balance:
      print('You do not have the funds')
    else:
      self.balance -= amount
      print(f'Your account balance is {self.balance}')
  
  def view_balance(self):
    self.show_details()
    print(f'Your account balance is {self.balance}')

aymeric = Bank('Aymeric', 30, 'male')
aymeric.withdraw(30)
aymeric.view_balance()