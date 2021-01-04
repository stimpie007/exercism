class Luhn:
    def __init__(self, card_num):
        self.card_number = card_num.replace(' ', '')
        self.valid = self.valid()

    def checksum(self):
        digits = list(map(int, self.card_number))
        odd_sum = sum(digits[-1::-2])
        even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
        return (odd_sum + even_sum) % 10

    def valid(self):
        return self.checksum() == 0 if self.card_number.isdigit() and self.card_number != "0" else False
