a=int(input())
for i in range(2,a):
	if(a%i==0):
		print(a,"is not a prime number")
		break
	else:
		print(a,"is prime number")
		break
