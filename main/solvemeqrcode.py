import qrtools
from PIL import Image
import requests

cookie = {"sid":"h9se1d6mg468tq8nreioqceldi7fda043b58fnr8k7k9098rkeb1"}
r = requests.get("http://solveme.kr/probs/13/94e613b1bafd90cbbf53ee24452b35d8/",cookies=cookie)
b64img = r.content.split("<")[12].split(",")[1].replace('" alt="QR Code">\r\n\t','')
f = open("qrcode.png","wb")
f.write(b64img.decode("base64"))
f.close()
r.close()

img = Image.open("qrcode.png",'r')
size = img.size
img2 = Image.new('RGBA',(int(size[0])-92,int(size[0])-92))
pix = img.load()
pix2 = img2.load()
x,y = 0,0
for j in range(size[0]):
    for i in range(size[0]):
        if pix[i,j][3] == 255:
            pix2[x,y] = pix[i,j]
            x+=1
    if pix[0,j][3] == 255:
        y+=1
    x=0
img2.save("code.png")

qr = qrtools.QR()
qr.decode("code.png")
print qr.data

r2 = requests.post('http://solveme.kr/probs/13/94e613b1bafd90cbbf53ee24452b35d8/',cookies=cookie,data={'answer':qr.data})
print r2.content
        
