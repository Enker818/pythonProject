bøker = []
bøker.append('The Two Towers')
bøker.append('The Return of the King')
bøker.append('The Fellowship of the Ring')
for i in range (len(bøker)):
     bøker[i] = 'Lord of the Rings: ' + bøker[i]
print("Innhold i Lord of the Rings-listen (tradisjonell for-løkke):")
for x in bøker:
    print(x)
i = 0
print("eller")
while i < len(bøker):
    print(bøker[i])
    i +=1