import qrcode
enlace=input("Introduce la información para generar el qr: ")
img=qrcode.make(enlace)
nombreQR=input("Introduce el nombre para guardar el archivo png: ")
f=open(nombreQR+".png","wb")
img.save(f)
f.close()