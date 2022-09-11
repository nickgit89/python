import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

print(os.name)
print("Item exists:", str(path.exists("textfile.txt")))
print("Item is a file", path.isfile("textfile.txt"))
print("Item is a folder", path.isdir("textfile.txt"))

print("Item's path:", path.realpath("textfile.txt"))
print("Item's path and name:", path.split(path.realpath("textfile.txt")))