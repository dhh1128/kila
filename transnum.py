digit_names = ["zo", "un", "to", "si", "kq", "fai", "cei", "sxt", "ok", "nuv"]
first_digit = ord('0')

def _trans_triplet(triplet, power_of_ten) -> str:
    if triplet == "000": return ''
    answer = ''
    for digit in triplet:
        answer += digit_names[ord(digit) - first_digit]
    if power_of_ten >= 3:
        answer += "po" + translate_number(power_of_ten)
    return answer

def translate_number(value: int) -> str:
    prefix = ''
    if value < 0:
        value *= -1
        prefix = "hi"
    digits = str(value)
    words = []
    power_of_ten = 0
    for i in range(len(digits), 0, -3):
        triplet = digits[max(0, i - 3):i]
        words.insert(0, _trans_triplet(triplet, power_of_ten))
        power_of_ten += 3
    return prefix + ' '.join(words)

while True:
    number = input()
    print(translate_number(int(number)))
