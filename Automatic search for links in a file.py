
with open('Ссылки1', "r", encoding='utf-8') as f:
    list_links = f.read()


with open('Ссылки2', "r", encoding='utf-8') as d:
    list_links2 = d.read()


list_links = list_links.split()
list_links2 = list_links2.split()
all_links = list_links + list_links2

lst1 = []
lst2 = []

for i in all_links:
    if all_links.count(i) == 1:
        lst1.append(i)
    else:
        lst2.append(i)


with open('Неповторящиеся ссылки.txt', 'w', encoding='utf-8') as file:

    for j in lst1:
        file.write(str(j) + '\n')


with open('Повторящиеся ссылки.txt', 'w', encoding='utf-8') as file2:

    for k in set(lst2):
        file2.write(str(k) + '\n')






