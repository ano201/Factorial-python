def factorial_num(num):
	factorial = 1
	for multiply in range(1, num+1):
		factorial*=multiply
	return factorial

while True:
	print("Type nothing or type without any integer to excit the program.")
	print("")
	try:
		enter_num = input("Enter Factorial number: ")
		calculated_factorial = factorial_num(int(enter_num))
		print(f'Factorial of "{enter_num}" is "{calculated_factorial}"')
		print("")
	except:
		break