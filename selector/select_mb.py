from select_alg import parametr_select
from db_handler import db_sel

MB_PROCENT = 0.15
def search_gpu(price_pc):  # Отбор из БД CPU
    global power
    price_max = int(price_pc * (MB_PROCENT + 0.05))
    price_min = int(price_pc * (MB_PROCENT - 0.05))

    gpu_selection = db_sel("cpu", price_max, price_min)

    try:
        result = select_mb(gpu_selection)
    except IndexError:
        result = ["Нет комплектующей", 0]

    return result
def select_mb(mb_selection):  # Выбор CPU по параметрам из уже отобранных по цене

    gpu_list = [0] * len(mb_selection)
    parametrs = {1: 2, 2: 1, 3: 2, 4: 1, 5: 2, 6: 0}

    for par_num in range(1, 7):
        tp_list = parametr_select(par_num, mb_selection)
        gpu_list[tp_list.index(max(tp_list))] += parametrs[par_num]

    if gpu_list.count(max(gpu_list)) != 1:
        price_list = parametr_select(7, mb_selection)
        gpu_list[price_list.index(min(price_list))] += 10

    return mb_selection[gpu_list.index(max(gpu_list))]

