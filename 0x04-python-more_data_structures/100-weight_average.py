#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    for tup in my_list:
        num += tup[0] * tup[1]
        den += tup[1]

    return (num / den)
            if r_num == ch:
                if rom_n.get(ch) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [rom_n.get(ch)]
                else:
                    list_num.append(rom_n.get(ch))

                last_rom = rom_n.get(ch)

    num += to_subtract(list_num)

    return (num)
