#!/usr/bin/env python

mygenerator = (x*x for x in range(5)) # Generators are iterators, but you can only iterate over them once. It's because they do not store all the values in memory, they generate the values on the fly

#It is just the same except you used () instead of []

for i in mygenerator:
	print(i)

for j in mygenerator: # This will not work
	print(j)," >"
