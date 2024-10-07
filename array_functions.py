import pytest
def find_max_min(arr, max=True):
    if len(arr) == 0:
        return None
    result = arr[0]  # Инициализируем результат первым элементом массива

    if max:
        for num in arr:
            if num > result:
                result = num
    else:
        for num in arr:
            if num < result:
                result = num

    return result


def sort_array(arr):
    # Реализация пузырьковой сортировки
    n = len(arr)
    for i in range(n):
        for j in range(1, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def find_median(arr):
    if not arr:
        return None

    count = 0
    for _ in arr:
        count += 1

    total_sum = 0
    for num in arr:
        total_sum += num

    return total_sum / count

def reverse_array(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr


def offset_elements(arr, offset):
    # Если массив пустой, возвращаем его же
    if not arr:
        return arr

    # Избегаем смещений больше длины массива
    offset = offset % len(arr)

    # Создаем новый массив для результата
    result = []

    # Добавляем элементы от позиции смещения до конца массива
    for i in range(len(arr) - offset, len(arr)):
        result.append(arr[i])

    # Добавляем оставшиеся элементы с начала до позиции смещения
    for i in range(len(arr) - offset):
        result.append(arr[i])

    return result


def menu():
    array = input('Введите элементы массива через пробел\n').split()
    print('Напишите:',' max, если хотите найти максимум\n',
                    ' min, если хотите найти минимум\n',
                    ' sort, если хотите отсортировать массив\n',
                     'med, если хотите найти медиану\n',
                    'rev, если хотите поменять порядок элементов на обратный\n')
    choice = input()
    match choice:
        case "max":
            print(f"Максимум: {find_max_min(array, max=True)}")
        case "min":
            print(f"Минимум: {find_max_min(array, max=False)}")
        case "sort":
            print(f"Отсортированный массив: {sort_array(array)}")
        case "med":
            print(f"Медиана: {find_median(array)}")
        case "rev":
            print(f"Массив в обратном порядке: {reverse_array(array)}")
        case "offset":
            offset = int(input("Введите количество позиций для смещения: "))
            print(f"Массив после смещения: {offset_elements(array, offset)}")
        case _:
            print("Неверный ввод")

import pytest

def test_find_max_min():
    # Тест для нахождения максимума
    assert find_max_min([1, 2, 3, 4, 5]) == 5
    # Тест для нахождения минимума
    assert find_max_min([1, 2, 3, 4, 5], max=False) == 1
    # Тест для пустого массива
    assert find_max_min([]) == None

def test_sort_array():
    # Тест для сортировки массива
    assert sort_array([5, 3, 2, 4, 1]) == [1, 2, 3, 4, 5]
    # Тест для уже отсортированного массива
    assert sort_array([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_find_median():
    # Тест для нахождения медианы
    assert find_median([1, 2, 3, 4, 5]) == 3
    # Тест для пустого массива
    assert find_median([]) == None

def test_reverse_array():
    # Тест для разворота массива
    assert reverse_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    # Тест для пустого массива
    assert reverse_array([]) == []

def test_offset_elements():
    # Тест для смещения элементов на 2 позиции
    assert offset_elements([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    # Тест для смещения элементов на длину массива
    assert offset_elements([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
    # Тест для пустого массива
    assert offset_elements([], 2) == []

if __name__ == "__main__":
    pytest.main()






