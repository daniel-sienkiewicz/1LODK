def func1():
	print 1

def func2():
	print 2

funclist = [func1, func2]

for f in funclist:
	f()
