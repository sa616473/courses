
# raisin 7^4 can be done two ways
x = 7*7*7*7
print x

# simple way
x = 7**4
print x

# truning a string into a character array
s = "Hi there Sam!"
l = list(s)
print l

# spliting a string according to spaces and new lines

l = s.split()
print l


planet = "Earth"
diameter = 12742
# without using .format()
print 'The diameter of', planet, 'is', diameter, 'kilometers'
# Using .format()
print 'The diameter of {} is {} kilometers'.format(planet, diameter)

#Given the nested dictonary grab the word hello

d = {'k1': [1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print d.keys()
print d['k1'][3]['tricky'][3]['target'][3]

# the main difference between a tuple and a list is that 
# a list is mutable and tuple is immutable

#simple function that returns the email.com
def domainget(email):
	x = email.split('@')
	return x[1]


#Fancy
def domaingetfancy(email):
	return email.split('@')[1]

print domainget('saitejasmopuri@gmail.com')
print domaingetfancy('saitejasmopuri@gmail.com')

# a function returns true if the word dog is presented in the string
def finddog(s):
	x = s.lower()
	y = x.split()

	for i in range(len(y)):
		if y[i] == 'dog':
			return True
	return False

print finddog('Is there a dog here?')

# A function that counts the occurences of the word dog

def countdog(s):
	counter = 0
	x = s.lower().split()
	for i in range(len(x)):
		if x[i] == 'dog':
			counter = counter + 1
	return counter

print countdog('This dog is faster than 10 dog with 5 dog')



seq = ['soup', 'dog', 'salad', 'cat', 'great']

# without using lamda and filter expression
x = []
for i in range(len(seq)):
	if seq[i][0] == 's':
		x.append(seq[i])
print x;

# using lambda expression  and the filter function

print list(filter(lambda word : word[0] == 's', seq))

# You are driving a little too fast, and a 
# police officer stops you. Write a function
# to return one of 3 possible results:
# No ticket, Small ticket, or Big Ticket.
# If your speed is 60 or less, the result is
#  No Ticket. If speed is between 61 nd 80 
#  inclusive, the result is Small Ticket.
#  If speed is 81 or more, the result is
#  Big Ticket unless it is your birthday 
#  (encoded as a boolean value in the parameters of the function)  
#  on your birthday, your speed can be 5 higher in all cases.

def caught_speeding(speed, is_birthday):
	if is_birthday == False:	
		if speed <= 60:
			return 'NO TICKET'
		elif speed > 60 and speed <= 80:
			return 'SMALL TICKET'
		elif speed > 80:
			return 'BIG TICKET'

	elif is_birthday == True:	
		if speed <= 65:
			return 'NO TICKET'
		elif speed > 65 and speed <= 85:
			return 'SMALL TICKET'
		elif speed > 85:
			return 'BIG TICKET'

print caught_speeding(75, True)