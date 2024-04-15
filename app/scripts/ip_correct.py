import ipaddress

def get_address_type(ip_address):
    response = ''
    try:
        ip = ipaddress.ip_address(ip_address)
        if ip.is_multicast:
            response += "Мультикаст"
        elif ip.is_private:
            response += "Частный"
        elif ip.is_loopback:
            response += "Локальный (петлевой)"
        elif ip.is_link_local:
            response += "Локальный (для сети)"
        elif ip.is_reserved:
            response += "Зарезервированный"
        elif ip.is_global:
            response += "Глобальный (уникаст)"
        else:
            response += "Неизвестный"
    except ValueError:
        response += "Недопустимый IP адрес"
    return response


