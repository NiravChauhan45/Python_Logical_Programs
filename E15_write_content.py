# Excercise 15 : Write all content of a given file into a new file by skipping line number 

with open("nirav.txt","r") as fp:
    lines = fp.readlines()

with open("nirav2.txt","w")as fp:
    count = 0
    for line in lines:
        if count==4:
            count+=1
            continue
        else:
            fp.write(line)
        count+=1