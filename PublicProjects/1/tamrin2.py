tarikhTavalod = int(input("Tarikh tavalod ra vared konid : "))

print(tarikhTavalod)

strTT=str(tarikhTavalod)
stra=[]
for i in strTT:
    stra.append(i)


print ("saal : ",stra[0]+stra[1])
print ("maah : ",stra[2]+stra[3])
print ("rooz : ",stra[4]+stra[5])