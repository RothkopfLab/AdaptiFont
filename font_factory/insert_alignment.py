import os,sys
sys.path.append(os.path.dirname(__file__))
import numpy as np
from util.letters import letters,letter2folder
from fontTools.ttLib.ttFont import TTFont

def align_glyph(hmtx,glyf,char,meta,vert_min,scaling):
    if "coordinates" not in glyf[char].__dict__:
        #print(f"WARNING, letter without paths {char}")
        return
    coords = glyf[char].coordinates._a
    realwidth = glyf[char].xMax-glyf[char].xMin
    realheight = glyf[char].yMax-glyf[char].yMin
    pad_left = meta["pad_left"]*scaling
    verschieb_x = pad_left-hmtx[char][1]
    new_width = meta["pad_right"]*scaling+max(coords[::2])+verschieb_x
    hmtx[char]=(max(0,int(new_width)),max(0,int(pad_left)))
    verschieb_y = meta["pad_bottom"]*scaling+vert_min-min(coords[1::2])
    for i in range(len(coords)):
        if i%2==0:
            coords[i]+=int(verschieb_x)
        else:
            coords[i]+=int(verschieb_y)
    

def insert_alignment(metadata_path,ttf_path,NMF_save):
    with open(os.path.join(NMF_save,"NN.txt"),"r") as f:
        NN=float(f.read())
    meta = np.load(metadata_path)
    meta-=NN
    font = TTFont(ttf_path)
    hmtx = font.get('hmtx')
    glyf = font.get('glyf')
    head = font.get("head")
    scaling = head.unitsPerEm
    hhea = font.get("hhea")
    hhea.ascent=int(meta[0]*scaling)
    hhea.descent = 0
    hmtx["space"] = (max(0,int(meta[1]*scaling)),0)
    i = 2
    for char in [letter2folder[l] for l in letters]:
        char_meta = {"pad_right":meta[i],
                     "pad_bottom":meta[i+1],
                     "pad_left":meta[i+2]}
        align_glyph(hmtx,glyf,char,char_meta,hhea.descent,scaling)
        i+=3
    font.save(ttf_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Provide the ttf file path")
    insert_alignment("",sys.argv[1])