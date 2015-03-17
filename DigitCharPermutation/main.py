digits = '123456789'
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

k = 0

for i in range(0,9):
    for j in range(0,9):
        k += 1
        print '%s\t%s' % (str(k), str(digits)[i] + str(digits)[i])
        
for i in range(0,9):
    for j in range(0,26):
        k += 1
        print '%s\t%s' % (str(k), str(digits)[i] + characters[j])
        
for i in range(0,26):
    for j in range(0,9):
        k += 1
        print '%s\t%s' % (str(k), characters[i] + str(digits)[j] )

for i in range(0,26):
    for j in range(0,26):
        k += 1
        print '%s\t%s' % (str(k), characters[i] + characters[j] )