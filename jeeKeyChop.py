
if __name__ == '__main__':
	#PATH TO ANSWER KEY FILE
	text = list(open('/storage/emulated/0/0Python/jee txts/input mains1 answer key.txt', 'r'))



def keychop(text):

	findthis='uestionNo">'
	findthis2= 'nswer">'
	chopat = '<'
	
	outkey = []
	
	####out = open('/storage/emulated/0/0Python/jee txts/outputKey1.txt', 'w')
	
	
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
			####print(chop , file = out)
			#print(chop)
			outkey.append(chop)
	#print(outkey)
	return outkey



if __name__ == '__main__':
	print(keychop(text))