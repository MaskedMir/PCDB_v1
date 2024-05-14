from db_handler import psu_db

PSU_PROCENT = 0.10  # Процент от общей стоимости компьютера, выделяемый на блок питания


def search_psu(price_pc):
    price_max = int(price_pc * (PSU_PROCENT + 0.05))
    price_min = int(price_pc * (PSU_PROCENT - 0.05))

    psu_selection = psu_db(price_max, price_min)

    # Проверяем, что есть хотя бы один блок питания для сравнения
    if len(psu_selection) == 0:
        print("Not enough PSUs to compare.")
        return ["Нет комплектующей", 0]
    elif len(psu_selection) < 2:
        return psu_selection[0]

    return compare_psus(psu_selection)


def compare_psus(psu_selection):
    # Сравнение параметров и выбор лучшего блока питания
    best_psu_index = -1
    best_score = float('-inf')

    for i, psu in enumerate(psu_selection):
        score = 0

        # power: чем больше мощность, тем лучше
        power = []
        # lvl: чем выше уровень, тем лучше (например, Gold лучше Bronze)
        lvl = []
        # price: чем меньше, тем лучше
        price = []

        for parameter in psu_selection:
            power.append(parameter[1])
        if psu[1] == max(power):
            score += 3

        for parameter in psu_selection:
            lvl.append(parameter[2])
        if psu[2] == max(lvl):
            score += 2

        for parameter in psu_selection:
            price.append(parameter[3])
        if psu[3] == min(price):
            score += 3

        if score > best_score:
            best_score = score
            best_psu_index = i

    return psu_selection[best_psu_index]
