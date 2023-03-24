""" It should get the dict, get the kw and its value.
    Make it as a sep lst and return a new dict with kw and val swapped !

**  Author: S.Abul Aiman Shaa
    Age: 13
    Mom: K.Sharmila Begum
    Dad: A.Shajahan Abdul Rahman
    brother_1: S.Abul Aalik Shaa
**  brother_2: S.Abul Aidin Shaa

"""

# Randomized "list", "tuple", "dictionary", "set".
def randomize(dt):
    init = list(dt)
    value_hash = set(init)
    value_hex = list(value_hash)
    return value_hex[0]


# Swapping dictionary kw -> val, val -> kw.
def swap_dict(_dict: dict):
    updated_dict = dict()
    kw = list(_dict.keys())
    val = list(_dict.values())
    for i in range(len(_dict)):
        updated_dict.update({val[i]: kw[i]})

    return updated_dict


if __name__ == '__main__':
    test = {'Air': 0,
            'F': 86,
            'C': 12,
    }

    print(test, '\n')
    print(swap_dict(test))

    test_2 = {"A", "B", "C", "D", "E"}

    print(randomize(test_2))