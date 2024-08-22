def insert(a,loc,key):
	n = len(a)
	i = loc
	while i<n and a[i] is not None:
		i = i+1
	if i>=n:
		print("array full")
		return a
	while i>loc:
		a[i]=a[i-1]
		i= i-1
	a[loc] = key
	return a
	
a = [1, 2, 4, 5, None]
loc = 2  # Position where we want to insert the key

# Key to be inserted
key = 10

# Insert the key into the array
result = insert(a, loc, key)
print(result)
	
	
