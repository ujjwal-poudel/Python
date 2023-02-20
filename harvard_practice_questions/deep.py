"""
implement a program that prompts the user for the answer
to the Great Question of Life, the Universe and
Everything, outputting Yes if the user inputs 42
or (case-insensitively) forty-two or forty two.
Otherwise output No.
"""

answer = input("What is the answer to the Great Questin of Life, the Universe and Everything? ".lower())

if answer == "42":
    print("yes")
    
elif answer == "forty-two":
    print("yes")
    
elif answer == "forty_two":
    print("yes")
    
elif answer == "forty two":
    print('yes')
    
elif answer == 'fortytwo':
    print("yes")
    
else:
    print('no')