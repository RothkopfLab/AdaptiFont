import os
import sys
sys.path.append(os.path.dirname(__file__))
from save_nmf_combi import save_nmf_combi
from letters_to_font import letters_to_font
from convert_bmp_to_svg import bmp_to_svg

def combine_to_svg_font(NMF_save_folder,showvals,out_folder,font_name):
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    bmp_path = os.path.join(out_folder,"bmp")
    svg_path = os.path.join(out_folder,"svg")
    font_path = os.path.join(out_folder,font_name+".svg")
    metadata_path = os.path.join(out_folder,"metadata.npy")
    save_nmf_combi(bmp_path,NMF_save_folder,showvals,metadata_path)
    bmp_to_svg(bmp_path,svg_path)
    letters_to_font(svg_path,font_path,font_name)

if __name__ == "__main__":
    if len(sys.argv) < 5:
        raise Exception("Provide the NMF save folder, the NMF dimension combination, the original image folder, the output directory, and the new font name")
    combine_to_svg_font(sys.argv[1], sys.argv[2],sys.argv[3].split(","),sys.argv[4])