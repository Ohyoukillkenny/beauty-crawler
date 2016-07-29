#! usr/bin/python
__author__='Lingkun kong'

import re
import urllib2
from PIL import Image
num = 1
for i in range(1,30):
	i_new = i * 24
	#url from youdao
	url='http://image.youdao.com/search?q=%E9%9F%A9%E7%BA%A2&keyfrom=image.page'+str(i)+'&start='+str(i_new)
	html=urllib2.urlopen(url).read() 
	#print html
	regx='<img border=".*?" id=".*?" src="(.*?).jpg" width=".*?" height=".*?" sizew=".*?" sizeh=".*?" class="imgthumb"/>'
	pattern=re.compile(regx)
	links=re.findall(pattern,html)

	for link in links:
		link = link +'.jpg'
		print link + ' is ready'
		data=urllib2.urlopen(link).read()
		pic = open('/Users/ohyoukillkenny/Documents/interesting_python/img_ugly/'+str(num)+'.png','wb')
		pic.write(data)
		pic.close()
		img=Image.open('/Users/ohyoukillkenny/Documents/interesting_python/img_ugly/'+str(num)+'.png')
		img=img.resize((400,400))
		img.save('/Users/ohyoukillkenny/Documents/interesting_python/img_ugly/'+str(num)+'.png')
		num+=1