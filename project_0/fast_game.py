"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np

def fast_predict(num:int=1):
    """Угадываем число по алгоритму

    Args:
        num (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # счетчик попыток
    min_num = 0 # нижняя граница диапазона чисел для рандомного выбора
    max_num = 101 # верхняя граница диапазона чисел для рандомного выбора
    while True:
        count += 1
        predict_number = np.random.randint(min_num, max_num) # предполагаемое число
        if predict_number == num:
            break
        elif predict_number < num:
            min_num = predict_number
        else:
            max_num = predict_number
    return count

def fast_score_game(fast_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов наш алгоритм угадывает число

    Args:
        fast_predict (num): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    score_ls = list(map(fast_predict, random_array))
    score = int(np.mean(score_ls)) 
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

if __name__=='__main__':
    fast_score_game(fast_predict)      