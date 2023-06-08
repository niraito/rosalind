fi = open('rosalind_ini5.txt', 'r')

inscription = []
for i in fi:
  inscription.append(str(i))

#print(len(inscription))
outscription = []
for i in range(0, len(inscription)):
  if i % 2 == 1:
    outscription.append(str(inscription[i]))

# Here we open output file in append mode, so if you already have a file named as output:
# delete it, and start over again ;)
with open('output.txt', 'a') as fo:
  for i in outscription:
    fo.write(i)
