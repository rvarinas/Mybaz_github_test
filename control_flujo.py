#Ciclo for
names = ['Hugo', 'Paco', 'Luis']
absence = []

# for name in names:
#     #print(name)
#     if name == 'Paco':
#         print(name + ' si se encuentra en clase')
#     else:
#         absence.append(name)

# print ('Lista de alumnos ausentes')
# print(absence)

### Ciclo while
# i = 1
# while i < 8:
#     print(i)
#     if i == 8:
#         break
#     i += 1

# for name in names:
#     if name != 'Paco':
#         absence.append(name)
#     else:
#         print (name + ' si se encuentra en clase')
# print(absence)

def evaluacion_edad(age):
    if age < 4:
        ticket_price = 0
    elif age < 18:
        ticket_price = 10
    else:
        ticket_price = 15
    
    print(ticket_price)

age = int(input("Ingresa la edad"))
evaluacion_edad(age)

    




