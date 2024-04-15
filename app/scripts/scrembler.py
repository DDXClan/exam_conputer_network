def scrembler(string: str):
    string.split()
    bool_list = ['', ]
    result = list()
    response = 'Результат: '
    for x in string:
        if x == '1':
            bool_list.append(True)
        else: bool_list.append(False)
    for x in range(1, len(bool_list)):
        if x > 5:
            result.append(int((bool_list[x] ^ bool_list[x-3]) ^ bool_list[x-5]))
        elif x > 3 and x < 6:
            result.append(int(bool_list[x] ^ bool_list[x-3]))
        else:
            result.append(int(bool_list[x]))
    for x in result:
        response += str(x)
    return response

print(scrembler('11001001111'))
