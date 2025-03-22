print("\033[31m")

import time
import pygame

# Инициализация pygame для работы с музыкой
pygame.mixer.init()

# Загружаем и начинаем воспроизведение музыки
pygame.mixer.music.load("C:\\Users\\andre\PycharmProjects\data_anal_11\python__data_2\song\\benedixhion-toxin-made-with-Voicemod.mp3")  # Укажите путь к вашему музыкальному файлу
pygame.mixer.music.play(-1)  # -1 означает, что музыка будет играть в цикле

# Ваша логика с вычитанием
start_value = 1000
decrement = 7
steps = start_value // decrement  # Количество шагов

total_time = 30  # Время в секундах, на которое должен растянуться процесс
delay = total_time / steps  # Задержка между каждым шагом

current_value = start_value

for _ in range(steps):
    print(f"{current_value} - {decrement} = {current_value - decrement}")
    current_value -= decrement
    time.sleep(delay)  # Задержка, чтобы весь процесс длился 30 секунд

# Останавливаем музыку после завершения
pygame.mixer.music.stop()
