from art import logo
def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
  
}
def calculator():
  print(logo)
  num1 = int(input("first number"))
  for keys in operations: 
    print(keys)

  should_continue = True
  while should_continue:
    opr = input("enter operation")
    num2 = int(input("second number"))


    func = operations[opr]
    answer=func(num1,num2)
   
    print(f"{num1} {opr} {num2} = {answer}")

    cont=input("do you want to continue? press y for yes or n to start a new calculation")

    if(cont=="y"):
      num1=answer
    else:
      should_continue = False
      calculator()
   
calculator()