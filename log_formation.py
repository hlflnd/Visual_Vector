enable=True

def enable_logger():
    global enable
    enable=True

def disable_logger():
    global enable
    enable=False

def Log(msg,endl='\n'):
    if enable: print(f"\033[0m{msg}",end=endl)

def Warn(msg,endl='\n'):
    if enable: print(f"\033[33m{msg}\033[0m",end=endl)

def Error(msg,endl='\n'):
    if enable: print(f"\033[31m{msg}\033[0m",end=endl)

def Success(msg,endl='\n'):
    if enable: print(f"\033[32m{msg}\033[0m",end=endl)