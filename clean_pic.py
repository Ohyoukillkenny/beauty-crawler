__author__='Lingkun Kong'
import re
from PIL import Image
num_open = 1
num_save = 1
for i in range(1,5669):
	try:
		img=Image.open('/Users/ohyoukillkenny/Documents/interesting_python/img_ugly/'+str(num_open)+'.png')
	except Exception, e:
		num_open = num_open + 1
		continue
	num_open = num_open + 1
	img.save('/Users/ohyoukillkenny/Documents/interesting_python/img_ugly/'+str(num_save)+'.png')
	print num_save,'is done'
	num_save=num_save + 1