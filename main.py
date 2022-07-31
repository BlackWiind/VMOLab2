#Теория игр

from random import random

prise_a = 0
a1_sum = 0
b1_sum = 0


def game(l_strategy_a: 1, l_strategy_b: 1) -> int:
    if l_strategy_a == 1 and l_strategy_b == 1:
        return 6
    elif l_strategy_a == 1 and l_strategy_b == 2:
        return 14
    elif l_strategy_a == 2 and l_strategy_b == 1:
        return 21
    else:
        return 10


print("№ партии | Случайное А | Стратегия А | Случайное В | Стратегия В | Выйгрыш A | Накопленый выйгрыш А | "
      "Средний выйгрыш А")
for iteration in range(1, 101):
    random_a = random()
    if random_a < 0.58:
        strategy_a = 1
        a1_sum += 1
    else:
        strategy_a = 2
    random_b = random()
    if random_b < 0.21:
        strategy_b = 1
        b1_sum += 1
    else:
        strategy_b = 2
    prise_a += game(strategy_a, strategy_b)
    print(
        f"{iteration}.\t\t\t{round(random_a, 3)} \t\t\tA{strategy_a} \t\t\t{round(random_b, 3)} \t\t\tB{strategy_b} "
        f"\t\t\t {game(strategy_a, strategy_b)}\t\t\t\t{prise_a}\t\t\t\t\t{round(prise_a / iteration, 3)}")
print(f"Стратегия А1 использована {a1_sum} раза. Стратегия В1 использовна {b1_sum} раза.")