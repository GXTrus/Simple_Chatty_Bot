class SimpleChattyBot:

    def __init__(self):
        self.bot_name = "Aid"
        self.birth_year = 2020
        self.show_info()
        self.ask_show_name()
        self.ask_show_age()
        self.make_counter()

    def show_info(self):
        print(f"Hello! My name is {self.bot_name}.")
        print(f"I was created in {self.birth_year}.")

    def ask_show_name(self):
        self.your_name = input("Please, remind me your name.\n")
        print(f"What a great name you have, {self.your_name}!")

    def ask_show_age(self):
        print("Let me guess your age.")
        print("Say me remainders of dividing your age by 3, 5 and 7.")
        self.your_age = (int(input()) * 70 + int(input()) * 21 + int(input()) * 15) % 105
        print(f"Your age is {self.your_age}; that's a good time to start programming!")

    def make_counter(self):
        print('Now I will prove to you that I can count to any number you want.')
        for i in range(int(input()) + 1):
            print(i, '!')

        print('Completed, have a nice day!')


bot = SimpleChattyBot()
