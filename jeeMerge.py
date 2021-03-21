#import time
#start = time.time()


from jeeMyChop import mychop
from jeeKeyChop import keychop
from search_and_chop_adv import chopstr, chopall
outfile = ''
inputkey = ''
inputFinalKey = ''

###########
#   OPTIONS
###########

# output file path
outfile = open('./output/outputFinal2.txt', 'w')

#PATH TO INPUT ANSWER KEY FILE
inputkey = list(open('./input/inputKey2.txt', 'r'))

#PATH TO INPUT MARKED ANSWERS FILE
inputmy = list(open('./input/inputMy2.txt', 'r'))

#PATH TO FINAL ANSWER KEY FILE
#inputFinalKey = list(open('./input/inputFinalKey.txt', 'r'))

#PATH TO FINAL FINAL KEY
#inputFinalKey = list(open('./input/inputFinalFinalKey.txt', 'r'))

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



#NOT FINAL KEY
if inputkey:
	key = keychop(inputkey)


#inputkey = ''.join(inputkey)
#for i in range(len(inputkey)):
    #inputkey[i] = inputkey[i].replace(' ', '')
    #inputkey[i] = inputkey[i].replace('\n', '')
#findthis = [ ['uestionNo">', '<', 'line', 0], [ 'nswer">', '<', 'end', 0] ]
#key = chopall(inputkey, findthis)
#print(key)
#print((inputkey))
#print(inputkey.count('uestionNo">'))

#FINAL KEY
if inputFinalKey:
	ans = inputFinalKey
	final = []
	for i in range(len(ans)):
		ans[i] = ans[i].strip('\n')
		ans[i] = ans[i].split(' ')
		if ans[i][1] == 'D':
			ans[i][1] = 'Drop'
		if ans[i][0].isdigit():
			final.append(ans[i])
	#print(len(final), '\n', final)
	outputlist = []
	for i in range((len(final))):
		outputlist.append(final[i][0]+' ans- '+final[i][1])
	#print(len(outputlist) , '\n' , outputlist)
	key = outputlist




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
dropped = 0
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
		
	elif evaluate[e][6] == 'Drop' :
			dropped += 1
	
	#print(type(evaluate[e][2]))

totalDrop = 0
for e in range(len(evaluate)):
	if evaluate[e][6] == 'Drop':
		totalDrop += 1
	
#print(evaluate)
print('\n'*4)
incorrectInt = str(75-left-correct-incorrectObj)
print('SCORE: '+str(score))
print('CORRECT: '+str(correct))
print('INCORRECT OBJECTIVE: '+str(incorrectObj))
print('INCORRECT INT TYPE: '+incorrectInt)
print('LEFT: '+str(left))
if totalDrop:
	print('TOTAL DROPPED QUESTIONS: '+str(totalDrop))
if dropped:
	print('ATTEMPTED BUT DROPPED: '+str(dropped)+'  idk if these would add to total score')

if outfile:
    print('\n'*4 , file = outfile)
    print('SCORE: '+str(score) , file = outfile)
    print('CORRECT: '+str(correct) , file = outfile)
    print('INCORRECT OBJECTIVE: '+str(incorrectObj) , file = outfile)
    print('INCORRECT INT TYPE: '+incorrectInt , file = outfile)
    print('LEFT: '+str(left) , file = outfile)
    if totalDrop:
    	print('TOTAL DROPPED QUESTIONS: '+str(totalDrop) , file = outfile)
    if dropped:
    	print('ATTEMPTED BUT DROPPED: '+str(dropped)+'  idk if these would add to total score' , file = outfile)
    

#print(str(time.time()-start))