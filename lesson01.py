def div_num(num, den):
    return "На 0 делить нельзя!" if den == 0 else f"Ответ: {round(num / den, 2)}"


print(div_num(int(input("Введите числитель: ")), int(input("Введите знаменатель: "))))
