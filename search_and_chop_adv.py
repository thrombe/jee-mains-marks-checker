
##############################
'''
##
functions defined
chopall(text , findthis)
chopstr(line , findthis[i])



##
text = list(open('./relative filepath' , 'r'))
findthis = [ [ 'start chop after' ,\
					 'end chop before' ,\
					  'where to chop from\
					  (ie. line/start/end)'\
					  'how many chars to search\
					   for(0for inf)']]


'''
##############################

if __name__ == '__main__':
	findthis = [ [ 'Question ID :</td><td class="bold">' , '<' , 'line' , 0 ] , [ 'Status :</td><td class="bold">' , '<' , 'end' , 0 ] , [ 'Chosen Option :</td><td class="bold">' , '<' , 'end' , 1000] , [ 'Given Answer :</td><td class="bold" style="word-break: break-word;">' , '<' , 'start' , 0 ] ]


	#open file in read mode
	text = open("/storage/emulated/0/0Python/jee txts/input mains1 marked answers.txt", "r")

##not req
#text = list(text)

##
#print(len(text))

	findthis = [ [ 'Question ID :</td><td class="bold">', '<', 'line', 0 ], [ 'Option 1 ID :</td><td class="bold">', '<', 'end', 200 ], [ 'Option 2 ID :</td><td class="bold">', '<', 'end', 200 ], [ 'Option 3 ID :</td><td class="bold">', '<', 'end', 200 ], [ 'Option 4 ID :</td><td class="bold">', '<', 'end', 400  ] ]




def chopstr(line , findthis ):
	
	searchfor = findthis[3]
	(findthis , chopat , startend) = (findthis[0] , findthis[1] , findthis[2])
	
	#next line outputs the character index from where the string starts and -1 if not there
	isitthere = line.find(findthis)
	
	
	########### wierd for findthis[0][0]
#	print('    isitthere- '+str(isitthere))
			
			
	
	if isitthere != -1 and (isitthere < searchfor or searchfor == 0):
				
		#correcting position of start chop
		isitthere = isitthere + int( len(findthis))
				
		#start chop
		chop = line[ isitthere : ]
		
		#set start, end only if chopping from main line
		if startend == 'line':
		
			#chopping line for further chops
			start = line[ : isitthere ]
			end = chop[chop.find(chopat) : ]
			
			
		#to avoid error
		else:
				#(start , end ) = (line , line)
				(start , end ) = ('no' , 'no')
			
		#end chop
		chop = chop[ : chop.find(chopat)]
		
		return (chop , start , end)
		
	else:
		return 'not found'

def chopall(text , findthis):
	
	#to avoid not defined error
	(line , start , end) = (None , None , None)
	out = []
	chopped = ''

	#repeat for every line
	for line in text:
		
		loop = line.count(findthis[0][0])
		
		####
		#print(loop)
		
		
		# loop+1 idk why, couldnt figure out
		for k in range(loop+1):
			
			##
			if chopped:
				#print(type(output))
				out.append(chopped)
				chopped = ''
			
			if end:
				line = end
		
			#repeating for every findthis
			for i in range(len(findthis)):
				
				#setting 'lines'
				if findthis[i][2] == 'line':
					lines = line
				elif findthis[i][2] == 'start':
					lines = start
				elif findthis[i][2] == 'end':
					lines = end
				
				#chopping
				output = chopstr(lines , findthis[i])
				
			#if not found, move to next line or continue
				if output == 'not found':
					if i == 0:
						
						##
						#print('not found break')
						break
					else:
						
						##
						#print('not found continue')
						continue
				
				#if found, setup for 'lines'
				if output[1] != 'no':
					(chop , start , end) = output
				else:
					chop = output[0]
					
				##
				if chopped:
					chopped = chopped +' '+ chop
				else:
					chopped = chop
				#print(chopped)
				
				
	#			if i == 0:
	#				print('\n')
	#			print(chop)
	#print(out)
	return out


if __name__ == '__main__':
	opt = chopall(text , findthis)
	print(opt)
	#print(len(opt))