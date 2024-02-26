word = 'Help' + 'A'
print(word)
print(word[2])
print(word[0:2])
print(word[:2])

x = int(input("Please enter an integer: "))
if x < 0:
	x = 0
	print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

a = ['cat', 'dog', 'mouse'] 
for x in a:
	print(x, len(x))

for x in range(0, len(a)):
	print(x, a[x])

questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('What is your {0}? It is {1}.'.format(q, a))
