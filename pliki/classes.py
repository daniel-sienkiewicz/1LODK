class MyClass(object):
	"""A simple example class"""

	def __init__(self, anytext=""):
		self.i = 12345
		self._x = "private"
		self.anytext = anytext

	def f(self):
		return self.anytext

c = MyClass("text")
print c.i
c.i = 20
c.j = 30
print c.i, c.j
print c.f()
