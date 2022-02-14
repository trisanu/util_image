from PIL import Image, ImageEnhance
import os
import tkinter as tk
from tkinter import filedialog as fd


class Opxn_AdjImageDim:
	CNST_cmfrompixel = 2.54/144
	CNST_allwdformat = ['.jpg', '.png',]


	def __init__(self,inppath,
	             reqwidth: float = None,
	             reqheigth: float = None,
	             ):
		self.inppath = inppath
		self.inpimgpil = Image.open(self.inpimgpath)
		self.reqwidthcm = reqwidth
		self.reqheigthcm = reqheigth
		self.outimgpil = self.pilRredimension_bypxl()


	@property
	def inpimgpath(self):
		if not str.lower(os.path.splitext(self.inppath)[1]) in self.CNST_allwdformat:
			raise ValueError("Please select images in formats jpg or png")
		else:
			return self.inppath

	@property
	def outimgname(self):
		_fname,_extn = os.path.splitext(os.path.basename(self.inpimgpath))
		return "".join(["".join([_fname,"_RESIZED"]),_extn])

	@property
	def outimgpath(self):
		return os.path.join(os.path.dirname(self.inppath),self.outimgname)

	def pilRredimension_bycm(self):
		self.enhance_image(n = 1.5)
		_outhgt_Pxl = int(1 / self.CNST_cmfrompixel * self.reqheigthcm)
		_outwid_Pxl = int(1 / self.CNST_cmfrompixel * self.reqwidthcm)
		revise_cms = (_outwid_Pxl ,  _outhgt_Pxl)
		self.inpimgpil = self.inpimgpil.convert('RGB')
		revise_img = self.inpimgpil.resize(size = revise_cms)
		return revise_img

	def pilRredimension_bypxl(self):
		self.enhance_image(n = 1.5)
		_outhgt_Pxl = int(self.reqheigthcm)
		_outwid_Pxl = int(self.reqwidthcm)
		revise_cms = (_outwid_Pxl ,  _outhgt_Pxl)
		self.inpimgpil = self.inpimgpil.convert('RGB')
		revise_img = self.inpimgpil.resize(size = revise_cms)
		return revise_img

	def enhance_image(self,n):
		self.inpimgpil = ImageEnhance.Brightness(self.inpimgpil)
		self.inpimgpil = self.inpimgpil.enhance(n)
		self.inpimgpil = ImageEnhance.Contrast(self.inpimgpil)
		self.inpimgpil = self.inpimgpil.enhance(n)
		self.inpimgpil = ImageEnhance.Sharpness(self.inpimgpil)
		self.inpimgpil = self.inpimgpil.enhance(n)
		self.inpimgpil = ImageEnhance.Color(self.inpimgpil)
		self.inpimgpil = self.inpimgpil.enhance(n)


	def write_pil(self):
		self.outimgpil.save(self.outimgpath , dpi = (144 , 144))



if __name__ == "__main__":
	root = tk.Tk()
	inppath = fd.askopenfilename()
	app = Opxn_AdjImageDim(inppath,
	                       reqwidth = 125 ,
	                       reqheigth = 150 ,
	                       )
	app.write_pil()
	root.destroy()
	root.quit()
