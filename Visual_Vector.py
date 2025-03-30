#coding=gbk
from pathlib import Path
from tkinter import *
import pyglet
import sys

from log_formation import *
from coordsystem_setup import *

#------------------------Configure-----------------------

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

def init_tk(tk:Tk):
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

    canvas.create_rectangle(Width*0.7,0,Width*0.7,Height,width=3)

    c = CoordinateSystem(tk,canvas,Width,Height)

    return 0

def main():
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

    if init_tk(tk) == 1:
        return 1

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