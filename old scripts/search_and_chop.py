####################
'''
##
defined functions #text is a list or string'
chop(text , findthis , chopat)




##
findthis = 'string'
text = list(open('./relative filepath' , 'r'))
chopat = 'string'

'''
####################

if __name__ == '__main__':
	#options
	findthis='Question ID :</td><td class="bold">'
	chopat = '<'


	#open file in read mode
	text = open("./jee txts/input mains1 marked answers.txt", "r")



#defining chop() function
def chop(text , findthis , chopat ):
	
	if type(text) == type('string'):
		list = []
		list.append(text)
		text = list
	
	out = []
	
	for line in text:
		
		#finding out how many times 'findthis' appears in a single line
		howmany  = line.count(findthis)
		
		#looping for multiple passes through same line
		for i in range(howmany):
		
			#next line outputs the character number from where the string starts and -1 if not there
			isitthere = line.find(findthis)
			
			if isitthere != -1:
				
				#correcting position of start chop
				isitthere = isitthere + int( len( findthis ) )
				
				#start chop
				chop = line[ isitthere : ]
				
				#chopping line for 'howmany' loop
				line = chop[chop.find(chopat) : ]
				
				#end chop
				chop = chop[ : chop.find(chopat)]
				
				
				out.append(chop)
				#print(chop)
				#print(chop , file = 'filepath' )
				#print(out)
	return out

if __name__ == '__main__':
	#calling chop()
	print(chop(text , findthis , chopat ))