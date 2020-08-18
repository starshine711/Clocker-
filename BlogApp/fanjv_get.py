import requests
response = requests.get('https://api.catbk.cn/list?vmid=438061775&ps=21')
response.encoding='utf-8'
try:
	f=open('..\\static\\web\\fanjv.json','w',encoding='utf-8')
	f.write(response.text)
	f.close()
	print(response.text)
except:
	print('none')
input('...')