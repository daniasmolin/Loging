def check_age(age):
    try:
        assert age >= 18, "Вам має бути 18 років або більше"
    except AssertionError as e:
        print(e)
    else:
        print("Ви можете використовувати цей сервіс")

check_age(20)