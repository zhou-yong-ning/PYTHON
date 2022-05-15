import os
from time import sleep

path = os.path.dirname(os.path.abspath(__file__))
# path =path.replace(）
print(path)
file = os.listdir(path)
print(file)
sleep(10)