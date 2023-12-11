""" 
● Контекст
Корреляция - статистическая мера, используемая для оценки
связи между двумя случайными величинами.
● Ваша задача
Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать
функциональную, т.к. в этом примере она значительно
упростит вам жизнь.
"""

def pearson_correlation(x_list, y_list):

    avg_x = sum(x_list) / len(x_list)
    avg_y = sum(y_list) / len(y_list)

    def find_numerator(a, b):
        return (a - avg_x) * (b - avg_y)

    def find_std1(a):
        return (a - avg_x) ** 2

    def find_std2(b):
        return (b - avg_y) ** 2

    return round(sum(map(find_numerator, x_list, y_list)) / (sum(map(find_std1, x_list)) *
                                                   sum(map(find_std2,
                                                           y_list))) ** 0.5, 3)

list1 = [2, 4, 6, 8]
list2 = [3, 5, 7, 10]

pearson_coefficient = pearson_correlation(list1, list2)

print(f'Коэффицент корелляции Пирсона для списков {list1} и {list2} равен: {pearson_coefficient}')