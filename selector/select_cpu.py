from select_alg import parametr_select
from db_handler import mb_db

CPU_PROCENT = 0.25
def search_mb(price_pc):  # Отбор из БД CPU
    global power
    price_max = int(price_pc * (CPU_PROCENT + 0.05))
    price_min = int(price_pc * (CPU_PROCENT - 0.05))

    mb_selection = mb_db(price_max, price_min)

    try:
        result = select_mb(mb_selection)
    except IndexError:
        result = ["Нет комплектующей", 0]

    return result
def select_mb(mb_selection):  # Выбор CPU по параметрам из уже отобранных по цене

    mb_list = [0] * len(mb_selection)
    parametrs = {1: 2, 2: 2, 3: 3, 4: 2, 5: 2, 6: 1,
                 7: 0, 8: 2, 9: 1, 10: 2}

    for par_num in range(1, 11):
        tp_list = parametr_select(par_num, mb_selection)
        mb_list[tp_list.index(max(tp_list))] += parametrs[par_num]

    if mb_list.count(max(mb_list)) != 1:
        price_list = parametr_select(12, mb_selection)
        mb_list[price_list.index(min(price_list))] += 10

    return mb_selection[mb_list.index(max(mb_list))]

