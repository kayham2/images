from PIL import Image, ImageFilter
img = Image.open('./astro.jpg')
img.thumbnail((400,400))

img.save('thumbnail.jpg')

print(img.size)
<<<<<<< HEAD
print('hell')
=======
print('hello')
>>>>>>> 53bb1531962d050772628832c78eaaf6897cba26
