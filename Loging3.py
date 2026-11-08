def login(username, password):
    correct_username = "admin"
    correct_password = "secretpassword"

    try:
        assert username == correct_username and password == correct_password, "Невірне ім'я користувача або пароль"
    except AssertionError as e:
        print(e)
    else:
        print("Вхід виконано успішно")

login("admin", "secretpassword")