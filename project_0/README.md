# Проект: Угадай число

## Оглавление
[1.Описание проекта](https://github.com/TattaS/sf_data_science/blob/main/project_0/README.md#Описание-проекта)  
[2.Какой кейс решаем](https://github.com/TattaS/sf_data_science/blob/main/project_0/README.md#Какой-кейс-решаем?)  
[3.Краткая информация о данных](https://github.com/TattaS/sf_data_science/blob/main/project_0/README.md#Краткая-информация-о-данных)  
[4.Этапы работы над проектом](https://github.com/TattaS/sf_data_science/blob/main/project_0/README.md#Этапы-работы-над-проектом)  
[5.Результаты](https://github.com/TattaS/sf_data_science/blob/main/project_0/README.md#Результаты)  
[6.Выводы](https://github.com/TattaS/sf_data_science/blob/main/project_0/README.md#Выводы)

### Описание проекта
Угадать загаданное компьютером число за минимальное количество попыток.

:arrow_up: [к оглавлению](https://github.com/TattaS/sf_data_science/blob/main/project_0/README.md#Оглавление)

### Какой кейс решаем?
Нужно написать программу, которая угадывает число за минимальное число попыток.

**Условия соревнования:**
- Компьютер загадывает целое число от 0 до 100б и нам его нужно угадать. Под "угадать" подразумевается "написать программу, которая угадывает число".
- Алгоритм угадывает информацию о том, ольше ли случайное число или меньше нжуного нам.

**Метрика качества**  
Результат оценивается по среднему количеству попыток при 1000 повторений.

**Что практикуем**  
Учимся писать хороший код на Python

:arrow_up: [к оглавлению](https://github.com/TattaS/sf_data_science/blob/main/project_0/README.md#Оглавление)

### Краткая информация о данных  
...

:arrow_up: [к оглавлению](https://github.com/TattaS/sf_data_science/blob/main/project_0/README.md#Оглавление)

### Этапы работы над проектом  
1. Написали код, который предлагает пользователю угадать загаданное компьютером случайное число. (https://github.com/TattaS/sf_data_science/blob/main/project_0/game.py)  
2. Написали код, который вычисляет среднее количество попыток угадать число методом случайного подбора. (https://github.com/TattaS/sf_data_science/blob/main/project_0/game_v2.py)
3. Написала код, который вычисляет среднее количество попыток угадать число по алгоритму. (https://github.com/TattaS/sf_data_science/blob/main/project_0/fast_game.py)

:arrow_up:[к оглавлению](https://github.com/TattaS/sf_data_science/blob/main/project_0/README.md#Оглавление)

### Результат
При случайном подборе компьютер угадывает число в среднем за 101 попытку ( вычислено среднее за 1000 повторений кода )
По алгоритму компьютер угадвает число в среднем за 8 попыток (вычислено среднее за 1000 повторений кода)
(https://github.com/TattaS/sf_data_science/blob/main/project_0/game.ipynb)

:arrow_up: [к оглавлению](https://github.com/TattaS/sf_data_science/blob/main/project_0/README.md#Оглавление)

### Выводы
Использовать алгоритм при угадывании числа значительно выгоднее, чем метод случайного подбора

:arrow_up: [к оглавлению](https://github.com/TattaS/sf_data_science/blob/main/project_0/README.md#Оглавление)

