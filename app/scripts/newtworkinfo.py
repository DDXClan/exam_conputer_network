import ipaddress

async def networkinfo(ip: str, mask: str) -> str:
    ip_address = ip
    subnet_mask = mask
    n = ipaddress.IPv4Network(f'{ip_address}/{subnet_mask}', strict=False)
    first, midle, last = n[1], n[-2], n[-1]
    return f'первый: {first}, последний: {midle}, шировещательный: {last}'


    