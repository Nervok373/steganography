from PIL import Image, ImageDraw
import random
import os
import base64

f = open("key.key", "wb")
key = base64.urlsafe_b64encode(os.urandom(128))
f.write(key)
f.close()

random.seed(key)


def stega_encrypt():
    keys = []  # сюда будут помещены ключи
    img = Image.open(input("path to image: "))  # создаём объект изображения
    text = input("text here: ")  # текст (не должен начинатся с '&')
    text = text + "&&&"
    draw = ImageDraw.Draw(img)  # объект рисования
    width = img.size[0]  # ширина
    height = img.size[1]  # высота
    pix = img.load()  # все пиксели тут

    for elem in ([ord(elem) for elem in text]):
        ind = True
        while ind:
            key = (random.randint(1, width - 10), random.randint(1, height - 10))
            if not key in keys:
                keys.append(key)
                ind = False

        g, b = pix[key][1:3]
        draw.point(key, (elem, g, b))

    print('keys were written to the key.key file')
    img.save("cript_image.png", "PNG")
    f.close()


stega_encrypt()
