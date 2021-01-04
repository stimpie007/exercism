def total(basket):
    price = 800
    discount = {
        2: 5,
        3: 10,
        4: 20,
        5: 25
    }

    # Make group of books
    groups = list()
    while basket:
        books = list()
        for book in set(basket):
            books.append(book)
            basket.pop(basket.index(book))
        groups.append(books)

    # Calculate price
    purchase_price = 0
    for group in groups:
        if len(group) in discount:
            percentage = discount[len(group)]
            purchase_price += int(len(group) * (price - (price / 100 * percentage)))
        else:
            purchase_price += int(len(group) * price)

    return purchase_price
