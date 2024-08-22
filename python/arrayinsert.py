


def insert_any(a,U,location,key):
	if a[U] is not None:
		print("array is full")
		return a
	i= U
	while i>location:
		a[i]=a[i-1]
		i= i-1
	a[i]=key
	return a


a = [2,5,3,45,None,None]
U= 4

key = 43
location = 2

result = insert_any(a,U,location,key)

print(result)
