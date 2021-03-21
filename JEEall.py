
from search_and_chop_adv import chopall
outfile, inputKey, inputFinalKey = '', '', ''

###########
#   OPTIONS
###########

# output file path (can comment this off for no file output)
outfile = open('./output/outputFinal.txt', 'w')

#PATH TO INPUT ANSWER KEY FILE (html code)
inputKey = list(open('./input/inputKey.txt', 'r'))

#PATH TO INPUT MARKED ANSWERS FILE (html code)
inputMy = list(open('./input/inputMy.txt', 'r'))

#PATH TO FINAL KEY FILE (keys from pdf)
#inputFinalKey = list(open('./input/inputFinalKey.txt', 'r'))

#PATH TO FINAL FINAL KEY FILE (keys from pdf)
#inputFinalKey = list(open('./input/inputFinalFinalKey.txt', 'r'))

############

if inputKey: # getting data out of the answer key html
	findthis = [ ['uestionNo">', '<', 'line', 0], [ 'nswer">', '<', 'end', 0] ]
	inputKey = chopall(inputKey, findthis)

findthis = [ [ 'Question ID :</td><td class="bold">', '<', 'line', 0 ], [ 'Status :</td><td class="bold">' , '<' , 'end' , 0 ] , [ 'Chosen Option :</td><td class="bold">' , '<' , 'end' , 1000] , [ 'Given Answer :</td><td class="bold" style="word-break: break-word;">' , '<' , 'start' , 0 ], [ 'Option 1 ID :</td><td class="bold">', '<', 'end', 200 ], [ 'Option 2 ID :</td><td class="bold">', '<', 'end', 200 ], [ 'Option 3 ID :</td><td class="bold">', '<', 'end', 200 ], [ 'Option 4 ID :</td><td class="bold">', '<', 'end', 400  ] ]
inputMy = chopall(inputMy, findthis) # getting data out of marked answers html

if inputFinalKey: # arranging data from a txt which has text copied from the final answer key pdf
	ans = inputFinalKey
	final = []
	for i in range(len(ans)):
		ans[i] = ans[i].strip('\n')
		ans[i] = ans[i].split(' ')
		if ans[i][1] == 'D':
			ans[i][1] = 'Drop'
		if ans[i][0].isdigit():
			final.append(ans[i])
	outputlist = []
	for i in range((len(final))):
		outputlist.append([final[i][0], final[i][1]])
	inputKey = outputlist

correctObj, correctInt, incorrectObj, incorrectInt, left, droppedObj, droppedInt, droppedButAttempted, num = 0, 0, 0, 0, -15, 0, 0, 0, 0
evaluate = {}
for my in inputMy:
	if my[2] == '1': my[2] = 'A' # convert 1234 to ABCD in My
	elif my[2] == '2': my[2] = 'B'
	elif my[2] == '3': my[2] = 'C'
	elif my[2] == '4': my[2] = 'D'
	for key in inputKey:
		if key[0] == my[0]: # append ABCD or integer to keys in Key
			key.append('integer')
			if key[1] == my[4]: key[2] = 'A'
			elif key[1] == my[5]: key[2] = 'B'
			elif key[1] == my[6]: key[2] = 'C'
			elif key[1] == my[7]: key[2] = 'D'
			
			if key[1] == 'Drop': # decide what happened to the questions
				if key[2] == 'integer': droppedInt += 1
				else: droppedObj += 1
				if my[2] != 'not found' or my[3] != 'not found': droppedButAttempted += 1
			elif my[1] == 'Not Answered': left += 1
			elif key[2] == my[2]: correctObj += 1
			elif key[1] == my[3]: correctInt += 1
			elif key[2] == 'integer': incorrectInt += 1
			elif key[2] != 'integer': incorrectObj += 1
			
			num += 1
			if key[2] == 'integer': key[2], key[1], my[2] = key[1], 'No key ID', 'NA'
			else: my[3] = 'NA'
			evaluate['Q'+str(num)] = { 'QID' : my[0], 'keyID' : key[1], 'key' : key[2], 'status' : my[1], 'markedObj' : my[2], 'markedInt' : my[3] }
			break
score = 4*(correctObj + correctInt + droppedButAttempted) + (-1)*incorrectObj

def printy(string): #define func to print to both file and stdrout
	if outfile: print(string, file = outfile)
	print(string)

for q, p in evaluate.items(): # printing all question details
	printy(q)
	for r in p.keys():
		printy(r + ': ' + p[r])
	printy('\n')

# print stats
printie = [ 'SCORE: '+str(score), 'CORRECT OBJ: '+str(correctObj), 'CORRECT INT: '+str(correctInt), 'INCORRECT OBJ: '+str(incorrectObj), 'INCORRECT INT: '+str(incorrectInt), 'LEFT: '+str(left), 'DROPPED OBJ: '+str(droppedObj), 'DROPPED INT: '+str(droppedInt), 'DROPPED BUT ATTEMPTED: '+str(droppedButAttempted) , 'dropped questions are added to score(if attempted) but not to "correct" or "incorrect" '  ]
for item in printie: printy(item)