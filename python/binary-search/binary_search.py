def find(search_list, value):
    left_most = 0
    right_most = len(search_list) - 1
    while left_most <= right_most:
        m = (left_most + right_most) // 2
        if search_list[m] < value:
            left_most = m + 1
        if search_list[m] > value:
            right_most = m - 1
        if search_list[m] == value:
            return m
    raise ValueError(f"{value} novalue found in {search_list}")
