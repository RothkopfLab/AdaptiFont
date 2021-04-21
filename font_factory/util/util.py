import os,sys
from PIL import Image
import numpy as np
sys.path.append(os.path.dirname(__file__))
from letters import letters,letter2folder

def load_nmf(folder):
    W = np.load(folder+"/W.npy")
    H = np.load(folder+"/H.npy")
    shape = np.load(folder+"/shape.npy")
    return W,H,shape

def load_letter_sizes(path):
    with open(path,"r") as f:
        lines = f.read().splitlines()
        if lines[-1]=="":
            lines = lines[:-1]
    sizes = {x.split(":")[0]:int(x.split(":")[1]) for x in lines}
    return sizes