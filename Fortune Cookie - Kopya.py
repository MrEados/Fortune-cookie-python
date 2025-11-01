import random
def fortune_cookie():
    cookies = [
        "A smooth sea never made a skilled sailor.",
        "Your creative energy is on the rise.",
        "The greatest risk is not taking one.",
        "Good things come to those who wait.",
        "Be the change that you wish to see in the world.",
        "A journey of a thousand miles begins with a single step.",
        "Listen to your heart and follow your instincts.",
        "Success is within your reach.",
        "Don't let yesterday take up too much of today.",
        "The best way to predict the future is to create it."
        ]
    print('Welcome to the Fortune Cookie!')
    while True:
        try:
            q = int(input('If you want a cookie please press 1, if you had enough for today press 2: '))
            if q == 1:
                one_cookie = random.choice(cookies)
                print(f'Your Fortune: {one_cookie}')
            elif q == 2:
                print('Have a nice day!')
                break
            else:
                print('Wrong input!')
        except ValueError:
            print('Wrong input!')
fortune_cookie()


