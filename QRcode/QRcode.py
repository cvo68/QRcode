import qrcode

titulo = ('Meu primeiro qrcode')

img = qrcode.make(titulo)

img.save('C:/Users/cvo68/Pictures/Saved Pictures/qrcode.png')
