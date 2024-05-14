from db_handler import db_sel

RAM_PROCENT = 0.15  # Процент от общей стоимости компьютера, выделяемый на оперативную память

# Функция для поиска RAM
def search_ram(price_pc):
    price_max = int(price_pc * (RAM_PROCENT + 0.05))
    price_min = int(price_pc * (RAM_PROCENT - 0.05))

    ram_selection = db_sel("ram", price_max, price_min)

    # Проверяем, что есть хотя бы два модуля оперативной памяти для сравнения
    if len(ram_selection) == 0:
        print("Not enough RAMs to compare.")
        return ["Нет комплектующей", 0]
    elif len(ram_selection) < 2:
        return ram_selection[0]

    return compare_rams(ram_selection)

def compare_rams(ram_selection):
    # Сравнение параметров и выбор лучшего RAM
    best_ram_index = -1
    best_score = float('-inf')

    for i, ram in enumerate(ram_selection):
        score = 0

        # type: тип памяти, например DDR4 или DDR5
        type_ = []
        # memory: объем памяти, чем больше, тем лучше
        memory = []
        # power: потребляемая мощность, чем меньше, тем лучше
        power = []
        # price: цена, чем меньше, тем лучше
        price = []

        for parameter in ram_selection:
            type_.append(parameter[1])
        if ram[1] == max(type_):
            score += 2

        for parameter in ram_selection:
            memory.append(parameter[2])
        if ram[2] == max(memory):
            score += 3

        for parameter in ram_selection:
            power.append(parameter[3])
        if ram[3] == min(power):
            score += 2

        for parameter in ram_selection:
            price.append(parameter[4])
        if ram[4] == min(price):
            score += 3

        if score > best_score:
            best_score = score
            best_ram_index = i

    return ram_selection[best_ram_index]

