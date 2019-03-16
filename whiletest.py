tmp=27
print('input number:' + str(tmp))
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b=[]
count=0
#qiu shang
shang=int(tmp)//26
print('shang: ' + str(shang))
# qiu count:
while True:
	if shang>1:
		count=count+1
		shang=shang//26
	
	else:
		break

print('count: ' + str(count))

yushu=int(tmp)%26
# qiu ge wei shu：
b.insert(0,a[yushu-1])
#print(b)
while count>0:
	b.insert(0,a[count-1])
	count=count-1

print('answer: ' + str(b))

