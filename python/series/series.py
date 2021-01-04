from typing import List


def slices(series: str, length: int) -> List[str]:
    """
    Get slices for a series according to the given length

    :param
    series: str
    length: int

    :return:
    List[str]
    """
    if length > len(series) or length <= 0 or not series:
        raise ValueError(".+")
    else:
        return list(series[x:length + x] for x in range(len(series)) if len(series[x:length + x]) == length)
