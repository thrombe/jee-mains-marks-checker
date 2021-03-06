
from jeeMyChop import mychop
from jeeKeyChop import keychop
from search_and_chop_adv import chopstr, chopall
outfile = ''

###########
#   OPTIONS
###########

# output file path
outfile = open('./output/outputFinal.txt', 'w')

#PATH TO INPUT ANSWER KEY FILE
inputkey = list(open('./input/inputKey.txt', 'r'))

#PATH TO INPUT MARKED ANSWERS FILE
inputmy = list(open('./input/inputMy.txt', 'r'))


##############
#   IGNORE
##############

#PATH TO MARKED ANSWWRS FILE
#marked = open('./jee txts/outputMyAnswers1.txt' , 'r')
#marked = list(marked)

#PATH O CORRECT ANSWERS FILE
#key = open('./jee txts/outputKey1.txt' , 'r')
#key = list(key)

###########################

evaluate = []
score = 0

findthis = [ [ 'Question ID :</td><td class="bold">', '<', 'line', 0 ], [ 'Option 1 ID :</td><td class="bold">', '<', 'end', 200 ], [ 'Option 2 ID :</td><td class="bold">', '<', 'end', 200 ], [ 'Option 3 ID :</td><td class="bold">', '<', 'end', 200 ], [ 'Option 4 ID :</td><td class="bold">', '<', 'end', 400  ] ]

options = chopall(inputmy, findthis)

for i in range(len(options)):
	options[i] = options[i].split(' ')


key = keychop(inputkey)
marked = mychop(inputmy)

###
for k in range(len(key)):
	key[k] = key[k].split(' ans- ')
	
	for o in range(len(options)):
		#print(len(options))
		if key[k][0] == options[o][0]:
			try:
				if key[k][1] == options[o][1]:
					key[k][1] = 'A'
				if key[k][1] == options[o][2]:
					key[k][1] = 'B'
				if key[k][1] == options[o][3]:
					key[k][1] = 'C'
				if key[k][1] == options[o][4]:
					key[k][1] = 'D'
			except:
				pass
		
	key[k] = key[k][0]+' ans: '+key[k][1]
#print(options)
#print(key)

#print(marked)

for line in marked:
	chopM = line[ : line.find(' ')]
	endM = line[line.find(' ') : ]
	
	
	for line2 in key:
		
		chopK = line2[ : line2.find(' ')]
		endK = line2[line2.find(' ') : ]

		if chopM == chopK:
			
			if outfile:
				print(chopK+'\n'+'marked:'+endM+'\n'+'key:'+endK+'\n' , file=outfile)
			
			print(chopK+'\n'+'marked:'+endM+'\n'+'key:'+endK+'\n')
			evaluate.append(chopK+' '+'marked:'+endM+' '+'key:'+endK)


############
correct = 0
incorrectObj = 0
left = -15
incorrectInt = 0
for e in range(len(evaluate)):
	#print(len(evaluate))
	#print(evaluate[e])
	evaluate[e] = evaluate[e].split(' ')
	if evaluate[e][2] == 'Not':
		left += 1
	elif evaluate[e][3] == evaluate[e][6]:
		score += 4
		correct += 1
	elif evaluate[e][3] != evaluate[e][6] and (evaluate[e][6] == 'A' or evaluate[e][6] == 'B' or evaluate[e][6] == 'C' or evaluate[e][6] == 'D'):
		score += -1
		incorrectObj += 1
	#print(type(evaluate[e][2]))
	
#print(evaluate)
print('\n'*4)
incorrectInt = str(75-left-correct-incorrectObj)
print('SCORE: '+str(score))
print('CORRECT: '+str(correct))
print('INCORRECT OBJECTIVE: '+str(incorrectObj))
print('INCORRECT INT TYPE: '+incorrectInt)
print('LEFT: '+str(left))