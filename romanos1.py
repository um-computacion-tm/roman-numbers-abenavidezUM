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


def to_decimal(romanos):
    diccionario = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_num = 0
    for i in range(len(romanos)):
        if i > 0 and diccionario[romanos[i]] > diccionario[romanos[i-1]]:
            decimal_num += diccionario[romanos[i]] - 2 * diccionario[romanos[i-1]]
        else:
            decimal_num += diccionario[romanos[i]]
    return decimal_num



if __name__ == "__main__":
    
   print(to_roman(75))
   print(to_decimal("MCI"))
