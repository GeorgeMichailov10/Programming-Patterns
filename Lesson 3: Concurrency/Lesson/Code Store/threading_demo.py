# Pascal's triangle example

import concurrent.futures
import math

# 0 - indexed
def generate_row(row_num):
    values = []
    for index in range(row_num + 1):
        values.append(math.comb(row_num, index))
    return values

def generate_pascal_traingle(row_num):
    with concurrent.futures.ThreadPoolExecutor(max_workers=row_num) as executor:
        futures = [executor.submit(generate_row, i) for i in range(row_num)]

        for future in concurrent.futures.as_completed(futures):
            print(future.result())

generate_pascal_traingle(5)