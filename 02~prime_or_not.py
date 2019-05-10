def prime(n):
	if n==1 or n==0:
		print(n,"is Neither Prime Nor Composite")
		return
	i=2
	while i<=n/2:
		if n%i==0:
			print(n,"is Not a Prime Number")
			return
		else:
			i+=1
	print(n,"is a Prime Number")
	return
	
n=input("Enter a Number: ")
prime(n)
