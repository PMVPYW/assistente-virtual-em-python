hours = 0
minutes = 0
end = ""
open("sound/time/list.txt", "w")
print("processing...")
while hours != 24:
    strhour = str(hours)
    strminutes = str(minutes)

    minutes += 1

    if minutes >= 60:
        hours += 1
        minutes = 0
    print(f"{strhour}:{strminutes}")
    with open("sound/time/list.txt", "a+") as f:
        f.write(f"{strhour} horas, {strminutes} minutos.\n")
    
#print(end)
