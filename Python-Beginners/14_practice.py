# name = input("Enter name ")
# print("Good afternoon "+ name)

Letter =''' <|name|> you are selected \n at Date: <|Date|>'''

name = input("Enter name\n")
Date = input("Enter Date\n")
Letter.replace("<|name|>", name)
Letter.replace("<|Date|>", Date)
print(Letter)
