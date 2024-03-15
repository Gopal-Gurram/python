class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter("Gopal", 25)
player2 = PlayerCharacter("nani", 28)

print(player1.name)
print(player2.name)
