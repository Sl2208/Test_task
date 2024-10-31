import os
import subprocess

def get_size(item):
    # Получаем размер файлов и директорий
    try:
        # Используем 'du -s' для получения полного размера элементов текущей диретории с учетом кодировки
        size = int(subprocess.check_output(['du', '-s', item]).split()[0].decode('utf-8'))
    except subprocess.CalledProcessError:
        size = 0  # Fallback if 'du' encounters an issue
    return size

def display_sizes():
    # Отображаем размер каждого элемента в текущей директории 
    items_with_size = []

    # Циклический перебор всего набора элементов текущей диретории
    for item in os.listdir('.'):
        if os.path.isdir(item) or os.path.isfile(item):
            # Получаем размеры элементов и формируем их списком
            size = get_size(item)
            items_with_size.append((size, item))

    # добавляем вывод списком элементов с помощью одноразовой функции с сортировкой по убыванию их размера
    items_with_size.sort(reverse=True, key=lambda x: x[0])

    # Создаем отображение в читабельном виде
    for size, item in items_with_size:
        # Используем 'du -sh' для нормального отображения 
        norm_readable_view = subprocess.check_output(['du', '-sh', item]).split()[0].decode('utf-8')
        print(f"{norm_readable_view} - {item}")

# Запускаем по циклу
if __name__ == "__main__":
    display_sizes()
