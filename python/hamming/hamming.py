def distance(strand_a, strand_b):
    differences = 0

    if len(strand_a) is len(strand_b):
        for position, character in enumerate(strand_a):
            differences += 1 if character != strand_b[position] else 0
    else:
        raise ValueError("The 2 given strands are not the same length! :'-(")

    return differences
