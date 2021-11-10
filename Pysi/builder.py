import os
from wrapper import wrap

homeFile = open("./home/home.html")
homeContent = homeFile.read()
homeFile.close()

wrap("../index.html", homeContent)
