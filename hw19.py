with open('new.txt', mode='r+', encoding='utf-8') as my_file:
    for line in my_file:
        airport_data = line.strip().split(';')
        name = airport_data[2]
        iso_country = airport_data[5]

        if iso_country == "UA":
            print(name)
