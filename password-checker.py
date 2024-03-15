username=input("What is your name....?")
password=input("what is your password....?")
password_length= len(password)
hidden_password= '*' * password_length
print(f"Hello {username}, Your password is {hidden_password} and {password_length} characters")