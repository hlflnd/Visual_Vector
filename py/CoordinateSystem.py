#coding=gbk
from tkinter import *

from py.Logger import *

class CoordinateSystem:
	def __init__(self,tk:Tk,canvas:Canvas,width:float,height:float,step:float=15.0):
		self.tk=tk
		self.canvas=canvas
		self.width=width*0.7
		self.height=height
		self.scale=1.0
		self.step=step

		self.canvas.config(highlightthickness=0,bd=0)

		try:
			Log("创建坐标系...")
			self.canvas.create_rectangle(0,0,self.width,self.height,fill="cyan")
			self.canvas.create_rectangle(self.width,0,width,self.height,fill="grey")
			canvas.create_rectangle(self.width,0,self.width,self.height,width=3)

			self.Xaxis = self.canvas.create_line(0,self.height/2,self.width,self.height/2,arrow=LAST,tags="BASIC")
			self.Yaxis = self.canvas.create_line(self.width/2,self.height,self.width/2,0,arrow=LAST,tags="BASIC")
			self.Origin = self.canvas.create_oval(self.width/2-2,self.height/2-2,self.width/2+2,self.height/2+2,fill="black",tags="BASIC")
		
		except Exception as e:
			Error(repr(e))
			Error("完啦！未知错误！")
			return 0

		Success("创建坐标系成功。")

	'''
	def translating(self,step:float,direction:str):
		match direction:
			case "left":
				self.canvas.move(self.Yaxis,-step,0)
				self.canvas.move(self.Origin,-step,0)
			case "right":
				self.canvas.move(self.Yaxis,step,0)
				self.canvas.move(self.Origin,step,0)
			case "up":
				self.canvas.move(self.Xaxis,0,step)
				self.canvas.move(self.Origin,0,step)
			case "down":
				self.canvas.move(self.Xaxis,0,-step)
				self.canvas.move(self.Origin,0,-step)
			case _:
				Error("参数错误：平移坐标系方向只能为{left,right,up,down}中的参数。")
	'''

	def translate_left(self,step):
		self.canvas.move(self.Yaxis,step,0)
		coordY = self.canvas.coords(self.Yaxis)
		if coordY[0] + coordY[2] > self.width * 2:
			self.canvas.tag_lower(self.Yaxis)
		if coordY[0] + coordY[2] < self.width * 2:
			self.canvas.tag_raise(self.Yaxis)

		self.canvas.move(self.Origin,step,0)
		coordO = self.canvas.coords(self.Origin)
		if coordO[0] + coordO[2] > self.width * 2:
			self.canvas.tag_lower(self.Origin)
		if coordO[0] + coordO[2] < self.width * 2:
			self.canvas.tag_raise(self.Origin)

		self.tk.update()

	'''	
	def translate_right(self,step):
		self.canvas.move(self.Yaxis,-step,0)
		self.canvas.move(self.Origin,-step,0)
		self.tk.update()
	
	def translate_up(self,step):
		self.canvas.move(self.Xaxis,0,-step)
		self.canvas.move(self.Origin,0,-step)
		self.tk.update()
	'''

	def translate_down(self,step):
		self.canvas.move(self.Xaxis,0,step)
		self.canvas.move(self.Origin,0,step)
		self.tk.update()
	
	def reunion(self,args=None):
		self.canvas.moveto(self.Xaxis,0,self.height/2)
		self.canvas.tag_raise(self.Yaxis)
		self.canvas.moveto(self.Yaxis,self.width/2,0)
		self.canvas.tag_raise(self.Origin)
		self.canvas.moveto(self.Origin,self.width/2,self.height/2)
		self.tk.update()

	def text_adjustion(self):
		pass

	'''
	def test(self,arg=None):
		Log("测试...")
		for i in range(100):
			self.translate_left(1)
			self.tk.update()
			time.sleep(0.01)
		for i in range(100):
			self.translate_right(1)
			self.tk.update()
			time.sleep(0.01)
		for i in range(100):
			self.translate_up(1)
			self.tk.update()
			time.sleep(0.01)
		for i in range(100):
			self.translate_down(1)
			self.tk.update()
			time.sleep(0.01)
		Log("测试完成。")
	'''