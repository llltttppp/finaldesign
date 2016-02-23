import sys
sys.path.append('J:\graduation design\mscoco\coco-caption-master\coco-caption-master')
from pycocotools.coco import COCO
from pycocoevalcap.eval import COCOEvalCap
import matplotlib.pyplot as plt
from PIL import Image
import pylab
pylab.rcParams['figure.figsize'] = (10.0, 8.0)

import json
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.3f')
dataDir='J:/graduation design/mscoco'
dataType='val2014'
annFile='%s/annotations/captions_%s.json'%(dataDir,dataType)
coco = COCO(annFile)

def readanns(i):
    imgId = coco.getImgIds()[i]
    annIds = coco.getAnnIds(imgIds=imgId)
    anns = coco.loadAnns(annIds)
    img =coco.loadImgs(imgId)[0]
    im = Image.open('J:/graduation design/mscoco/val2014/%s' %(img['file_name']))
    return anns