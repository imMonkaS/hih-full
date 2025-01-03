# Hack-in-home-Stankin-Backend

## Навигация по проекту:
...

## Проблема: нужно автоматизировать процесс покраски объекта


## Преимущества решения:
1. Удобный интерфейс для взаимодействия
2. Интуитивно понятный функционал
3. Обученная модель yolo11n-seg, которая выполняет сегментацию элементов автомобиля (можно переобучить для других объектов, например для распознавания объектов на ядерном реакторе)
4. Хороший алгоритм для расчета цены (провели исследование о механике расчета стоимости покраски)
5. Проработанная архитектура web-сервиса (чистая архитектура, паттерн репозитории и сервисы, взаимодействие back и фронт через)
6. Возможность интеграции системы с внешними системами через API
7. Отрисовка 3D модели для легкого визуального взаимодействия с системой (в нашем решении ваш глаз не устанет от кучи таблиц и цифр)

## Основной функционал системы:
1. Отправка фото автомобиля с фронта на бэк
2. Выделение имеющихся на фото областей
3. Передача фронту данных об найденных областях и доп. параметрах (массив найденных элементов)
4. Получение ответа от бэка, формирование кнопок на базовой 3д модели (кнопки дают возможность выбирать элементы которые мы хотим покрасить)
5. Далее пользователь выбирает элементы, они добавляются в формулу при расчете окончательной суммы
6. После выбора элементов и указания параметров, на фронте считается сумма необходимая для покраски

## Глобальные фичи:
1. Обученная модель yolo11n-seg (можно переобучить для других объектов, например для распознавания объектов на ядерном реакторе)
2. 3D модель для выбора элементов для покраски
3. Взаимодействие через API
