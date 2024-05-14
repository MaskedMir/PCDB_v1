from db_handler import db_sel

CPU_PROCENT = 0.25


# Предполагая, что функция db_sel правильно реализована и возвращает список CPU-процессоров
def search_cpu(price_pc):
    price_max = int(price_pc * (CPU_PROCENT + 0.15))
    price_min = int(price_pc * (CPU_PROCENT - 0.15))

    cpu_selection = db_sel("cpu", price_max, price_min)

    # Проверяем, что есть хотя бы два процессора для сравнения
    if len(cpu_selection) == 0:
        print("Not enough GPUs to compare.")
        return ["Нет комплектующей", 0]
    elif len(cpu_selection) < 2:
        return cpu_selection[0]

    return compare_cpus(cpu_selection)


def compare_cpus(cpu_selection):
    # Сравнение параметров и выбор лучшего CPU
    best_cpu_index = -1
    best_score = float('-inf')

    for i, cpu in enumerate(cpu_selection):
        score = 0

        # technical_process: чем меньше, тем лучше
        technical_process = []
        # cores: чем больше, тем лучше
        cores = []
        # frequency: чем больше, тем лучше
        frequency = []
        # cache: чем больше, тем лучше
        cache = []
        # tdp: чем меньше, тем лучше
        tdp = []
        # ram_frequency: чем больше, тем лучше
        ram_frequency = []
        # price: чем меньше, тем лучше
        price = []
        # ram_canale: чем больше, тем лучше
        ram_canale = []

        for parameter in cpu_selection:
            technical_process.append(parameter[1])
        if cpu[1] == min(technical_process):
            score += 2

        for parameter in cpu_selection:
            cores.append(parameter[1])
        if cpu[3] == max(cores):
            score += 3

        for parameter in cpu_selection:
            frequency.append(parameter[1])
        if cpu[4] == max(frequency):
            score += 3

        for parameter in cpu_selection:
            cache.append(parameter[1])
        if cpu[5] == max(cache):
            score += 1

        for parameter in cpu_selection:
            tdp.append(parameter[1])
        if cpu[6] == min(tdp):
            score += 2

        for parameter in cpu_selection:
            ram_frequency.append(parameter[1])
        if cpu[11] == max(ram_frequency):
            score += 1

        for parameter in cpu_selection:
            price.append(parameter[1])
        if cpu[12] == min(price):
            score += 3

        # Проверка наличия видео ядра
        if cpu[7]:
            score += 1

        # Учитываем количество каналов RAM
        for parameter in cpu_selection:
            ram_canale.append(parameter[1])
        if cpu[10] == max(ram_canale):
            score += 1

        if score > best_score:
            best_score = score
            best_cpu_index = i

    return cpu_selection[best_cpu_index]
