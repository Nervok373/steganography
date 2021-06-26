from PIL import Image
import random

f = open("key.key", "rb")
key = f.read()
f.close()

random.seed(key)

def stega_decrypt():
	decript_message = []
	end_text = 0
	try:
		img = Image.open(input("path to image: "))
	except:
		return "error: failed"

	width = img.size[0]  # ширина
	height = img.size[1]  # высота
	pix = img.load()

	go_to_text = True
	while go_to_text:
		key = (random.randint(1, width - 10), random.randint(1, height - 10))
		letter = pix[tuple(key)][0]
		decript_message.append(letter)
		if chr(letter) == "&":
			end_text += 1
			if end_text == 3:
				go_to_text = False

	decript_message = ''.join([chr(elem) for elem in decript_message])
	return decript_message[:-3]


print("you message: ", stega_decrypt())