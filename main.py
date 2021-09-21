print("You can now start interacting with the SRPN calculator")

stack = [] # User input will be stored here and changed with calculations 
random_num_list = [1957747793, 1714636915, 1681692777, 846930886, 1804289383 ]
# I could not figure out random numbers in C so listed first 5 to be called


def process_command(str):# This is where the user input is processed and 
  if user_input == "+":  # directed to relavant function 
    addition()
  elif user_input == "-":
    subtraction()
  elif user_input == "*":
    multiply()
  elif user_input == "/":
    divide()
  elif user_input == "%":
    modulus()
  elif user_input == "=":
    try: # Viewed exceptions: https://docs.python.org/3/tutorial/errors.html
      saturation(stack[-1])
    except:
      empty_stack()
  elif user_input == "":
    empty_input()
  elif user_input == "d":
    print_stack(stack)
  elif user_input == "^":
    power()
  elif user_input == "#":
    comment()
  elif user_input == "r":
    random_num()
  else:
    stack.append(int(user_input))  


# Below are all functions called by the process command
# First are the calculation types
def addition():
  if len(stack) <= 1: # Checks if there are two values for calcualation 
    stack_underflow()
  else:
    result = pop() + pop()
    stack.append(result)

def subtraction():
  if len(stack) <= 1:
      stack_underflow()
  else:
    x = pop()   # Have to use pop on separte variables otherwise I would get a
    y = pop()   # negative number ie 11-3 = -8 not 8
    result = y - x
    stack.append((result))

def multiply():
  if len(stack) <= 1:
    stack_underflow()
  else:
    result = pop() * pop()
    stack.append(result)

def divide():
  if len(stack) <= 1:
    stack_underflow()
  elif stack[-1] == 0:
    zero() # checks if the first number is not being divided by zero
  else:
    x = pop()
    y = pop()
    result = int(y / x)
    stack.append(result)

def modulus():
  if len(stack) <= 1:
      stack_underflow()
  elif stack[-1] == 0:
    zero()
  else:
     x = pop()
     y = pop()
     result = y % x
     stack.append(result)

def power():
  if len(stack) <= 1:
      stack_underflow()
  else:
    x = pop()
    y = pop()
    result = y**x
    stack.append(result)


# Next are the other accepted inputs
def saturation(sat): # Triggered by "="
  if sat > -2147483648 and sat < 2147483647:
    print(sat)
  elif sat <= -2147483648:
    print(-2147483648)
  else: 
    print(2147483647)

def empty_stack(): # Triggered by "="
  if len(stack) == 0:
    print("Stack empty.")   

def empty_input():# Allows empty input to be accepted 
    return 0

def print_stack(stack):       # Viewed built in functions:
  for i in range(len(stack)): # https://docs.python.org/3/library/functions.html
    print(stack[i])
    
def comment(): # Can comment, but have to enter single comment first
  user_input = input()
  while user_input != "#":
    user_input = input()

def random_num(): 
  random_number = random_num_list.pop()
  stack.append(random_number)

  if len(random_num_list) == 0: # Stops error when list is empty
    return 0


# Next are useful funcitons used
def stack_underflow(): 
    print("Stack underflow.")
    
def zero():
    print("Divide by 0.")

def pop():
  return stack.pop() # Just pops the stack when called (only stack)


# This is the main loop of the program, sending input to process_command
while True:
  try: # Viewed exceptions: https://docs.python.org/3/tutorial/errors.html
    user_input = input()
    process_command(user_input)
  except:
    print('Unrecognised operator or operand '+ '"' + (user_input) + '".')

# Link to Repl.it: https://repl.it/@tdw20/Calc#main.py