from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
# img.thumbnail((400, 400))
# img.save('thumbnail.jpg')
# print(img.size)


 



# 1ST PART
# img = Image.open('./Pokedex/pikachu.jpg')

# filtered_img = img.convert('L')


# print(img)
# print(img.format)filtered_img = img.filter(ImageFilter.BLUR)
# print(img.size)
# print(dir(img))
# filtered_img.show()



# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)


# x = filtered_img.rotate(90)
# x.save("grey.png", 'png')
# filtered_img.save("grey.png", 'png')


# resize = filtered_img.resize((300, 300))
# resize.save("grey.png", "png")

# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save('grey.png', 'png')