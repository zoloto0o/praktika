import random
import string

def generate_password(length=12, use_digits=True, use_special=True, use_upper=True, use_lower=True):
    
    characters = ""
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*()_+-="
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase

    if not characters:
        raise ValueError("Должен быть выбран хотя бы один тип символов")

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    """
    Запрашивает параметры для генерации пароля у пользователя.
    """
    # Запрос длины пароля
    try:
        length = int(input("Введите длину пароля (по умолчанию 12): ") or 12)
    except ValueError:
        print("Неверный ввод, будет использовано значение по умолчанию (12).")
        length = 12

    # Запрос параметров использования различных типов символов
    use_digits = input("Использовать цифры? (y/n, по умолчанию 'y'): ").lower() != "n"
    use_special = input("Использовать спецсимволы? (y/n, по умолчанию 'y'): ").lower() != "n"
    use_upper = input("Использовать заглавные буквы? (y/n, по умолчанию 'y'): ").lower() != "n"
    use_lower = input("Использовать строчные буквы? (y/n, по умолчанию 'y'): ").lower() != "n"

    return length, use_digits, use_special, use_upper, use_lower

if __name__ == "__main__":
    print("Генератор паролей")
    
    # Получение параметров от пользователя
    length, use_digits, use_special, use_upper, use_lower = get_user_input()
    
    # Генерация пароля с указанными параметрами
    password = generate_password(length, use_digits, use_special, use_upper, use_lower)
    print("Сгенерированный пароль:", password)
