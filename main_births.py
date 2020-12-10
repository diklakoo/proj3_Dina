d ={}
with open('births.csv') as file:
    for line in file:
        if line.startswith('"year"'):
            continue
        else:
            line=line.rstrip().split(",")
            year=int(line[0])
            state = line[1]
            births = int(line[3])
            if year >= 1986 and year <= 2006:
                if state in d :
                    d[state]= d[state]+ births
                else:
                    d[state] = births

for key,val in d.items() :
    print (f" {key} has {val:,} births total." )


max_state = max(d, key=d.get)
max_births =  max(d.values())
print(f"the state with the most births is :  {max_state} , with {max_births: ,} births total .")
