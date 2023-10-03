0x01. Python - if/else, loops, functions
Python

Python if statement
The if statement is the most simple decision-making statement. It is used to decide whether a certain statement or block of statements will be executed or not.

Syntax: 

if condition:
   # Statements to execute if
   # condition is true

Python If-Else Statement
The if statement alone tells us that if a condition is true it will execute a block of statements and if the condition is false it won’t. But if we want to do something else if the condition is false, we can use the else statement with if statement to execute a block of code when the if condition is false. 

Syntax: 

if (condition):
    # Executes this block if
    # condition is true
else:
    # Executes this block if
    # condition is false


Nested-If Statement in Python
A nested if is an if statement that is the target of another if statement. Nested if statements mean an if statement inside another if statement. Yes, Python allows us to nest if statements within if statements. i.e., we can place an if statement inside another if statement.

Syntax: 

if (condition1):
   # Executes when condition1 is true
   if (condition2): 
      # Executes when condition2 is true
   # if Block is end here
# if Block is end here

Here, a user can decide among multiple options. The if statements are executed from the top down. As soon as one of the conditions controlling the if is true, the statement associated with that if is executed, and the rest of the ladder is bypassed. If none of the conditions is true, then the final else statement will be executed.

Syntax: 

if (condition):
    statement
elif (condition):
    statement
.
.
else:
    statement



