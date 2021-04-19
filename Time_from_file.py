#  read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages
file = input("Enter File: ")
if len(file) < 1: file = "mbox-short.txt" #fast access
nfile = open(file)
dictit = dict()
for line in nfile:
    if not line.startswith("From"): continue #looking for necessiary lines
    sline = line.split()
    if sline[0] != "From": continue
    time = sline[5] #picking up time
    time = time.split(":")
    hour = time[0]
    dictit[hour] = dictit.get(hour, 0) +1 

#Sort by hours  
result = (sorted( [(k,v) for k,v in dictit.items() ]))
for h, q in result:
    print(h, q)
