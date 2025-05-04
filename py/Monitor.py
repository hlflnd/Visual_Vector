from tkinter import *
import time

from py import CoordinateSystem
from py.Logger import *

class Monitor:
	def __init__(self,tk:Tk,step:float,cs:CoordinateSystem):
		self.tk=tk
		self.mouse_pressed = False
		self.mouse_x = 0.0
		self.mouse_y = 0.0
		self.step=step
		self.cs = cs
		self.deltatime=time.time()

	def bind(self):
		self.tk.bind("<Motion>",self.on_mouse_move)
		self.tk.bind("<ButtonPress>",self.on_left_press)
		self.tk.bind("<ButtonRelease>",self.on_left_release)
		self.tk.bind("<KeyPress-r>",self.cs.reunion)

	def on_mouse_move(self,event):
		#Log("Motion.")
		if self.mouse_pressed and time.time() - self.deltatime > 0.005:
			#Log("Pressed motion.")
			dx = event.x - self.mouse_x
			dy = event.y - self.mouse_y
			self.cs.translate_left(self.step*dx/(dx*dx+dy*dy)**0.5)
			self.cs.translate_down(self.step*dy/(dx*dx+dy*dy)**0.5)
			self.deltatime = time.time()

		self.mouse_x = event.x
		self.mouse_y = event.y

	def on_left_press(self,event):
		if event.num == 1:
			self.mouse_pressed = True
		#Log("Pressed.")

	def on_left_release(self,event):
		if event.num == 1:
			self.mouse_pressed = False
		#Log("Released.")