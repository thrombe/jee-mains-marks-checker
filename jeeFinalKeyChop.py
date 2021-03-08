inputFinalKey = list(open('./jee txts/input mains1 final key.txt', 'r'))
outFile = open('./jee txts/outputKeyFinal1.txt' , 'w')

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