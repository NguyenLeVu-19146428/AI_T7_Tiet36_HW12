import os
import glob
i = 1
for filename in glob.glob("*.jpg.jpg"):
    os.rename(filename,str(i) + ".jpg")
    i+=1