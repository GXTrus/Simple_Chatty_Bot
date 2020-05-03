def end():
    print('Congratulations, have a nice day!')


def test():
    print("Let's test your programming knowledge.")
    # test 1
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    answer = False
    while not answer:
        a = input()
        if a == 'a' or a == '2':
            answer = True
        else:
            print("Please, try again")

    print('Completed, have a nice day!')


def make_counter():
    print('Now I will prove to you that I can count to any number you want.')
    for i in range(int(input()) + 1):
        print(i, '!')
    print('Completed, have a nice day!')


class SimpleChattyBot:

    def __init__(self):
        self.bot_name = "Aid"
        self.birth_year = 2020
        self.your_name = None
        self.your_age = None
        self.greet()
        self.remind_name()
        self.guess_age()
        make_counter()
        test()
        end()

    def greet(self):
        print(f"Hello! My name is {self.bot_name}.")
        print(f"I was created in {self.birth_year}.")

    def remind_name(self):
        self.your_name = input("Please, remind me your name.\n")
        print(f"What a great name you have, {self.your_name}!")

    def guess_age(self):
        print("Let me guess your age.")
        print("Say me remainders of dividing your age by 3, 5 and 7.")
        self.your_age = (int(input()) * 70 + int(input()) * 21 + int(input()) * 15) % 105
        print(f"Your age is {self.your_age}; that's a good time to start programming!")


bot = SimpleChattyBot()
