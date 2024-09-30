bøker = ['The Hobbit',
         'Farmer Giles of Ham',
         'The Fellowship of the Ring',
         'The Two Towers',
         'The Return of the King',
         'The Adventures of Tom Bombadil',
         "Tree and Leaf"]
print(bøker[0])
print(bøker[1])
print(bøker[5])
print(bøker[6])

bøker.append('The Silmarillion')
bøker.append('Unfinished Tales')
for i in range (len(bøker)):
    if bøker[i] in ['The Fellowship of the Ring', 'The Two Towers', 'The Return of the King']:
        bøker[i] = 'Lord of the Rings: ' + bøker[i]
print(sorted(bøker))