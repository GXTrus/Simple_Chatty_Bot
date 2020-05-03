# write your code here
class SimpleChattyBot:

    def __init__(self):
        self.bot_name = "Aid"
        self.birth_year = 2020

    def show_info(self):
        print(f"Hello! My name is {self.bot_name}.")
        print(f"I was created in {self.birth_year}.")


bot = SimpleChattyBot()
bot.show_info()
