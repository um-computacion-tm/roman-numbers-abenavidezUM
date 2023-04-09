import unittest

def to_roman(decimal):
    if decimal <= 0:
        return ""

    romanos = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    numero_romano = ""
    for numero, letra in romanos.items():
        while decimal >= numero:
            numero_romano += letra
            decimal -= numero

    return numero_romano


if __name__ == "__main__":
    print(to_roman(75))
 
