def check_password(password):
    try:
        assert len(password) >= 8, "Пароль должен содержать как минимум 8 символов"
        assert any(char.isupper() for char in password), "Пароль должен содержать хотя бы одну заглавную букву"
        assert any(char.isdigit() for char in password), "Пароль должен содержать хотя бы одну цифру"

        return "ok"
    except AssertionError as e:
        return f"error: {e}"
    except Exception as e:
        return f"error: Непредвиденная ошибка: {e}"


# Ввод пароля
password = input("Введите пароль: ")

# Проверка пароля
result = check_password(password)
print(result)