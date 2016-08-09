import sys
import math
import time
import os

clear_console = 'clear' if os.name == 'posix' else 'CLS'
width = 10
height = 20
screen = []

row_temp = []

for x in range(0,width):
	row_temp.append(0)
for y in range(0,height):
	screen.append(row_temp)

#extra row for bottom border
print screen
print "->"+str(screen[0][9])

# sys.exit(1)

def print_frame(screen):
	for y in range(0,height):
		for x in range(0,width):
			if screen[y][x] == 1:
				sys.stdout.write("#")
			else:
				sys.stdout.write(" ")
		sys.stdout.write("\n")

print "Tetris"

# outstr = ""
# for x in xrange(0,i):
# 	outstr += "\n"
# outstr += "#"
# i += 1

while True:
	os.system(clear_console)
	print_frame(screen)
	sys.stdout.flush()
	# print outstr
	time.sleep(0.5)

# testing pull request
