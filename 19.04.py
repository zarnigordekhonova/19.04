# 1 - masala

from threading import Thread
from time import time, sleep
from multiprocessing import Process, Pool
from faker import Faker
import random

def greeting_1():
    print("Salom Python")
    n = 10**6
    while n > 0:
        n -= 1
    sleep(1)
    print('Hayr Python')


def greeting_2():
    print("Hello Python")
    n = 10**6
    while n > 0:
        n -= 1
    sleep(1)
    print('Bye Python')


def square_root():
    for i in range(1, 4+1):
        n = 10 ** 6
        while n > 0:
            n -= 1
        sleep(2)
        print(f"{i}, Kvadrat: {i ** 2}")


def multiply():
    for i in range(1, 4+1):
        n = 10 ** 6
        while n > 0:
            n -= 1
        sleep(2)
        print(f"{i}, Ko'paytma: {i * 2}")


def thread_timer():
    start = time()
    t1 = Thread(target=greeting_1)
    t2 = Thread(target=greeting_2)
    t3 = Thread(target=square_root)
    t4 = Thread(target=multiply)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print('Thread timer: ', time() - start)
    return time() - start



def simple_timer():
    start = time()
    greeting_1()
    greeting_2()
    square_root()
    multiply()
    print('Simple timer:', time() - start)
    return time() - start



t = thread_timer()
s = simple_timer()
difference = s - t
print('Thread_timer va simple_timer o\'rtasidagi farq ', difference, 'ga teng.')


# 2 - masala
def even_numbers(i):
    if i % 2 == 0:
        # print(i)
        sleep(2)


if __name__ == "__main__":
    start = time()
    with Pool(4) as p:
        l = list(range(1, 21))
        p.map(even_numbers, l)
        # print('Vaqt: ', time() - start)



# 3 - masala
def names_with_A(i):
    if i.startswith('A'):
        print(i)
        sleep(2)


if __name__ == "__main__":
    start = time()
    r = []
    f = Faker()
    with open("names_1.txt", 'a') as file:
        for i in range(100):
            file.write(f'{f.name()}\n')
    with open('names_1.txt', 'r') as names_file:
        for i in names_file:
            r.append(i)

    with Pool(3) as p:
        p.map(names_with_A, r)
    print('Vaqt: ', time() - start)


# 4 - masala
def true_false(i):
    if len(i) > 5:
        print(f'{i} --> False')
    else:
        print(f'{i} --> True')
    sleep(5)

if __name__ == "__main__":
    start = time()
    with Pool(3) as p:
        n = names = ["Emma", "Liam", "Sophia", "Albert", "Olivia", "Aiden", "Isabella", "Lucas", "Mia", "Ethan",
                     "Ava", "James", "Lily", "Alexander", "Emily", "Charlotte", "Benjamin", "Amelia", "Jack", "Zoe"]
        p.map(true_false, n)
    print('Vaqt: ', time() - start)



# 5-masala
def tub_sonlar(i):
        c = 0
        for k in range(1, i):
            if i % k == 0:
                c += 1
        if c == 1:
            print(f'{i} --> Tub')
        else:
            print(f'{i} --> Murakkab')
        sleep(2)

if __name__ == "__main__":
    start = time()
    l = list(range(2, 23))

    with Pool(4) as p:
        p.map(tub_sonlar, l)
    print('Vaqt: ', time() - start)


# 6-masala
def sorted_list():
    start = time()
    result = []
    for i in range(20):
        r = random.randint(1, 100)
        result.append(r)
    s = sorted(result)
    with open('numbers.txt', 'a') as file:
        for i in s:
            file.write(f'{str(i)}\n')
sorted_list()

# 7 - masala
def remove_duplicate(s):
    result = []
    r = ""
    for i in s:
        if i != r:
            result.append(i)
            r = i
    output = "".join(result)

    if output:
        print(output)
    else:
        print("Empty String")

remove_duplicate('aabbccdd')











