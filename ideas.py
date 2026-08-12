import datetime

# Відповідь на message від користувача на повідомлення start

mes = input("Привіт користувач! Будемо починати працю(напишіть ʼstartʼ) ")

def give_date(start_date, end_date, days_input):
    list_weekdays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Нд"]
    current_date = start_date
    int_list_days = []

    for day in days_input:
        if day in list_weekdays:
            int_list_days.append(list_weekdays.index(day))

    result = []
    count = 0
    while current_date <= end_date:
        if current_date.weekday() in int_list_days:
            count += 1
            date = datetime.datetime.strftime(current_date, "%d/%m") + "(" + str(list_weekdays[current_date.weekday()]) + ")"

            result.append(date)

        current_date = current_date + datetime.timedelta(days=1)

    return result

def list_dates(start, end, choice):
    #Перетворюємо вхідні дані на зрозумілу мову

    start_date = datetime.datetime.strptime(start, "%d/%m/%y")
    end_date = datetime.datetime.strptime(end, "%d/%m/%y")

    if choice == 1:
        days_input = ["Ср", "Нд"]
        result = give_date(start_date, end_date, days_input)

        return [result, days_input]

    elif choice == 2:
        days_input = ["Чт", "Пт", "Нд"]
        result = give_date(start_date, end_date, days_input)

        return [result, days_input]

    elif choice == 3:
        days_input = input("Впишіть дні тижня, які вам потрібні('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд'): ").split()
        result = give_date(start_date, end_date, days_input)

        return [result, days_input]

    return None



if mes == "start":
    print()
    print("Праця почалась!")
    while True:
        print("Оберіть задачу, яку потрібно виконати з панелі ʼМЕНЮʼ:")
        print("\n 'МЕНЮ':"
              "\n 1)Створення списку дат по днях"
              "\n 2)Створення повідомлення для обʼяв"
              "\n 0)Закінчити роботу")
        choice = int(input("Зробить свій вибір(потрібна цифра): "))

        if choice == 1:
            print("Оберіть, який саме список вам потрібен:")
            print("\n1)Для лідерів прославлення"
                            "\n2)Для своєї групи прославлення"
                            "\n3)Свій список")
            choice =  int(input("\nЗробіть свій вибіл(1-3): "))

            start = input("\nВпишіть початкову дату(dd/mm/yy): ")
            end = input("Впишіть кінцеву дату(dd/mm/yy): ")

            dates = list_dates(start, end, choice)

            print()
            count = 1
            for date in dates[0]:
                print(date)
                if count % len(dates[1]) == 0:
                    print()
                    print("New week: ")
                count += 1

        elif choice == 2:
            None

        elif choice == 0:
            print()
            print("Роботу закінчено")
            break
else:
    print()
    print("Праця не почалась(")