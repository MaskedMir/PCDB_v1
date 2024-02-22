def parametr_select(column, list):
    parametr_list = []
    for el in list:
        parametr_list.append(el[column])
    return parametr_list


from db_handler import ps_db
PS_PROCENT = 0.1
def search_ps(price_pc, pc_list):
    price_max = int(price_pc * (PS_PROCENT + 0.05))
    price_min = int(price_pc * (PS_PROCENT - 0.05))
    power = 200

    ps_sel = ps_db(power, price_max, price_min)

    try:
        if len(ps_sel) > 1:
            result = select_ps(ps_sel)
        else:
            result = ps_sel[0]
    except IndexError:
        result = ["Нет комплектующей", 0]

    return result

def select_ps(ps_selection):
    el_list = [0] * len(ps_selection)
    parametrs = {1: 2, 2: 2}

    for par_num in range(1, 2):
        tp_list = parametr_select(par_num, ps_selection)
        el_list[tp_list.index(max(tp_list))] += parametrs[par_num]

    if el_list.count(max(el_list)) != 1:
        price_list = parametr_select(3, ps_selection)
        el_list[price_list.index(min(price_list))] += 10

    return ps_selection[el_list.index(max(el_list))]