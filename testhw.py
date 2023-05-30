def month_generator():
    months = ["січень", "лютий", "березень", "квітень", "травень", "червень",
              "липень", "серпень", "вересень", "жовтень", "листопад", "грудень"]
    while True:
        for month in months:
            yield month


generator = month_generator()
for i in range(13):
    print(next(generator))
