letter = '''Dear <|name|>,
you are selected !

Date: <|Date|>
'''
name = input("Enter your name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
