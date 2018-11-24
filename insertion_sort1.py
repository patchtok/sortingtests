#Take the first item from your unsorted list, remove it and place it in the sorted list
#Take the next item in the unsorted list and insert it into the right place in the sorted list
#Do this until the unsorted list is empty
y= [5,9,11,3,12,7,-1, 7, -12, 8,8,8,8,8,8]
z=[5,4,1,7,3,0,6,2,9,8]
A = z
S = []
S.append(A[0])
A.remove(A[0])
print(A, end='')
print(S)
total_checks = 0
while len(A)>0:
    i = len(S)-1
    check_count = 0
    while i >= 0 and A[0] < S[i] :
        i -= 1
        check_count += 1
    total_checks += check_count
    S.insert(i+1, A[0])
    A.remove(A[0])
    print(A, end='')
    print(S, end='')
    print("Checks = {}".format(check_count))

print("Total Checks = {}".format(total_checks))