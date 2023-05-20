import string
import random

characters = list(string.ascii_letters + string.digits + " !@#$%^&*()")


def generate_password():
    password_length = int(input("Сколько символов должно быть в пароле? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)


option = input("Вы хотите сгенирировать пароль? (Да/Нет): ").lower()

if option == "да":
    generate_password()
elif option == "нет":
    print("Программа завершила работу")
    quit()
else:
    print("Введите Да или Нет")
    quit()
