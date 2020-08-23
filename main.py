import turtle 
my_turtle = turtle.Turtle()

my_turtle.speed(0)

def function(length,angle):
	for i in range(4):
		my_turtle.fd(length)
		my_turtle.right(angle)

for i in range(100):
	function(100,90)
	my_turtle.right(11)