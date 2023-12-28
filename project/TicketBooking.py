print('Welcome to Booking Movie...')
name=input("please enter your name:- ")
seats=int(input('select number of seats,you want to book:- '))
category=int(input('enter the stage you want \n 1.Diamond \n 2.gold \n 3.silver \n'))
if category==1:
    amount=seats*200
if category==2:
    amount=seats*150
if category==3:
    amount=seats*200 
print(f'Hi {name} you have booked {seats} seats and total amount is {amount}')  