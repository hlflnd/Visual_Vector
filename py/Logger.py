__enable=True

def enable_logger():
    global __enable
    __enable=True

def disable_logger():
    global __enable
    __enable=False

def Log(msg,endl='\n'):
    if __enable: print(f"\033[0m{msg}",end=endl)

def Warn(msg,endl='\n'):
    if __enable: print(f"\033[33m{msg}\033[0m",end=endl)

def Error(msg,endl='\n'):
    if __enable: print(f"\033[31m{msg}\033[0m",end=endl)

def Success(msg,endl='\n'):
    if __enable: print(f"\033[32m{msg}\033[0m",end=endl)