# dictionaries
capitals_dict = {"Iowa" : "Des Moines", "Wisconsin" : "Madison"}
print(capitals_dict)
print(capitals_dict["Iowa"])
print(capitals_dict.get("Iowa")) # normal way
print(capitals_dict.get("Missouri" , "Failed"))
capitals_dict["Utah"] = "Salt Lake City"
print(capitals_dict)
capitals_dict["California"] = "Sacramento"
print(capitals_dict)

#del capitals_dict["California"]
#print(capitals_dict)

print(capitals_dict.values())
print(capitals_dict.keys())

print()
for capital in capitals_dict:
    print(capital, capitals_dict[capital])


cards = [2,3,4,5,6,7,8,9,10, "J" , "Q", "K", "A"]
suits = ["C", "H", "S", "D"]
for suit in suits:
    for card in cards:
        pass


