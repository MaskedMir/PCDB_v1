from db_handler import mb_db

MB_PROCENT = 0.2


def search_mb(cpu, price_pc):  # Отбор из БД материнской платы

    price_max = int(price_pc * (MB_PROCENT + 0.1))
    price_min = int(price_pc * (MB_PROCENT - 0.1))

    mb_sel = mb_db(cpu, price_max, price_min)

    # Проверяем, что есть хотя бы два графических процессора для сравнения
    if len(mb_sel) == 0:
        print("Not enough GPUs to compare.")
        return ["Нет комплектующей", 0]
    elif len(mb_sel) < 2:
        return mb_sel[0]

    return compare_motherboards(mb_sel)


def compare_motherboards(motherboard_selection):

    # Сравнение параметров и выбор лучшей материнской платы
    best_motherboard_index = -1
    best_score = float('-inf')

    for i, mb in enumerate(motherboard_selection):
        score = 0

        # Параметры для сравнения
        # chipset: может быть специфическим и требует дополнительной логики, если необходимо
        # socket: должен соответствовать сокету CPU
        # ram_type: должен соответствовать типу RAM
        # expansion_slots: чем больше, тем лучше
        expansion_slots = []
        # sata: чем больше портов SATA, тем лучше
        sata = []
        # sata_version: чем выше версия, тем лучше
        sata_version = []
        # m2: чем больше слотов M.2, тем лучше
        m2 = []
        # usb3_2: чем больше портов USB 3.2, тем лучше
        usb3_2 = []
        # usb2_0: чем больше портов USB 2.0, тем лучше
        usb2_0 = []
        # form_factor: ATX лучше, но может зависеть от корпуса
        form_factor = []
        # price: чем меньше, тем лучше
        price = []

        for parameter in motherboard_selection:
            expansion_slots.append(parameter[4])
        if mb[4] == max(expansion_slots):
            score += 2

        for parameter in motherboard_selection:
            sata.append(parameter[5])
        if mb[5] == max(sata):
            score += 1

        for parameter in motherboard_selection:
            sata_version.append(parameter[6])
        if mb[6] == max(sata_version):
            score += 1

        for parameter in motherboard_selection:
            m2.append(parameter[7])
        if mb[7] == max(m2):
            score += 2

        for parameter in motherboard_selection:
            usb3_2.append(parameter[8])
        if mb[8] == max(usb3_2):
            score += 1

        for parameter in motherboard_selection:
            usb2_0.append(parameter[9])
        if mb[9] == max(usb2_0):
            score += 1

        for parameter in motherboard_selection:
            form_factor.append(parameter[10])
        if mb[10] == "ATX":
            score += 2
        elif mb[10] == "MicroATX":
            score += 1

        for parameter in motherboard_selection:
            price.append(parameter[11])
        if mb[11] == min(price):
            score += 3

        if score > best_score:
            best_score = score
            best_motherboard_index = i

    return motherboard_selection[best_motherboard_index]
