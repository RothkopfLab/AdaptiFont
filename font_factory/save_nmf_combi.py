import sys
import os
sys.path.append(os.path.dirname(__file__))
import numpy as np
from PIL import Image
from util.letters import letters,letter2folder,smalls
from util.util import load_letter_sizes,load_nmf

def gettable(spvals,H,shape):
    table = np.zeros_like(H[0])
    combino = [0 if i>=len(spvals) else float(spvals[i]) for i in range(len(H))]
    for i in range(len(combino)):
        table += H[i] * combino[i]
    cut = shape[0]*shape[1]
    im = table[:cut].reshape(shape)
    metadata = table[cut:]
    return im,metadata

def save_img(img_array,location):
    pillow_im = Image.fromarray(img_array.astype(np.uint8),"L")
    pillow_im.save(location)

def save_letters(table,nmf_path,out_path,letters,letter2folder):
    sizes = load_letter_sizes(os.path.join(nmf_path,"sizes.txt"))
    xpos = 0
    for char in letters:
        table_part = table[:,xpos:xpos+sizes[letter2folder[char]]]
        save_img(table_part,os.path.join(out_path,
                 ("_"+letter2folder[char] if letter2folder[char] in smalls else letter2folder[char])+".bmp"))
        xpos += sizes[letter2folder[char]]

def save_nmf_combi(out_path,NMF_save_folder,showvals,metadata_path,reverse_colors=True):
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    W,H, shape = load_nmf(NMF_save_folder)
    im,metadata = gettable(showvals,H,shape)
    im = im.clip(0,255)
    if reverse_colors:
        im = 255 - im
    save_letters(im,NMF_save_folder,out_path,letters,letter2folder)
    np.save(metadata_path,metadata)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        raise Exception("Provide the image folder path, the output folder path, the NMF save path, your dimension combination choice and the metadata path")
    save_nmf_combi(sys.argv[1], sys.argv[2], sys.argv[3].split(","),sys.argv[4])