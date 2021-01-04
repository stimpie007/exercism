def triplets_with_sum(number):
    return [t for t in triplets_in_range(1, number) if sum(t) == number]


def triplets_in_range(start, end):
    triplets = []

    for n in range(start, end - 3):
        for m in range(n + 1, end - 2):
            triplet = [n, m, end - n - m]

            if is_triplet(triplet):
                triplets.append(triplet)

    return triplets


def is_triplet(triplet):
    return triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2 and triplet[0] < triplet[1] < triplet[2]
