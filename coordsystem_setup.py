#coding=gbk
from tkinter import *

from log_formation import *

class CoordinateSystem:
    def __init__(self,tk:Tk,canvas:Canvas,width:float,height:float):
        self.tk=tk
        self.canvas=canvas
        self.width=width*0.7
        self.height=height
        try:
            Log("创建坐标系...")
            self.canvas.create_rectangle(0,0,self.width,self.height,fill="cyan")
        except Exception as e:
            Error(repr(e))
            Error("完啦！未知错误！")
            return 0
        Success("创建坐标系成功。")

        self.Xaxis = (
            self.canvas.create_line(0,self.height/2,self.width,self.height/2,arrow=LAST),
            self.canvas.create_text(self.width-10,self.height/2+5,text="x",font=("Asana Math",10))
        )

        self.Yaxis = (
            self.canvas.create_line(self.width/2,self.height,self.width/2,0,arrow=LAST),
            self.canvas.create_text(self.width/2+15,3,text="y",font=("Asana Math",10))
        )

        self.Origin = (
            self.canvas.create_oval(self.width/2-3,self.height/2-3,self.width/2+3,self.height/2+3,fill="black"),
            self.canvas.create_text(self.width/2+13,self.height/2+7,text='O',font=("Asana Math",10))
        )
        
        

        
