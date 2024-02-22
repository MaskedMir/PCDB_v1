def parametr_select(column, list):
    parametr_list = []
    for el in list:
        parametr_list.append(el[column])
    return parametr_list


from db_handler import db_sel

PSD_PROCENT = 0.1


def search_psd(price_pc):  # Отбор из БД PSD
    psd_price_max = int(price_pc * (PSD_PROCENT + 0.05))
    psd_price_min = int(price_pc * (PSD_PROCENT - 0.05))

    psd_selection = db_sel("psd", psd_price_max, psd_price_min)

    try:
        if len(psd_selection) > 1:
            result = select_psd(psd_selection)
        else:
            result = psd_selection[0]
    except IndexError:
        result = ["Нет комплектующей", 0]

    return result


def select_psd(psd_selection):
    el_list = [0] * len(psd_selection)
    parametrs = {1: 2, 2: 2, 3: 3}

    for par_num in range(1, 11):
        tp_list = parametr_select(par_num, psd_selection)
        el_list[tp_list.index(max(tp_list))] += parametrs[par_num]

    if el_list.count(max(el_list)) != 1:
        price_list = parametr_select(4, psd_selection)
        el_list[price_list.index(min(price_list))] += 10

    return psd_selection[el_list.index(max(el_list))]
