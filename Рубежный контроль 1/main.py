from operator import itemgetter


class Os:
    def __init__(self, id, name, cost, comp_id):
        self.id = id
        self.name = name
        self.cost = cost
        self.comp_id = comp_id


class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class OsComp:
    def __init__(self, os_id, comp_id):
        self.os_id = os_id
        self.comp_id = comp_id


comps = [
    Computer(1, 'Acer'),
    Computer(2, 'Msi'),
    Computer(3, 'Asus'),
    Computer(4, 'Lenovo'),
    Computer(5, 'Apple')
]

oses = [
    Os(1, 'Windows', 2900, 3),
    Os(2, 'Abuntu', 3510, 2),
    Os(3, 'MacOS', 5450, 5),
    Os(4, 'ChromeOS', 1480, 2),
    Os(5, 'Adora', 4370, 3)
]

oses_comps = [
    OsComp(1, 3),
    OsComp(2, 2),
    OsComp(3, 5),
    OsComp(4, 2),
    OsComp(5, 3),

    OsComp(1, 2),
    OsComp(2, 4),
    OsComp(3, 1),
    OsComp(4, 4),
    OsComp(5, 1)
]


def main():
    one_to_many = [(o.name, o.cost, c.name)
                   for c in comps
                   for o in oses
                   if c.id == o.comp_id]

    many_to_many_temp = [(c.name, oc.os_id, oc.comp_id)
                         for c in comps
                         for oc in oses_comps
                         if c.id == oc.comp_id]

    many_to_many = [(o.name, o.cost, c_name)
                    for c_name, oc_id, c_id in many_to_many_temp
                    for o in oses
                    if o.id == oc_id]

    print('Задание B1: ')
    res1 = []
    for name, _, comp in one_to_many:
        if name[0] == "A":
            res1.append((name, comp))
    print(res1, "\n")

    print('Задание B2: ')
    res2 = []
    for c in comps:
        c_oses = list(filter(lambda x: x[2] == c.name, one_to_many))
        if len(c_oses) > 0:
            c_cost = [cost for _, cost, _ in c_oses]
            c_cost_min = min(c_cost)
            res2.append((c.name, c_cost_min))
    res2_sorted = sorted(res2, key=itemgetter(1))
    print(res2_sorted, "\n")

    print('Задание B3: ')
    res3 = []
    for name, _, comp in many_to_many:
        res3.append((name, comp))
    res3_sorted = sorted(res3, key=itemgetter(0))
    print(res3_sorted)


if __name__ == "__main__":
    main()
