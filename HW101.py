import time
import threading
from pprint import pprint
import io

def write_words(word_count, file_name):
    start_time = time.time()
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count + 1):
            file.write(f'Какое-то слово №{i}\n')
            time.sleep(0.1)
    finish_time = time.time()
    print(f'Завершилась запись в файл {file_name}, время записи: {round((finish_time - start_time), 2)}')


res = write_words(10, 'example1.txt')
res = write_words(30, 'example2.txt')
res = write_words(200, 'example3.txt')
res = write_words(100, 'example4.txt')
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()