class PasswordManager:
    def __init__(self, password: str):
        self.__password = password

    def __get_password(self):
        return self.__password

    # TODO: Implement the verify_password method
    def verify_password(self, valid_pass: str) -> bool:
        return valid_pass == self.__get_password()


# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))  # Should print: False
