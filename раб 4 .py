import keyboard

def check_password(password):
    assert len(password) >= 8, "Пароль должен содержать как минимум 8 символов"
    assert any(char.isupper() for char in password), "Пароль должен содержать хотя бы одну заглавную букву"
    assert any(char.isdigit() for char in password), "Пароль должен содержать хотя бы одну цифру"

    return "ok"

def main():
    try:
        while True:
            password = input("Введите пароль: ")
            try:
                result = check_password(password)
                print(result)
                break
            except AssertionError as e:
                print(f"Ошибка: {e.__class__.__name__}")
    except KeyboardInterrupt:
        print("Bye-Bye")

if __name__ == "__main__":
    main()