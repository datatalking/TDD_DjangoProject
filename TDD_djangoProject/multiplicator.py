# SOURCE Test-Driven Development with Django by Packt Publishing Kevin Harvey
# FILENAME multiplicator

def multiplicator1(x, y):
	i = 0
	result = 0
	while i < x:
		result += y
		i += 1
		return result
	
	assert multiplicator1(2, 3) == 6


def multiplicator(x, y):
	return x * y

assert multiplicator(2, 3) == 6

"""
An example of red/green/refactor

The smallest cycle of TDD typically involves three steps
1. Writing a test that fails(red)
2. Doing whatever is necessary to get that test to pass (green)
3. Optimizing to fix any subpar code you may have introduced to get the test to pass (refactor)

Notes:
In the future we will add
Version Control, Documentation, Testing and Continuous Integration
A good primer on git is  http://git-scm.com/doc. but we use PyCharm so it makes it easy.

Benefits:
Bug stay fixed
Teams work better
Always write testable code
TDD forces stability into code
Take bigger risks with code
Scale up to be professional coder quicker
"""