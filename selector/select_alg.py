from select_cpu import search_mb
from select_gpu import search_gpu
from db_handler import db_pc_list

def parametr_select(column, list):
    parametr_list = []
    for el in list:
        parametr_list.append(el[column])
    return parametr_list


def pc_selection(price_pc):  # Сборка данных в один список (конечный список комплектующих для ПК)
    cpu = search_mb(price_pc)
    # motherboard = db_search.search_motherboard(cpu, price_pc)
    gpu = search_gpu(price_pc)
    # ram = db_search.search_ram(price_pc)
    # psd = db_search.search_psd(price_pc)
    # ps = db_search.search_ps(price_pc)

    pc_list = [cpu]
    db_pc_list(pc_list)
    return pc_list

