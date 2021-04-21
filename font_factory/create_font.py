"""Create a font just from a combination of NMF dimensions.
Requires fontforge to be installed."""

import argparse,os,sys
sys.path.append(os.path.dirname(__file__))
from combine_to_svg_font import combine_to_svg_font
from svg_to_ttf import svg_to_ttf
from insert_alignment import insert_alignment
import time

def create_font(font_name,nmf_dims,nmf_save,out_folder):
    home_folder = os.path.join(out_folder,font_name)
    ttf_path = os.path.join(home_folder,font_name+".ttf")
    combine_to_svg_font(nmf_save,nmf_dims,home_folder,font_name)
    svg_to_ttf(os.path.join(home_folder,font_name+".svg"),ttf_path)
    insert_alignment(os.path.join(out_folder,font_name,"metadata.npy"),ttf_path,nmf_save)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Specify how to create the font')
    parser.add_argument("fontname",nargs='?',help="specify the fontname for your new font")
    parser.add_argument("--nmf_dims","-d",nargs='?',default="5,5,5",help="How to combine the nmf dimensions")
    parser.add_argument("--nmf_save","-s",nargs='?',default="font_factory/NMF_3_dim",help="In what folder are the NMF matricies stored?")
    #parser.add_argument("--orig_images","-i",nargs='?',default="new_images", help="Where are the original images for the NMF stored?")
    parser.add_argument("--out_folder","-o",nargs='?',default="example_fonts",help="Where to store your font?")
    args = parser.parse_args()
    create_font(args.fontname,args.nmf_dims.split(","),args.nmf_save,args.out_folder)