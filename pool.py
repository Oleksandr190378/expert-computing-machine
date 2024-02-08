from multiprocessing import Pool, current_process, cpu_count
from time import  time


def factorize(n):
    rez = []
    for i in range(1, n//2):
        if n % i == 0:
            rez.append(i)
    rez.append(n)
    print(f"Factorize {n}: {rez}")
    return rez


if __name__ == "__main__":
    input_data = input('Enter list of digits: ')
    data_list1 = input_data.split(',')
    data_list = [int(el) for el in data_list1 ]
    print(f"Count CPU: {cpu_count()}")

    start_time = time()
    with Pool(cpu_count()) as p:
        p.map_async(factorize, data_list, )
        p.close() 
        p.join()  
    print(f'End {current_process().name}')
    end_time1 = time() - start_time
    print(f"Time of pool map async process : {end_time1}")

    start_time3 = time()
    with Pool(cpu_count()) as d:
        d.map(factorize, data_list)
    print(f'End {current_process().name}')
    end_time3 = time() - start_time3
    print(f"Time of  pool map process : {end_time3}")

    start_time2 = time()
    for el in data_list:
        factorize(el)
    print(f'End {current_process().name}')
    end_time2 = time() - start_time2
    print(f"Time of single process : {end_time2}")
    
