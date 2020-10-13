#COPY YOUR CHAIN IN ChainInput.txt, more info about the markup in bespoke file

with open("ChainInput.txt","r+") as r:
    sequence = r.readline().strip("\n")

dictNuc = {"A":"T","T":"A","G":"C","C":"G"}
sequenceNew = ""

seq = "".join(dictNuc.get(char.upper(),char) for char in sequence)

startsign,stopsign = "5'","3'"
origineel = f'{startsign}-{sequence.upper()}-{stopsign}'
oplossing = f'{stopsign}-{seq}-{startsign}'

temp = 0
primer_parts = seq.split("-")
if len(primer_parts[0])>len(primer_parts[1]):
    total_temp = sum([temp+4 if codon in "GC" else 2 for codon in primer_parts[0]])
    primer = "REVERSE PRIMER: " + oplossing[::-1] + " temp: " + str(total_temp)
else:
    total_temp = sum([temp + 4 if codon in "GC" else 2 for codon in primer_parts[2]])
    primer = "FORWARD PRIMER: " + origineel + " temp: " + str(total_temp)

print('-'*30)
print(origineel+"\n"+oplossing)
print('-'*30)
print(primer)
