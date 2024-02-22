from selector.sel_cpu import search_cpu
from selector.sel_mb import search_mb
from selector.sel_gpu import search_gpu
from selector.sel_ram import search_ram
from selector.sel_psd import search_psd
from selector.sel_ps import search_ps
from db_handler import db_pc_list


def pc_selection(price_pc):  # Сборка данных в один список (конечный список комплектующих для ПК)
    cpu = search_cpu(price_pc)
    motherboard = search_mb(cpu, price_pc)
    gpu = search_gpu(price_pc)
    ram = search_ram(price_pc)
    psd = search_psd(price_pc)

    pc_list = [cpu, motherboard, gpu, ram, psd]
    ps = search_ps(price_pc, pc_list)
    pc_list.append(ps)

    db_pc_list(pc_list)
    return pc_list
