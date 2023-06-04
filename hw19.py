with open('airport.csv', mode='r+', encoding='utf-8') as my_file:
    for line in my_file:
        airport = line.strip().split(';')
        name = airport[0]
        iso_country = airport[1]

        if iso_country == "UA":
            print(name)
