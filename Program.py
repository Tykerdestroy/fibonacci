term = int(input("How many terms? ")) 
num1, num2 = 0, 1 
count = 0
if term <= 0:
 print("Please enter a positive integer") 
elif term == 1:
 print("Fibonacci sequence upto",term,":") 
 print(num1) 
else:
 print("Fibonacci sequence:")
 while count < term:
  print(num1)
  final = num1 + num2
  n1 = n2 
  n2 = final 
  count += 1
