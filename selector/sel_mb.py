def parametr_select(column, list):
    parametr_list = []
    for el in list:
        parametr_list.append(el[column])
    return parametr_list


from db_handler import mb_db

MB_PROCENT = 0.15


def search_mb(cpu, price_pc):  # Отбор из БД материнской платы

    price_max = int(price_pc * (MB_PROCENT + 0.05))
    price_min = int(price_pc * (MB_PROCENT - 0.05))

    mb_sel = mb_db(cpu, price_max, price_min)

    try:
        if len(mb_sel) > 1:
            result = select_mb(mb_sel)
        else:
            result = mb_sel[0]
    except IndexError:
        result = ["Нет комплектующей", 0]

    return result


def select_mb(mb_selection):
    gpu_list = [0] * len(mb_selection)
    parametrs = {1: 2, 2: 2, 3: 3, 4: 2, 5: 2, 6: 1,
                 7: 0, 8: 2, 9: 1, 10: 2}

    for par_num in range(1, 11):
        tp_list = parametr_select(par_num, mb_selection)
        gpu_list[tp_list.index(max(tp_list))] += parametrs[par_num]

    if gpu_list.count(max(gpu_list)) != 1:
        price_list = parametr_select(11, mb_selection)
        gpu_list[price_list.index(min(price_list))] += 10

    return mb_selection[gpu_list.index(max(gpu_list))]
