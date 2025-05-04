#coding=gbk
from pathlib import Path
from tkinter import *
import pyglet
import json
import sys

from py.Monitor import *
from py.Logger import *
from py.CoordinateSystem import *

#----------------------configuration---------------------

#窗口名称
Title = "Visual Vector"

#窗口宽度、高度
Width = 2000
Height = int(Width * 0.618)

#窗口使用的图标，记得写拓展名.ico哦（若无则为None）
Icon = "./logo/wxyzlogo.ico"

#是否输出调试信息
Log_enabled = True

#使用的字体
font_path = "Asana-Math.otf"

#--------------------------------------------------------

def init(tk:Tk):
	global Coords
	Log("窗口初始化开始...")

	try:
		Log(f"创建标题：{Title}...")
		tk.title(Title)
		if type(Title) is not str:
			Warn(f"警告：标题不为string（当前为{type(Title)}）。")
	except Exception as e:
		Error(repr(e))
		Error("完啦！未知错误！")
		return 1
	Success(f"成功设置标题：{Title}。")

	try:
		Log(f"创建窗口：{Width}x{Height}...")
		tk.geometry(f"{Width}x{Height}")
	except TclError as e:
		Error(repr(e))
		Error(f"a.k.a.错误的窗口大小：{Width}x{Height}。")
		return 1
	except Exception as e:
		Error(repr(e))
		Error("完啦！未知错误！")
		return 1
	Success(f"成功设置窗口长宽：{Width}x{Height}。")

	if Icon!=None:
		try:
			ico=Icon.split('/')[-1]
			Log(f"创建图标：{ico}...")
			tk.iconbitmap(Icon)
			if Icon[-3:]!="ico":
				Warn(f"警告：图标{ico}拓展名不为.ico（当前为{Icon[-3:]}），可能无法正常显示。")
		except TclError as e:
			Error(repr(e))
			Error(f"a.k.a.未知的路径或文件：{Icon}。")
			return 1
		except Exception as e:
			Error(repr(e))
			Error("完啦！未知错误！")
			return 1
		Success(f"成功设置图标：{ico}。")
	else:   
		Log("无需设置图标：None。")

	tk.resizable(0,0)
	
	canvas = Canvas(tk,width=Width,height=Height)
	canvas.pack()

	Coords = CoordinateSystem(tk,canvas,Width,Height)
	
	return 0

def key_binding(tk:Tk):
	global Monix
	try:
		Log("读取设置文件...")
		with open("options.json","r") as f:
			options = json.load(f)
		Success("读取设置文件成功。")
	except FileNotFoundError as e:
		Error(repr(e))
		Error("a.k.a.未找到设置文件。")
		return 0
	except json.JSONDecodeError as e:
		Error(repr(e))
		Error("a.k.a.JSON格式无效。")
		return 0

	try:
		Log("启动按键绑定...")
		Monix = Monitor(tk,Coords.step,Coords)
		Monix.bind()

	except TclError as e:
		Error(repr(e))
		Error("a.k.a.无对应按键绑定。")
		return 1
	except Exception as e:
		Error(repr(e))
		Error("完啦！未知错误！")
		return 1
	Success("按键绑定设置成功。")

	return 0
	

def main():
	Success(f"程序Visual_Vector开始运行：at {time.asctime()}")

	try:
		f = font_path.split('/')[-1]
		Log(f"导入字体：{f}...")
		pyglet.options['win32_gdi_font']=True
		pyglet.font.add_file(str(Path(__file__).parent / font_path))
		pyglet.font.load(font_path)
		Success(f"成功导入字体{f}。")
	except Exception as e:
		Error(repr(e))
		Error(f"a.k.a.安装字体{f}失败！")
		Warn(f"不使用字体{f}。")
	
	tk=Tk()
	
	if Log_enabled: enable_logger()
	else: disable_logger()

	if init(tk) == 1:
		return 1
	if key_binding(tk) == 1:
		return 1

	tk.update()
	tk.update_idletasks()

	Log("主循环开始...")
	tk.mainloop()

	return 0

if __name__ == "__main__":
	status = main()

	if status==0:
		Success("程序结束。")
	else:
		Error("程序异常结束。")

	sys.exit(int(status==0))