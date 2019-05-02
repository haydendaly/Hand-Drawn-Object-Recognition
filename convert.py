class Functions:

	from PIL import Image
	import random
	#import numpy as np

	def convert():
		from PIL import Image
		img = Image.open("image.ps")
		img.save("image.png", "png")
		img = Image.open("image.png")
		img = img.resize((28,28))
		img.save("image.png")
		img = Image.open("image.png")
		#np_img = np.array(img)
		#np_img = np_img[:,:,0]
		#np_img = abs(np_img-255)

	def get_prediction():
	        item_list = ['drums', 'sun', 'laptop', 'book', 'traffic_light', 'wristwatch', 'wheel', 'shovel', 'cake', 'clock', 'broom', 'crown', 'cactus', 'car', 'bicycle', 'donut']
	        string_item = random.choice(item_list)
	        return string_item
