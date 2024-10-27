import re
import time
def convert_date(date_str):
    # Определение шаблона для поиска даты
    date_pattern = r'(\d{2,4})\-(\d{1,2})\-(\d{1,2}) (\d{2})\:(\d{2})'

    # Поиск даты
    match = re.search(date_pattern, date_str)

    if match:
        # Получение частей даты
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        hour = match.group(4)
        minute = match.group(5)
        # Преобразование порядка компонентов
        new_date = f"{day}-{month}-{year} {hour}:{minute}"

        return date_str.replace(match.group(), new_date)
    else:
        return date_str

def popular(s):
    t = []
    m = s.split(';\n')
    for i in m:
        k = i.split('\n')
        k[0] = k[0][:-8]
        k[1] = int(k[1][k[1].find(' ')+1:k[1].find('.')])
        l = (k[0],k[1])
        t.append(l)
    d = dict(t)
    max_keys = []
    for k in d:
        if d[k] == max(d.values()):
            max_keys.append(k+' '+'КОЛ-ВО: '+str(max(d.values())))
    return ','.join(max_keys)


def product_finder(s):
    s = s.replace(',','.')
    k = []
    m = s.split('\n')
    for i in range(len(m)):
        if (' Х ' in m[i] or ' х ' in m[i]):
            k.append(m[i-1]+' КОЛ-ВО:\n'+m[i])
    return ';\n'.join(k)

def itog(s):
    m = s.split('\n')
    m1 = []
    for i in m:
        if 'итог' in i:
            m1.append(i)
    m2 = set()
    for i in m1:
        i = i.replace('.',' ').replace(',',' ').replace('=',' ').split()
        for j in i:
            try:
                if int(j)!=0:
                    m2.add(int(j))
            except:
                pass

    for i in m2:
        return i
def data_finder(s):
    date_finder = '\d{2}-\d{2}-\d{2} \d{2}:\d{2}'
    m = s.split('\n')
    k = ''
    for i in m:
        match = re.search(date_finder, i)
        if match:
            k = i
    k = k[:k.rfind('-')+1] + '20' + k[k.rfind('-')+1:]
    return k
def date_conv(s):
    halal_object = time.strptime(s, "%d-%m-%Y %H:%M")
    halal_time = time.strftime("%d-%m-%Y %H:%M", halal_object)
    halal_time1 = time.strftime("%d-%m-%Y %H:%M", time.localtime(time.time()))
    m = [halal_time,halal_time1]
    return m