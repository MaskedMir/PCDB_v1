from db_handler import db_sel

GPU_PROCENT = 0.40  # Процент от общей стоимости компьютера, выделяемый на хранилище

# Функция для поиска SSD/HDD
def search_gpu(price_pc):
    price_max = int(price_pc * (GPU_PROCENT + 0.15))
    price_min = int(price_pc * (GPU_PROCENT - 0.15))

    gpu_selection = db_sel("gpu", price_max, price_min)

    # Проверяем, что есть хотя бы один накопитель для сравнения
    if len(gpu_selection) == 0:
        print("Not enough storages to compare.")
        return ["Нет комплектующей", 0]
    elif len(gpu_selection) < 2:
        return gpu_selection[0]

    return compare_gpus(gpu_selection)

# Функция для сравнения и выбора лучшего SSD/HDD
def compare_gpus(gpu_selection):
    best_gpu_index = -1
    best_score = float('-inf')

    for i, gpu in enumerate(gpu_selection):
        score = 0

        # chip: сравнение по типу чипа может быть специфическим и требует дополнительной логики, если необходимо
        # memory_type: чем выше тип памяти (DDR6 лучше DDR5), тем лучше
        memory_type = []
        # memory: чем больше, тем лучше
        memory = []
        # bitrate: чем больше, тем лучше
        bitrate = []
        # connection_interface: может быть специфическим для совместимости
        # power: чем меньше, тем лучше
        power = []
        # price: чем меньше, тем лучше
        price = []

        for parameter in gpu_selection:
            memory_type.append(parameter[2])
        if gpu[2] == max(memory_type):
            score += 2

        for parameter in gpu_selection:
            memory.append(parameter[3])
        if gpu[3] == max(memory):
            score += 3

        for parameter in gpu_selection:
            bitrate.append(parameter[4])
        if gpu[4] == max(bitrate):
            score += 2

        for parameter in gpu_selection:
            power.append(parameter[6])
        if gpu[6] == min(power):
            score += 2

        for parameter in gpu_selection:
            price.append(parameter[7])
        if gpu[7] == min(price):
            score += 3

        if score > best_score:
            best_score = score
            best_gpu_index = i


    return gpu_selection[best_gpu_index]


