from PIL import Image
merei = Image.open('merei.png')
Korea = Image.open('unist.jpeg')
Korea.paste(merei,(0,0), merei)
Korea.save('in unist.jpg')
