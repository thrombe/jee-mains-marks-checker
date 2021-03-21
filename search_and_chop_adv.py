
##############################
'''
##
functions defined                 #text can be string or list
chopall(text , findthis)         #uses chopstr to chop and then integrate stuff
chopstr(line , findthis[i])     #chops required strings out of single lines

##
text = list(open('./relative filepath' , 'r'))
findthis = [ [ 'start chop after', 'end chop before', 'where to chop from(ie. line/start/end)', 'how many chars to search for (0 for inf)']]
	# NOTE - findthis can have just 1 search string ie, findthis can be findthis[i]
'''
##############################

#findthis is findthis[i]
def chopstr(line, start, end, findthis):
	searchfor = findthis[3] #how many chars ahead to seach the string for
	findthis, chopat, startend = findthis[0], findthis[1], findthis[2]
	if startend == 'end': line = end
	elif startend == 'start': line = start
	
	isitthere = line.find(findthis) # outputs the character index from where the string starts and -1 if not there
	if isitthere != -1 and (isitthere < searchfor or searchfor == 0):
		isitthere = isitthere + int( len(findthis)) #correcting position of start chop
		chop = line[ isitthere : ] #start chop
		if startend == 'line': #set start, end only if chopping from main line
			start = line[ : isitthere ] #chopping line for further chops
			end = chop[chop.find(chopat) : ]
		chop = chop[ : chop.find(chopat)] #end chop
		return chop , start , end
	else: return 'not found', start, end

def chopall(text, findthis):
	if type(findthis[0]) == type('string'):
	    multiChop = 'no'
	    lis = []
	    lis.append(findthis)
	    findthis = lis # if only searching for 1 type of string, adjust the data structure
	else: multiChop = 'yes'
	line, start, end, out, chopped = '', '', '', [], [] #to avoid not defined error
	if type(text) == type([]): text = ''.join(text).replace('\n', '')
	elif type(text) == type('string'): text = text.replace('\n', '')
	howMany = text.count(findthis[0][0])
	for _ in range(howMany):
		for i, _ in enumerate(findthis):
			chop, start, end = chopstr(text, start, end, findthis[i])
			chopped.append(chop)
			if i == 0: text = end
		if multiChop == 'yes':
			out.append(chopped)
			chopped = []
	if multiChop == 'no': out  = chopped
	return out
		

if __name__ == '__main__':
	findthis = [ [ 'Question ID :</td><td class="bold">' , '<' , 'line' , 0 ] , [ 'Status :</td><td class="bold">' , '<' , 'end' , 0 ] , [ 'Chosen Option :</td><td class="bold">' , '<' , 'end' , 1000] , [ 'Given Answer :</td><td class="bold" style="word-break: break-word;">' , '<' , 'start' , 0 ] ]
#	findthis =  [ 'Question ID :</td><td class="bold">' , '<' , 'line' , 0 ] #, [ 'Status :</td><td class="bold">' , '<' , 'end' , 0 ] , [ 'Chosen Option :</td><td class="bold">' , '<' , 'end' , 1000] , [ 'Given Answer :</td><td class="bold" style="word-break: break-word;">' , '<' , 'start' , 0 ] ]
#	findthis = [ ['uestionNo">', '<', 'line', 0], [ 'nswer">', '<', 'end', 0] ]
#	findthis = ['uestionNo">', '<', 'line', 0]
	text = open('/storage/emulated/0/0Python/Git/jee-mains-marks-checker/input/inputMy2.txt', "r")
#	text = open('/storage/emulated/0/0Python/Git/jee-mains-marks-checker/input/inputKey2.txt', "r")
	text = list(text)##
#	print(' '.join(list(text)).replace(' ', '').count(findthis[2][0].replace(' ', '')))##
#	print(text)##
#	print(len(text))##
	opt = chopall(text , findthis)
	print(opt)
	print(len(opt))