"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np

def fast_random_predict(n_number:int=1):
    """Угадываем число по алгоритму

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_number = 0
    max_number = 101
    while True:
        count += 1
        predict_number = (max_number - min_number)//2
        if predict_number == n_number:
            break
        elif predict_number < n_number:
            max_number == predict_number
        else:
            min_number == predict_number
    return count

def fast_score_game(fast_random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов наш алгоритм угадывает число

    Args:
        fast_random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    score_ls = list(map(fast_random_predict, random_array))
    score = int(np.mean(score_ls)) 
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

if __name__=='__main__':
    fast_score_game(fast_random_predict)      