#!/usr/bin/env python

def createGenerator():
	mylist = range(7)
	
	for i in mylist:
		yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!



for i in mygenerator:
	print(i)

for j in mygenerator:
	print(j)
