class SimpleChattyBot:

    def __init__(self):
        self.bot_name = "Aid"
        self.birth_year = 2020
        self.show_info()
        self.ask_name()
        self.show_your_name()

    def show_info(self):
        print(f"Hello! My name is {self.bot_name}.")
        print(f"I was created in {self.birth_year}.")

    def ask_name(self):
        self.your_name = input("Please, remind me your name.\n")

    def show_your_name(self):
        print(f"What a great name you have, {self.your_name}!")


bot = SimpleChattyBot()
