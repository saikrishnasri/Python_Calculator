## This Code is Python Calculator
# try:
# 	choice=int(input('Enter 1 for Addition\nEnter 2 for Subtraction \nEnter 3 for Multiply \nEnter 4 for Division'))
# 	if choice <=4 and choice >=1:
# 		num1=float(input('Enter the first number :'))
# 		num2=float(input('Enter the second number :'))
# 		if choice ==1:
# 			result=num1+num2
# 			print('Result :',result)
# 		elif choice ==2:
# 			result=num1-num2
# 			print('Result :',result)
# 		elif choice ==3:
# 			result=num1*num2
# 			print('Result :',result)
# 		elif choice ==4:
# 			result=num1/num2
# 			print('Result :',result)
# 	else:
# 		print('Please Select A Valid Choice')
# except ValueError:
# 	print('Please Enter In Digits')


## This Code is Another Way of Python Calculator

## This function adds two numbers
def add(x,y):
	try:
		return x+y
	except Exception as e:
		return "Unable to add given numbers"
## This function subtracts two numbers
def subtract(x,y):
	try:
		return x-y
	except Exception as e:
		return "Unable to subtract given numbers"
## This function multiples two numbers
def multiply(x,y):
	try:
		return x*y
	except Exception as e:
		return "Unable to multiply given numbers"
## This function divides two numbers
def divide(x,y):
	try:
		return x/y
	except Exception as e:
		return "Unable to division given numbers"

print("Please Select Your Operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

## Take input from the user
choice =input("Enter Choice(1/2/3/4): ")

##Check if choice is one of the four options
if choice in ('1','2','3','4'):
	num1=float(input("Enter first number: "))
	num2=float(input("Enter second number: "))

	if choice =='1':
		print(num1,"+",num2,"=",add(num1,num2))
	elif choice =='2':
		print(num1,"-",num2,"=",subtract(num1,num2))
	elif choice =='3':
		print(num1,"*",num2,"=",multiply(num1,num2))
	elif choice =='4':
		print(num1,"/",num2,"=",divide(num1,num2))
	#break
else:
	print("Please Select A Valid Option")