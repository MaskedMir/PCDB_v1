from db_handler import db_sel

PSD_PROCENT = 0.15


# Предполагая, что функция db_sel правильно реализована и возвращает список GPU
def search_psd(price_pc):
    price_max = int(price_pc * (PSD_PROCENT + 0.05))
    price_min = int(price_pc * (PSD_PROCENT - 0.05))

    psd_selection = db_sel("psd", price_max, price_min)

    # Проверяем, что есть хотя бы два графических процессора для сравнения
    if len(psd_selection) == 0:
        print("Not enough GPUs to compare.")
        return ["Нет комплектующей", 0]
    elif len(psd_selection) < 2:
        return psd_selection[0]

    return compare_gpus(psd_selection)


def compare_gpus(psd_selection):
    # Сравнение параметров и выбор лучшего GPU
    best_psd_index = -1
    best_score = float('-inf')

    for i, psd in enumerate(psd_selection):
        score = 0

        # capacity: чем больше объем памяти, тем лучше
        capacity = []
        # price: чем меньше, тем лучше
        price = []

        for parameter in psd_selection:
            capacity.append(parameter[2])
        if psd[2] == max(capacity):
            score += 2

        for parameter in psd_selection:
            price.append(parameter[5])
        if psd[5] == min(price):
            score += 3

        if psd[1] == "NVMe SSD":
            score += 5
        elif psd[1] == "SSD":
            score += 3
        elif psd[1] == "HDD":
            score += 1

        if score > best_score:
            best_score = score
            best_psd_index = i

    return psd_selection[best_psd_index]
