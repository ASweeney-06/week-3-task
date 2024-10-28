a = 0
list = []
sequence = []
def function(k,a):
    global list
    global sequence
    occured = False
    #print("a: "+str(a))
    #print("k: "+str(k))
    #print(list)
    for i in range(len(list)):#has a already been said
        if str(list[i]) == str(a-k):
            occured = True
    list = list + [a]
    if a-k > 0 and occured == False:
        a = a-k
    else:
        a = a+k
    sequence = sequence +[a]
    return a

for k in range(1):
    a = function(k,a)
    #print("a: "+str(a))
print(sequence)
sequence = []

for k in range(4):
    a = function(k,a)
    #print("a: "+str(a))
print(sequence)
sequence = []

for k in range(8):
    a = function(k,a)
    #print("a: "+str(a))
print(sequence)
sequence = []

for k in range(16):
    a = function(k,a)
    #print("a: "+str(a))
print(sequence)
sequence = []

for k in range(32):
    a = function(k,a)
    #print("a: "+str(a))
print(sequence)
sequence = []