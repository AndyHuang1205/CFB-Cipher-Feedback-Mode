"""
3/26/2023
CFB
"""

cipher_table = {
    '0b00': '0b01',
    '0b01': '0b10',
    '0b10': '0b11',
    '0b11': '0b00'
}

message = ["0b00", "0b01", "0b10", "0b11"]


def CFB(message, IV="0b10"):
    output = []
    for m in message:
        key = cipher_table.get(IV)
        xor = '0b{:02b}'.format(int(key, 2) ^ int(m, 2))
        IV = xor
        print(xor)


CFB(message)
