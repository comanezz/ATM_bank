user_name = 'Aymeric'
user_pin = 8272
user_balance = 7893.3
session_dashboard = True
count_wrong_pin = 0

# separate float number by 3 numbers and two numbers after decimal
def separate_float_by_three_digits(number):
  formatted_str = "{:,.2f}".format(number).replace(',',' ')
  return formatted_str

print(f'Welcome {user_name} to your bank account')

while True:
  user_input_pin = int(input('Enter your PIN: '))

  if user_input_pin == user_pin:
    print('Right PIN...')
    break
  else:
    print('Try again')

    count_wrong_pin += 1

    if count_wrong_pin == 3:
      print('You failed 3 times card blocked')
      session_dashboard = False
      break

while session_dashboard:
  print('''
      0. Logout and exit
      1. View account balance
      2. Withdraw cash
      3. Deposit cash
  ''')

  user_choice = int(input('Enter a number to proceed: '))

  if user_choice == 0:
    print('Logging out...')
    break
  
  elif user_choice == 1:

    while True:
      formatted_float = separate_float_by_three_digits(user_balance)

      print(f'Your account balance is {str(formatted_float)} €')
      print('\nWould you like to continue (1) or log out (0)')
      
      user_continue = int(input('\nPress 1 or 0: '))

      if user_continue == 1:
        break
      elif user_continue == 0:
        session_dashboard = False
        break
      else:
        print('\nNot a choice. Select 1 to continue or 0 to quit\n')
  elif user_choice == 2:
    amount_withdraw = int(input('\nHow much would you like to withdraw? ')) 

    if user_balance - amount_withdraw < 0:
      print('\nYou do not have the funds')
    else:
      user_balance -= amount_withdraw

      print(f'\nYou have {formatted_float} € left')
  elif user_choice == 3:
    deposit_amount = int(input('\nHow much would you like to deposit? '))
    user_balance += deposit_amount
    
    formatted_float = separate_float_by_three_digits(user_balance)
    print(f'\nYou have {formatted_float} € left')
  else:
    print('\nPlease select another number between (0-3)')
