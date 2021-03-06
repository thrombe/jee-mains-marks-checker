
if __name__ == '__main__':
	#PATH TO MARKED ANSWERS FILE
	text = list(open('./input/inputMy.txt', 'r'))
	

def mychop(text):
	
	#output in file
	out = open('./output/outputMy.txt', 'w')
	
	#question id
	findthis='Question ID :</td><td class="bold">'
	
	#answered
	findthis2= 'Status :</td><td class="bold">'
	
	#chosen
	findthis3 = 'Chosen Option :</td><td class="bold">'
	
	#integer type
	findthis4 = 'Given Answer :</td><td class="bold" style="word-break: break-word;">'
	
	
	chopat = '<'
	
	outmy = []
	
	
	for linee in text:
		found = True
		
		
		#go through same line multiple times
		end = linee
		while found:
			
			line = end
			chop2 = ''
			chop3 = ''
			chop4 = ''
		
			#next line outputs the character number from where the string starts and -1 if not there
			isitthere = line.find(findthis)
			if isitthere == -1:
				found = False
			else:
				isitthere = isitthere + int( len( findthis ) )
				start = line[ : isitthere ]
				chop = line[ isitthere : ]
				chop = chop[ : chop.find(chopat)]
				end = line[isitthere+int(len(chop)) : ]
			
			
				isitthere = end.find(findthis2)
				if isitthere != -1:
					isitthere = isitthere + int( len( findthis2 ) )
					chop2 = end[ isitthere : ]
					chop2 = chop2[ : chop2.find(chopat)]
				
				if chop2 == 'Not Answered':
	####				print(chop+' '+chop2, file = out)
					#print(chop+' '+chop2)
					outmy.append(chop+' '+chop2)
					continue
				
			
				isitthere = end.find(findthis3)
				if isitthere != -1:
					isitthere = isitthere + int( len( findthis3 ) )
					chop3 = end[ isitthere : ]
					chop3 = chop3[ : chop3.find(chopat)]
					
					
			#A B C D are mentioned as 1 2 3 4 in the answer
					chop3 = int(chop3)
					if chop3 == 1:
						chop3 = 'A'
					elif chop3 == 2:
						chop3 = 'B'
					elif chop3 == 3:
						chop3 = 'C'
					elif chop3 == 4:
						chop3 = 'D'
			
			
				isitthere = start.find(findthis4)
				if isitthere != -1:
					isitthere = isitthere + int( len( findthis4 ) )
					chop4 = start[ isitthere : ]
					chop4 = chop4[ : chop4.find(chopat)]
				
	
				if chop and chop2 and chop4:
					#print(chop+' '+chop2+' '+chop4)
					outmy.append(chop+' '+chop2+' '+chop4)
				elif chop and chop2 and chop3:
					#print(chop+' '+chop2+' '+chop3)
					outmy.append(chop+' '+chop2+' '+chop3)

				if __name__ == '__main__':
					if chop and chop2 and chop4:
						print(chop+' '+chop2+' '+chop4 , file = out)
						print(chop+' '+chop2+' '+chop4)
					elif chop and chop2 and chop3:
						print(chop+' '+chop2+' '+chop3 , file = out)
						print(chop+' '+chop2+' '+chop3)
	
	return outmy


if __name__ == '__main__':
	print(mychop(text))