#checks the nta site for updates, like result. and stores the info in a file to compare to when you check next time.
#link is https://ntaresults.nic.in/NTARESULTS_CMS/Page/Page?PageId=1&LangId=P


#pip install httplib2
#pip install beautifulsoup4

import httplib2
#from bs4 import BeautifulSoup
from search_and_chop import chop



out = str(list(open('./check.txt' , 'r'))[0])
out = out.split('%%%%%')
#print(out)

resp, content = httplib2.Http().request("https://ntaresults.nic.in/NTARESULTS_CMS/Page/Page?PageId=1&LangId=P")
#content = BeautifulSoup(content , 'html.parser')
#print(content.prettify())
#print(resp)    #theres some good info in there


#getting potentially useful stuff out of the content
content = chop((str(content)) , 'target="_blank">' , '<')

#throwing away blank values
new = []
for i in content:
	if i:
		new.append(i)
#print(new)

#now compare both lists
changed = ''
for i in range(len(out)):
	if out[i] != new[i]:
		changed = 'yes'
	else:
		pass

#if any of the items is changed, print yes
if changed:
	print('yes' + '\n')
	pass
else:
	print('no'+'\n')
print(new)

#printing output to a file in specific format
fin = ''
out = open('./check.txt' , 'w')
for i in new:
	if i:
		fin = fin +'%%%%%'+i
		
print(fin[5 : ] , end = '' , file = out)