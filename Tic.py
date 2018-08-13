import re 

pl1=0
pl2=1
x=0
y=0
game_over =0
print 'hello This is Tic Tac Toc'
a= [[' ','1','2','3'],
    ['1',' ',' ',' '],
    ['2',' ',' ',' '],
    ['3',' ',' ',' ']]
print a[0]
print a[1]
print a[2]
print a[3]
print '\n'

while game_over ==0:
	if pl1==1:
		print 'This is player A '
		print 'write X axsis'
		nb = input('Choose a number: ')
		x = int(nb)
		print 'write Y axsis'
		nb = input('Choose a number: ')
		y = int(nb)
		if a[x][y]!=' ':
			print 'the option is choosed'
			print a[0]
			print a[1]
			print a[2]
			print a[3]
			print '\n'

		else:
			a[x][y]='O'
			print a[0]
			print a[1]
			print a[2]
			print a[3]
			print '\n'
			pl1=0
			pl2=1


	elif pl2==1:
		print 'This is player B '
		print 'write X axsis'
		nb = input('Choose a number: ')
		x = int(nb)
		print 'write Y axsis'
		nb = input('Choose a number: ')
		y = int(nb)
		if a[x][y]!=' ':
			print 'the option is choosed'
			print a[0]
			print a[1]
			print a[2]
			print a[3]
			print '\n'
		else:
			a[x][y]='X'
			print a[0]
			print a[1]
			print a[2]
			print a[3]
			print '\n'
			pl1=1
			pl2=0

	if a[1][1] =='O' and a[1][2] =='O' and  a[1][3] =='O':
		game_over = 1
	elif a[2][1] =='O' and  a[2][2] =='O' and a[2][3] =='O':
		game_over = 1
	if a[3][1] =='O' and a[3][2] =='O' and a[3][3] =='O':
		game_over = 1
	elif a[1][1] =='O' and  a[1][2] =='O'and  a[1][3] =='O':
		game_over = 1
	if a[2][1] =='O'and a[2][2] =='O'and a[2][3] =='O':
		game_over = 1
	elif a[3][1] =='O' and a[3][2] =='O' and a[3][3] =='O':
		game_over = 1
	if a[1][1] =='O' and a[2][2] =='O'and a[3][3] =='O':
		game_over = 1
	elif a[3][1] =='O' and a[2][2] =='O' and a[1][3] =='O':
		game_over = 1

	if a[1][1] =='X' and a[1][2] =='X' and  a[1][3] =='X':
		game_over = 2
	elif a[2][1] =='x' and  a[2][2] =='X' and a[2][3] =='X':
		game_over = 2
	if a[3][1] =='O' and a[3][2] =='O' and a[3][3] =='O':
		game_over = 2
	elif a[1][1] =='X' and  a[1][2] =='X'and  a[1][3] =='X':
		game_over = 2
	if a[2][1] =='X' and a[2][2] =='X' and a[2][3] =='X':
		game_over = 2
	elif a[3][1] =='X' and a[3][2] =='X' and a[3][3] =='X':
		game_over = 2
	if a[1][1] =='X' and a[2][2] =='X' and a[3][3] =='X':
		game_over = 2
	elif a[3][1] =='X' and a[2][2] =='X' and a[1][3] =='X':
		game_over = 2

	if game_over ==1:
		print 'plyer A wine'
	elif game_over ==2:
		print 'player B wine'

	


			