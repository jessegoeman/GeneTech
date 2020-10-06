with open("ChainInput.txt","r+") as r:
    sequence = r.readline().strip("\n")

dictNuc = {"A":"T","T":"A","G":"C","C":"G"}
sequenceNew = ""
for char in sequence:
    sequenceNew+=dictNuc[char.upper()]

startsign,stopsign = "5'","3'"

print(f'{startsign}-{sequence.upper()}-{stopsign}')
print(f'{stopsign}-{sequenceNew.upper()}-{startsign}')
