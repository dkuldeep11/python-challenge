import re
import zipfile
zf = zipfile.ZipFile("channel.zip")

ans = []
id = '90052'
fname = id + '.txt'

#print zf.namelist()

while(True):
    data = zf.read(fname)
    #print data
    new_id = ''.join(re.findall(r'nothing is (\d*)', data))
    ans.append(zf.getinfo(fname).comment)
    #print new_id
    if new_id:
	fname = new_id + '.txt'
    else:
	print "solution = ", data
	break

#print ans

print ''.join(ans)
