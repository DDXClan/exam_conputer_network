def calculate_network_address(ip_address_str, subnet_mask):
    # Разбиваем IP-адрес и маску сети на октеты
    ip_octets = [int(octet) for octet in ip_address_str.split('.')]
    mask_octets = [int(octet) for octet in subnet_mask.split('.')]
    
    # Выполняем операцию "И" для каждого октета IP-адреса и маски сети
    network_octets = [ip_octets[i] & mask_octets[i] for i in range(4)]
    
    # Собираем октеты в строку адреса сети
    network_address = '.'.join(map(str, network_octets))
    
    return network_address

def calculate_host_address(ip_address_str, subnet_mask):
    # Разбиваем IP-адрес и маску сети на октеты
    ip_octets = [int(octet) for octet in ip_address_str.split('.')]
    mask_octets = [int(octet) for octet in subnet_mask.split('.')]
    
    # Выполняем операцию "И" для каждого октета IP-адреса и инвертированной маски сети
    host_octets = [ip_octets[i] & (~mask_octets[i] & 0xff) for i in range(4)]
    
    # Собираем октеты в строку адреса узла
    host_address = '.'.join(map(str, host_octets))
    
    return host_address

def fill_table(ip_addresses):
    table = []
    for ip_str in ip_addresses:
        # Определение класса IP-адреса
        first_octet = int(ip_str.split('.')[0])
        if first_octet <= 127:
            ip_class = 'A'
        elif first_octet <= 191:
            ip_class = 'B'
        else:
            ip_class = 'C'
        
        # Вычисление стандартной маски сети
        if ip_class == 'A':
            mask = '255.0.0.0'
        elif ip_class == 'B':
            mask = '255.255.0.0'
        else:
            mask = '255.255.255.0'
        
        # Определение адреса сети
        network_address = calculate_network_address(ip_str, mask)
        
        # Определение адреса узла
        host_address = calculate_host_address(ip_str, mask)
        
        # Получение широковещательного адреса
        broadcast_address = '.'.join(network_address.split('.')[:-1]) + '.255'
        
        # Добавление результатов в список
        table.append({
            "IP адрес": ip_str,
            "Класс": ip_class,
            "Стандартная маска сети": mask,
            "Адрес сети": network_address,
            "Адрес узла": host_address,
            "Адрес маски класса": mask,
            "Широковещательный адрес": broadcast_address.replace('0', '255')
        })
    
    return table

# Список IP-адресов узлов для заполнения таблицы
ip_addresses = [
    '162.72.133.14',
    '109.126.115.12',
    '202.14.155.174',
    '65.142.63.136',
    '192.164.211.22'
]

# Заполнение таблицы
table = fill_table(ip_addresses)

# Вывод таблицы
for row in table:
    print(row)
