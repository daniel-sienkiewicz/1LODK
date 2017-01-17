class Base(object):
	def __init__(self, param):
		print "Base:", param
	
	def method(self, param):
		print "Base.method:", param

class Derived(Base):
	def __init__(self, param):
		super(Derived, self).__init__(param)
		print "Derived:", param

	def method(self, param):
		Base.method(self, param)
		print "Derived.method:", param

d = Derived("me")
d.method("you")
