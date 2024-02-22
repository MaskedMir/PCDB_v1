def parametr_select(column, list):
    parametr_list = []
    for el in list:
        parametr_list.append(el[column])
    return parametr_list


from db_handler import db_sel

CPU_PROCENT = 0.25


def search_cpu(price_pc):
    price_max = int(price_pc * (CPU_PROCENT + 0.05))
    price_min = int(price_pc * (CPU_PROCENT - 0.05))

    cpu_selection = db_sel("cpu", price_max, price_min)

    try:
        result = select_cpu(cpu_selection)
    except IndexError:
        result = ["Нет комплектующей", 0]

    return result


def select_cpu(cpu_selection):
    el_list = [0] * len(cpu_selection)
    parametrs = {1: 2, 2: 2, 3: 3, 4: 2, 5: 2, 6: 1,
                 7: 0, 8: 2, 9: 1, 10: 2}

    for par_num in range(1, 11):
        tp_list = parametr_select(par_num, cpu_selection)
        el_list[tp_list.index(max(tp_list))] += parametrs[par_num]

    if el_list.count(max(el_list)) != 1:
        price_list = parametr_select(12, cpu_selection)
        el_list[price_list.index(min(price_list))] += 10

    return cpu_selection[el_list.index(max(el_list))]
