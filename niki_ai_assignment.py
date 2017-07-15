x=raw_input("Enter the number")
x=int(x)
mod=1000000007



a=1
b=1

for i in range(x-1):
	temp=a
	a=b
	b=((temp%mod)+(b%mod))%mod

print ((a%mod)+(b%mod))%mod

