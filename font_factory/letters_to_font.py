import os,sys,re

def letters_to_font(in_dir,out_file,font_name):
    base_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(base_path,"svg_embedding.svg"),"r") as f:
        svg_embedding = f.read()
    svgs = [os.path.join(in_dir,x) for x in os.listdir(in_dir)]

    glyphs = ['<glyph glyph-name="space" unicode=" " horiz-adv-x="278" />']
    for svg in svgs:
        with open(svg,"r") as f:
            paths = re.findall(r'<path d="(.*?)"/>',f.read().replace("\n"," "))
        path = "".join(paths)
        letter_name = os.path.basename(svg).split(".")[0]
        if "_" in letter_name:
            letter_name = letter_name.replace("_","").lower()
        glyphs.append('<glyph glyph-name="{}" unicode="{}" horiz-adv-x="{}" d="{}" />'.format(letter_name,letter_name,300,path))

    with open(out_file,"w") as f:
        f.write(svg_embedding.replace("fontname",font_name).replace("Insert glyphs","\n".join(glyphs)))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("Provide the svg graphics directory path and the output file name")
    create_svg_font(sys.argv[1], sys.argv[2], sys.argv[2].split(".")[0])