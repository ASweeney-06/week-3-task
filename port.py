a = 0
k = 1
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
for k in range(10):
    a = function(k,a)
    print("a: "+str(a))
print(sequence)