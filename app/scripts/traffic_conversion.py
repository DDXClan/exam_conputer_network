def traffic_conversion(traffic_bits=None, network_speed=None, disk_capacity=None):
    if traffic_bits is not None:
        megabits = traffic_bits / 10**6  # Переводим в мегабиты
        megabytes = megabits / 8  # Переводим в мегабайты
        return f"Объем переданного трафика в мегабитах: {megabits:.2f} Мб\nОбъем переданного трафика в мегабайтах: {megabytes:.2f} МБ"

    if disk_capacity is not None and network_speed is None:
        # Рассчитываем количество информации на DVD-R
        disk_bits = disk_capacity * 8 * 10**9  # Переводим гигабайты в биты
        return f"Количество информации на DVD-R: {disk_bits} бит"

    if network_speed is not None and disk_capacity is not None:
        # Рассчитываем время передачи данных с диска по сети
        disk_bits = disk_capacity * 8 * 10**9  # Переводим гигабайты в биты
        transfer_time_seconds = disk_bits / (network_speed * 10**6)
        return f"Время передачи данных с диска по сети: {transfer_time_seconds:.2f} сек"




