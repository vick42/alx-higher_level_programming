#1/usr.bin/python3
# Author - Victor Kiriinya

def remove_char_at(str, b):
    if b < 0:
        return (str)
    return (str[:b] + str[b+1:])
