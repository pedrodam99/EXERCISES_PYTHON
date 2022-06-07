tempo = int(input(''))

hrs = tempo // 3600
resto_hrs = tempo % 3600

mins = resto_hrs // 60
resto_mins = resto_hrs % 60

segs = resto_mins


print('%d:%d:%d' %(hrs, mins, segs))
