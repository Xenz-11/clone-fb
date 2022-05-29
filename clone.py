import os,sys
try:
        import requests
except ImportError:
        os.system('pip install requests')
try:
        import rich
except ImportError:
        os.system('pip install rich')
try:
        import bs4
except ImportError:
        os.system('pip install bs4')
os.system('git pull')
os.system('python clone.cython-easy-38.so')
