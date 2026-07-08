#Basic Bank Menu System
print('Welcome to hara bhara bank customer portal')
print('='*100)
import random
name=input('Enter your name: ')
query=''' Select Your choice..
1. Balance Enquiry
2.Raise Complaint
3.Give Feedback
4.Connect Customer Care
5. Exit
'''
print('query')
choice=int(input('Choose option: '))
if choice==1:
    print(f'Your current balance is Rs. {random.randint(1000,5000)}')
elif choice==2:
  print('Sorry to hear that you faced problem')
  print('Enter your complaint')
  comp=input(':\n')
  print('We have received your complaint')
  cid= random.randint(100,999)
  print(f'Your complaint id is {cid}')

elif choice==3:
  feedback=int(input('Enter your rating(1-5)'))
  print(f'Thanks for rating us {"⭐"*feedback} stars')
elif choice==4:
  print('You can connect to our customer care at 📞+91 9897198971')
elif choice==5:
  print('Thank you for using our services')
else:
  print('❌Invalid choice❌')
