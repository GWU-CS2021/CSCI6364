import cv2
import glob
import sys
import os
prefix = "c:\\ML-Project\\moeimouto-faces\\"
prefix_black = "c:\\ML-Project\\moeimouto-black\\"
prefix_grey = "c:\\ML-Project\\moeimouto-grey\\"

def save_grey(src = ""):
	img = cv2.imread(prefix+src)
	img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	border_v = 0
	border_h = 0
	if (1) >= (img.shape[0]/img.shape[1]):
	    border_v = int((((1)*img.shape[1])-img.shape[0])/2)
	else:
	    border_h = int((((1)*img.shape[0])-img.shape[1])/2)
	img = cv2.copyMakeBorder(img, border_v, border_v, border_h, border_h, cv2.BORDER_REPLICATE, 0)
	img = cv2.resize(img, (160, 160))
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_invert = cv2.bitwise_not(img_gray)
	img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
	final = cv2.divide(img_gray, 255 - img_smoothing, scale=256)
	f = cv2.bitwise_not(final)
	(thresh, blackAndWhiteImage) = cv2.threshold(f, 1, 255, cv2.THRESH_BINARY)
	black = cv2.bitwise_not(blackAndWhiteImage)
	grey_dir = prefix_grey + src
	black_dir = prefix_black + src

	if not os.path.exists(os.path.dirname(grey_dir)):
		# Create a new directory because it does not exist
		os.makedirs(os.path.dirname(grey_dir))


	if not os.path.exists(os.path.dirname(black_dir)):
		# Create a new directory because it does not exist
		os.makedirs(os.path.dirname(black_dir))

	cv2.imwrite(grey_dir, final)
	cv2.imwrite(black_dir, black)



def main():
	file_list = [str(pp.removeprefix(prefix)) for pp in glob.glob(r'c:\ML-Project\moeimouto-faces\000_hatsune_miku\*.png')]
	print(file_list)
	for file in file_list:
		save_grey(file)

if __name__ == '__main__':
	sys.exit(main())


