def parametr_select(column, list):
    parametr_list = []
    for el in list:
        parametr_list.append(el[column])
    return parametr_list


from db_handler import db_sel

RAM_PROCENT = 0.1


def search_ram(price_pc):  # Отбор из БД RAM
    price_max = int(price_pc * (RAM_PROCENT + 0.05))
    price_min = int(price_pc * (RAM_PROCENT - 0.05))

    ram_selection = db_sel("ram", price_max, price_min)

    try:
        if len(ram_selection) > 1:
            result = select_ram(ram_selection)
        else:
            result = ram_selection[0]
    except IndexError:
        result = ["Нет комплектующей", 0]
    return result


def select_ram(ram_selection):
    el_list = [0] * len(ram_selection)
    parametrs = {1: 2, 2: 2, 3: 3, 4: 2}

    for par_num in range(1, 6):
        tp_list = parametr_select(par_num, ram_selection)
        el_list[tp_list.index(max(tp_list))] += parametrs[par_num]

    if el_list.count(max(el_list)) != 1:
        price_list = parametr_select(5, ram_selection)
        el_list[price_list.index(min(price_list))] += 10

    return ram_selection[el_list.index(max(el_list))]
