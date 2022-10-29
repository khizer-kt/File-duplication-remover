List = [open("duplications.txt").readlines()]
List = list(dict.fromkeys(List))
with open("no_duplications.txt","w") as filehandle:
    for listitem in List:
        filehandle.write(f'{listitem}\n')
