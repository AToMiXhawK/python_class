"""Given a number, you need to check whether any permutation of the number is divisible by 8 or not. Print Yes or No."""

for testcase in range(int(input())):
    N = input()
    lst = []
    flag = 0
    for j in N:
        lst.append(j)
    perm = permutations(lst,len(N))
    for i in list(perm):
    	st = ""
    	for j in i:
    		st+=j
    	if int(st) % 8 == 0:
    		print("Yes")
    		flag = 1
    		break
    if flag==0:
        print("No")
