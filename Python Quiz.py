import random

def main():
    structure()
    print("Done")

def structure():
    no_x=0
    no_q=10
    no_wrong_trial=1
    quest_no=0
    score=0
    print('Press "q" to quit quiz\n')
    start_quiz=input("Type START: ").upper()
    while no_x<no_q:
        if start_quiz=="START":
            no_x+=1
            quest_no+=1
            print(f"Question No.{quest_no}")
            print(pick())
            print()
        else:
            no_wrong_trial+=1
            print("Invalid Input")
            start_quiz=input("Type START: ").upper()
            if no_wrong_trial==6:
                print("Try again later")
                break

#select question number
def pick():
    q=random.choice(range(30))
    #find question
    pic_quest=questions[q]
    print(pic_quest)
    #read answer
    ans_list=["A","B","C","D","E","Q"]
    ans=input("Answer: ").upper()
    if ans not in ans_list:
        return "INVALID INPUT"
    elif ans==str(answers[q]):
     return "CORRECT"
    elif ans=="Q":
        print("Thank you for participating in our quiz")
        return quit()
    else:
     return "INCORRECT"

questions= ("""\n1. Who developed Python Programming Language?
a) Wick van Rossum
b) Rasmus Lerdorf 
c) Guido van Rossum
d) Niene Stom""", """\n2. Which type of Programming does Python support?
a) object-oriented programming
b) structured programming
c) functional programming
d) all of the mentioned""", """\n3. Is Python case sensitive when dealing with identifiers?
a) no
b) yes
c) machine dependent
d) none of the mentioned""", """\n4. Which of the following is the correct extension of the Python file?
a) .python
b) .pl
c) .py
d) .p""", """\n5. Is Python code compiled or interpreted?
a) Python code is both compiled and interpreted
b) Python code is neither compiled nor interpreted
c) Python code is only compiled
d) Python code is only interpreted""", """\n6. All keywords in Python are in _________
a) Capitalized
b) lower case
c) UPPER CASE
d) None of the mentioned""", """7. What will be the value of the following Python expression?
4 + 3 % 5
a) 7
b) 2
c) 4
d) 1""", """8. Which of the following is used to define a block of code in Python language?
a) Indentation
b) Key
c) Brackets
d) All of the mentioned""",  """9. Which keyword is used for function in Python language?
a) Function
b) Def
c) Fun
d) Define""", """10. Which of the following character is used to give single-line comments in Python?
a) //
b) #
c) !
d) /*""", """11. Which of the following functions can help us to find the version of python that we are currently working on?
a) sys.version(1)
b) sys.version(0)
c) sys.version()
d) sys.version""", """12. Python supports the creation of anonymous functions at runtime, using a construct called __________
a) pi
b) anonymous
c) lambda
d) none of the mentioned""", """13. What is the order of precedence in python?
a) Exponential, Parentheses, Multiplication, Division, Addition, Subtraction
b) Exponential, Parentheses, Division, Multiplication, Addition, Subtraction
c) Parentheses, Exponential, Multiplication, Division, Subtraction, Addition
d) Parentheses, Exponential, Multiplication, Division, Addition, Subtraction""", """14. What does pip stand for python?
a) unlimited length
b) all private members must have leading and trailing underscores
c) Preferred Installer Program
d) none of the mentioned""", """15. Which of the following is true for variable names in Python?
a) underscore and ampersand are the only two special characters allowed
b) unlimited length
c) all private members must have leading and trailing underscores
d) none of the mentioned""", """16. Which of the following is the truncation division operator in Python?
a) |
b) //
c) /
d) %""", """17. Which of the following functions is a built-in function in python?
a) factorial()
b) print()
c) seed()
d) sqrt()""", """18. Which of the following is the use of id() function in python?
a) Every object doesn’t have a unique id
b) Id returns the identity of the object
c) All of the mentioned
d) None of the mentioned""", """19. What will be the output of the following Python function?
min(max(False,-3,-4), 2,7)
a) -4
b) -3
c) 2
d) False""", """20. Which of the following is not a core data type in Python programming?
a) Tuples
b) Lists
c) Class
d) Dictionary""", """21. Which of these is the definition for packages in Python?
a) A set of main modules
b) A folder of python modules
c) A number of files containing Python definitions and statements
d) A set of programs making use of Python modules""", """22. What will be the output of the following Python function?
len(["hello",2, 4, 6])
a) Error
b) 6
c) 4
d) 3""", """23. What is the order of namespaces in which Python looks for an identifier?
a) Python first searches the built-in namespace, then the global namespace and finally the local namespace
b) Python first searches the built-in namespace, then the local namespace and finally the global namespace
c) Python first searches the local namespace, then the global namespace and finally the built-in namespace
d) Python first searches the global namespace, then the local namespace and finally the built-in namespace""", """24. Which function is called when the following Python program is executed?
f = foo()
format(f)
a) str()
b) format()
c) __str__()
d) __format__()""", """25. Which one of the following is not a keyword in Python language?
a) pass
b) eval
c) assert
d) nonlocal""", """26. What arithmetic operators cannot be used with strings in Python?
a) *
b) –
c) +
d) All of the mentioned""", """27. Which of the following statements is used to create an empty set in Python?
a) ( )
b) [ ] 
c) { }
d) set()""", """28. To add a new element to a list we use which Python command?
a) list1.addEnd(5)
b) list1.addLast(5)
c) list1.append(5)
d) list1.add(5)""", """29. Which one of the following is the use of function in python?
a) Functions don’t provide better modularity for your application
b) you can’t also create your own functions
c) Functions are reusable pieces of programs
d) All of the mentioned""", """30. What is the maximum possible length of an identifier in Python?
a) 79 characters
b) 31 characters
c) 63 characters
d) none of the mentioned""")

answers=["C","D","A","C","B","D", "A", "A", "B", "B", "A", "C", "D", "C", "B", "B", "B", "B", "D", "C", "B", "C", "C", "C", "B", "B", "D", "C", "C", "D"]

main()