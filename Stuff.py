def verify_card_number(string):
    string = string.replace('-', '').replace(' ', '')
    digits = [int(ch) for ch in string]
    for i in range(len(digits)-2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    if sum(digits) % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID'

string = '453914881'
print(verify_card_number(string))