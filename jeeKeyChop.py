
if __name__ == '__main__':
	#PATH TO ANSWER KEY FILE
	text = list(open('./input/inputKey.txt', 'r'))



def keychop(text):

	findthis='uestionNo">'
	findthis2= 'nswer">'
	chopat = '<'
	
	outkey = []
	
	if __name__ == '__main__':
		out = open('./output/outputKey.txt', 'w')
	
	
	for line in text:
		
		#next line outputs the character number from where the string starts and -1 if not there
		isitthere = line.find(findthis)
		if isitthere != -1:
			isitthere = isitthere + int( len( findthis ) )
			
			#chopping out Q id
			chop = line[ isitthere : ]
			chop = chop[ : chop.find(chopat)]
			
			
			#the answers lie 2 lines ahead
	
		isitthere = line.find(findthis2)
		if isitthere != -1:
			isitthere = isitthere + int(len(findthis2))
					
					
			chop = chop+' ans- '+ line[ isitthere : ]
			chop=chop[ : chop.find(chopat) ]
			if __name__ == '__main__':
				print(chop , file = out)
			#print(chop)
			outkey.append(chop)
	#print(outkey)
	return outkey



if __name__ == '__main__':
	print(keychop(text))