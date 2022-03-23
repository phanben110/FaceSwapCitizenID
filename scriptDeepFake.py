import pandas as pd  
import os 
import cv2
import tempfile 
from BEN_MattingMethod import robustMattingV1 as robust 
import numpy as np 

pathDataSet = 'privateTest' 
destination = "BENDriver.jpg" 

pathSources = os.listdir(pathDataSet) 
model = robust()
for i, pathImage in enumerate( pathSources ) : 
    #if i <=30:
    #    continue
    try: 
        os.mkdir(f"results2/{pathImage[:-4]}")
    except: 
        pass 
    #background = np.zeros(imgShape, dtype = "uint8")
    #alpha, matting = model.imageMatting(background,source) 
    #cv2.imwrite(f'results2/{pathImage[:-4]}/alpha.jpg', alpha)
    try:

        image = f'{pathDataSet}/{pathImage}' 
        source = cv2.imread(image)
        imgShape = source.shape 
        print ( f"python main.py --src '{destination}' --dst '{image}'  --out 'results2/{pathImage[:-4]}/Fake_{pathImage[:-4]}_{destination[:-4]}.png' --correct_color" )
        print ( i )
        os.system(f"python main.py --src '{destination}' --dst '{image}'  --out 'results2/{pathImage[:-4]}/Fake_{pathImage[:-4]}_{destination[:-4]}.png' --correct_color")
    #print ( pathImage )
    except: 
        print(f" fail case {i}")
        continue


    #print ( source.shape )
    #print ( background.shape )


