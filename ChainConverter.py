with open("ChainInput.txt","r+") as r:
    sequence = r.readline().strip("\n")

dictNuc = {"A":"T","T":"A","G":"C","C":"G"}
sequenceNew = ""

seq = "".join(dictNuc.get(char.upper(),char) for char in sequence)

temp = 0
primer_parts = seq.split("-")
if len(primer_parts[0])>len(primer_parts[1]):
    total_temp = sum([temp+4 if codon in "GC" else 2 for codon in primer_parts[0]])
else:
    total_temp = sum([temp + 4 if codon in "GC" else 2 for codon in primer_parts[2]])


startsign,stopsign = "5'","3'"
oplossing = f'{stopsign}-{seq}-{startsign}'

print('-'*10)
print(f'{startsign}-{sequence.upper()}-{stopsign}')
print(oplossing)
print('-'*10)
print("FORWARD PRIMER: " +oplossing + " temp: "+str(total_temp))
print("REVERSE PRIMER: "+ oplossing[::-1] + " temp: "+str(total_temp))