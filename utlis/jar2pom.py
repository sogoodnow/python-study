import os

dir = "D:\workspace\WXQXW\WebContent\WEB-INF\lib"



if __name__ == '__main__':
    for p, d ,f in os.walk(dir):
        print("".join(f),end='\n')
