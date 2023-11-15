tickets = int(input("Введите количество билетов: "))
total_cost = 0
for i in range(1, tickets+1):
 age = int(input(f"Введите возраст участника по {i} билету: "))
 if age < 18:
    print("Стоимость билета: 0 руб.")
 elif 18 <= age < 25:
    total_cost += 990
    print("Стоимость билета: 990 руб.")
 else:
    total_cost += 1390
    print("Стоимость билета: 1390 руб.")
if tickets > 3:
    total_cost = total_cost - (total_cost/100*10)
    print("Вы зарегистрировали больше 3х человек. Ваша скидка 10%.")
    print(f"Сумма к оплате с учетом скидки: {total_cost} руб.")
else:
 print(f"Сумма к оплате: {total_cost} руб.")