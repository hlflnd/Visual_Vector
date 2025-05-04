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

#��������
Title = "Visual Vector"

#���ڿ�ȡ��߶�
Width = 2000
Height = int(Width * 0.618)

#����ʹ�õ�ͼ�꣬�ǵ�д��չ��.icoŶ��������ΪNone��
Icon = "./logo/wxyzlogo.ico"

#�Ƿ����������Ϣ
Log_enabled = True

#ʹ�õ�����
font_path = "Asana-Math.otf"

#--------------------------------------------------------

def init(tk:Tk):
	global Coords
	Log("���ڳ�ʼ����ʼ...")

	try:
		Log(f"�������⣺{Title}...")
		tk.title(Title)
		if type(Title) is not str:
			Warn(f"���棺���ⲻΪstring����ǰΪ{type(Title)}����")
	except Exception as e:
		Error(repr(e))
		Error("������δ֪����")
		return 1
	Success(f"�ɹ����ñ��⣺{Title}��")

	try:
		Log(f"�������ڣ�{Width}x{Height}...")
		tk.geometry(f"{Width}x{Height}")
	except TclError as e:
		Error(repr(e))
		Error(f"a.k.a.����Ĵ��ڴ�С��{Width}x{Height}��")
		return 1
	except Exception as e:
		Error(repr(e))
		Error("������δ֪����")
		return 1
	Success(f"�ɹ����ô��ڳ���{Width}x{Height}��")

	if Icon!=None:
		try:
			ico=Icon.split('/')[-1]
			Log(f"����ͼ�꣺{ico}...")
			tk.iconbitmap(Icon)
			if Icon[-3:]!="ico":
				Warn(f"���棺ͼ��{ico}��չ����Ϊ.ico����ǰΪ{Icon[-3:]}���������޷�������ʾ��")
		except TclError as e:
			Error(repr(e))
			Error(f"a.k.a.δ֪��·�����ļ���{Icon}��")
			return 1
		except Exception as e:
			Error(repr(e))
			Error("������δ֪����")
			return 1
		Success(f"�ɹ�����ͼ�꣺{ico}��")
	else:   
		Log("��������ͼ�꣺None��")

	tk.resizable(0,0)
	
	canvas = Canvas(tk,width=Width,height=Height)
	canvas.pack()

	Coords = CoordinateSystem(tk,canvas,Width,Height)
	
	return 0

def key_binding(tk:Tk):
	global Monix
	try:
		Log("��ȡ�����ļ�...")
		with open("options.json","r") as f:
			options = json.load(f)
		Success("��ȡ�����ļ��ɹ���")
	except FileNotFoundError as e:
		Error(repr(e))
		Error("a.k.a.δ�ҵ������ļ���")
		return 0
	except json.JSONDecodeError as e:
		Error(repr(e))
		Error("a.k.a.JSON��ʽ��Ч��")
		return 0

	try:
		Log("����������...")
		Monix = Monitor(tk,Coords.step,Coords)
		Monix.bind()

	except TclError as e:
		Error(repr(e))
		Error("a.k.a.�޶�Ӧ�����󶨡�")
		return 1
	except Exception as e:
		Error(repr(e))
		Error("������δ֪����")
		return 1
	Success("���������óɹ���")

	return 0
	

def main():
	Success(f"����Visual_Vector��ʼ���У�at {time.asctime()}")

	try:
		f = font_path.split('/')[-1]
		Log(f"�������壺{f}...")
		pyglet.options['win32_gdi_font']=True
		pyglet.font.add_file(str(Path(__file__).parent / font_path))
		pyglet.font.load(font_path)
		Success(f"�ɹ���������{f}��")
	except Exception as e:
		Error(repr(e))
		Error(f"a.k.a.��װ����{f}ʧ�ܣ�")
		Warn(f"��ʹ������{f}��")
	
	tk=Tk()
	
	if Log_enabled: enable_logger()
	else: disable_logger()

	if init(tk) == 1:
		return 1
	if key_binding(tk) == 1:
		return 1

	tk.update()
	tk.update_idletasks()

	Log("��ѭ����ʼ...")
	tk.mainloop()

	return 0

if __name__ == "__main__":
	status = main()

	if status==0:
		Success("���������")
	else:
		Error("�����쳣������")

	sys.exit(int(status==0))