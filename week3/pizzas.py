pizza_base = ["mozzarella", "tomato", "flour", "yeast","salt"]
vesuvio = ["salame", "ricotta", "spicy oil"]
popeye = ["ricotta", "spinach"]
spicy = ["salame", "spicy oil"]
popeye.extend(pizza_base)
vesuvio.extend(pizza_base)
popeye.append("mushrooms")
vesuvio.remove("mozzarella")
not_wasted = []
while len(popeye) > len(vesuvio):
    not_wasted.append(popeye.pop())
for x in spicy:
    if x not in vesuvio:
        not_wasted.append(x)

everything = list()
everything.extend(pizza_base)
everything.extend(vesuvio)
everything.extend(popeye)
everything.extend(spicy)
everything.extend(not_wasted)

for element in everything:
    print(everything.count(element))
    if element in pizza_base:
        print(pizza_base.index(element))
        pizza_base.remove(element)
    if element in vesuvio:
        print(vesuvio.index(element))
        vesuvio.remove(element)
    if element in popeye:
        print(popeye.index(element))
        popeye.remove(element)
    if element in spicy:
        print(spicy.index(element))
        spicy.remove(element)
    if element in not_wasted:
        print(not_wasted.index(element))
        not_wasted.remove(element)
print(len(everything))
print(everything)
everything.clear()