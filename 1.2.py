import os

#TODO1:

flats = [[3189226, 1, 11, "построена", 5, "да"], [3500000, 1, 9, "построена", 2, "нет" ],
[3200000, 1, 20, "построена", 6, "да"], [3300000, 1, 8, "построена", 9, "да"],
[3400000, 1, 20, "построена", 3, "нет"],[3400000, 1, 2, "построена", 4, "нет"],
[2999000, 2, 16, "построена", 8, "да"], [3490000, 1, 4, "построена", 2, "да"],
[2999000, 1, 6, "построена", 5, "нет"], [2759730, 1, 1, "строится", 4, "да"],
[2369234, 1, 10, "строится", 10, "да"]]

#стоимость, кол-во комнат, пешком до метро (мин), построена/строится, этаж, ниличие лифта


#TODO2:
for i, flat in enumerate(flats):
    if "построена" in flat[3] and flat[2] <= 15 and (flat[4] == 1 or flat[5] == "да"):
        print (("{0}. {1}").format(i, str(flat)))

os.system("pause")