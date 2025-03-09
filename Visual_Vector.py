#coding=gbk
from tkinter import *
import tkinter
import numpy as np
import math
import sys

from log_formation import *

#------------------------Configure-----------------------

#��������
Title = "Visual Vector"

#���ڿ�ȡ��߶�
Width = 1000
Height = 618

#����ʹ�õ�ͼ�꣬�ǵ�д��չ��.icoŶ��������ΪNone��
Icon = "./logo/wxyzlogo.ico"

#�Ƿ����������Ϣ
Log_enabled = True

#--------------------------------------------------------

def init_tk(tk:Tk): #��ʼ������
    try:
        tk.title(Title)
        if type(Title) is not str:
            Warn(f"���棺���ⲻΪstring����ǰΪ{type(Title)}����")
    except Exception as e:
        Error(repr(e))
        Error("������δ֪����")
        return 1
    Log(f"�ɹ����ñ��⣺{Title}��")

    try:
        tk.geometry(f"{Width}x{Height}")
    except TclError as e:
        Error(repr(e))
        Error(f"a.k.a.����Ĵ��ڴ�С��{Width}x{Height}��")
        return 1
    except Exception as e:
        Error(repr(e))
        Error("������δ֪����")
        return 1
    Log(f"�ɹ����ô��ڳ���{Width}x{Height}��")


    if Icon!=None:
        try:
            ico=Icon.split('/')[-1]
            tk.iconbitmap(Icon)
            if Icon[-3:]!="ico":
                Warn(f"���棺ͼ��{ico}��չ����Ϊ.ico����ǰΪ{Icon[-3:]}���������޷�������ʾ��")
        except TclError as e:
            Error(repr(e))
            Error(f"a.k.a.δ֪��·�����ļ���{Icon}")
            return 1
        except Exception as e:
            Error(repr(e))
            Error("������δ֪����")
            return 1
        Log(f"�ɹ�����ͼ�꣺{ico}��")
    else:
        Log("��������ͼ�꣺None��")

    return 0

def main():
    tk=Tk()

    if Log_enabled: enable_logger()
    else: disable_logger()

    if init_tk(tk) == 1:
        return 1

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