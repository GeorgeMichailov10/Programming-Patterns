import concurrent.futures
import threading
import math
import queue

# Pascals triangle demo

# 0 - indexed
def generate_row(row_num):
    values = []
    for index in range(row_num + 1):
        values.append(math.comb(row_num, index))
    return values

def generate_pascal_triangle_cf(row_num):
    # Thead pool executor manages spawning threads for us and kept in futures.
    with concurrent.futures.ThreadPoolExecutor(max_workers=row_num) as executor:
        futures = [executor.submit(generate_row, row) for row in range(row_num)]

        # Catch the future objects upon completion
        results = concurrent.futures.as_completed(futures)

        # Sort the results based on length from shortest to longest
        triangle = sorted(results, key=lambda x: len(x.result()))
        for row in triangle:
            print(row.result())

def generate_row_threading(row_num, result):
    values = []
    for index in range(row_num + 1):
        values.append(math.comb(row_num, index))
    result.append(values)

def generate_pascal_triangle_th(row_num):
    threads = []
    # Create shared list for threads to dump their results into
    result = []

    # Spawn a thread manually for each row and save it threads list for catching
    for row in range(row_num):
        thread = threading.Thread(target=generate_row_threading, args=(row, result))
        threads.append(thread)
        thread.start()

    # Catch each thread one by one
    for thread in threads:
        thread.join()

    # Sort and print triangle.
    pascal = sorted(result, key=lambda x: len(x))
    for row in pascal:
        print(row)
            

#generate_pascal_triangle_cf(5)
generate_pascal_triangle_th(5)