key=int(input("Enter the key"))
list=[1,34,55,32,65,14]
location = 0
found = 0
i = 0
while(i<=len(list)-1):
	if list[i]==key:
		found =1
		location =i+1
		break
	else:
		i = i+1
if found ==0:
	print("the key element is not present in the list")
else:
	print(location)
