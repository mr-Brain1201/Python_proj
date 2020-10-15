def profile(name, surname, age, citi, email, phone):
    return name, surname, age, citi, email, phone


while True:
    try:
        print(profile(
            name=input('Введите имя: '),
            surname=input('Введите фамилию: '),
            age=str(int(input('Введите год рождения: '))),
            citi=input('Введите ващ город: '),
            email=input('Введите ваш email: '),
            phone=str(int(input('Введите ваш телефон: ')))
        ))
    except ValueError as err:
        print(err)
    else:
        break
