roman_map = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]

def to_roman(num: int) -> str:
    if num <= 0 or num > 3999:
        raise ValueError("Number must be between 1 and 3999")

    result = ""
    for value, numeral in roman_map:
        while num >= value:
            result += numeral
            num -= value
    return result


def to_arabic(roman: str) -> int:
    roman = roman.upper()

    roman_values = {r: v for v, r in roman_map}
    i = 0
    total = 0

    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i+2] in roman_values:
            total += roman_values[roman[i:i+2]]
            i += 2
        else:
            if roman[i] not in roman_values:
                raise ValueError("Invalid Roman numeral")
            total += roman_values[roman[i]]
            i += 1

    return total
