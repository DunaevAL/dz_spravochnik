# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


def print_phonebook():
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        print(data.read())

def search_contact(search_term):
    found = False
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if search_term in line:
                print(line)
                found = True
    if not found:
        print("Контакт не найден")

def new_contact(name, middle_name, last_name, phone, comment):
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(f"{name:<15} {middle_name:<15} {last_name:<15} {phone:<15} {comment:<15}\n")

def main():
    while True:
        print("\nМеню:")
        print("1. Показать весь телефонный справочник")
        print("2. Найти контакт по фамилии или номеру телефона")
        print("3. Добавить новый контакт")
        print("4. Выход")

        choice = input("Выберите действие (1/2/3/4): ")

        if choice == '1':
            print_phonebook()
        elif choice == '2':
            search_term = input("Введите фамилию или номер телефона для поиска: ").upper()
            search_contact(search_term)
        elif choice == '3':
            name = input('Введите имя: ').upper()
            middle_name = input('Введите отчество: ').upper()
            last_name = input('Введите фамилию: ').upper()
            phone = input('Введите номер телефона: ')
            comment = input('Введите комментарий: ')
            new_contact(name, middle_name, last_name, phone, comment)
            print("Контакт успешно добавлен в телефонную книгу.")
        elif choice == '4':
            print("Завершение работы программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()







