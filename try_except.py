# my_dict = {"a":1, "b":2, "c":3}
# try:
#     value = my_dict["a"]
# except KeyError:
#     print("Noexiste")
# else:
#     print("Funcionaa")



my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["Hola"]
except IndexError:
    print("El índice no existe")
except KeyError:
    print("Noexiste")
else:
    print("Funcionaa")