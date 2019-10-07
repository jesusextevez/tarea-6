#L-2
base = 5
espacios = base - 1
contador = 1
for x in range(base):
    while espacios >=0:
        print ('%s%s%s'%((' '*espacios), ('*'*contador),(' '*espacios)))
        espacios -=1
        contador +=2
