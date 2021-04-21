import os,sys
from subprocess import DEVNULL, STDOUT, check_call
import time
if os.name == 'nt':
    potrace_path = os.path.join('potrace_win','potrace.exe')
    #potrace_path = os.path.join('../../portrace_win/potrace.exe')
else:
    potrace_path = 'potrace'
def bmp_to_svg(in_folder,out_folder):
    base_path = os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    filenames = os.listdir(in_folder)
    start = time.perf_counter()
    if os.name == 'nt':
        filtfiles = list(filter(lambda x:".bmp" in x,filenames))
        check_call('{} {} -b svg'.format(
                os.path.join(base_path,potrace_path),
                " ".join(['"'+os.path.join(in_folder, f)+'"' for f in filtfiles])
            ),shell=True, stdout=DEVNULL, stderr=STDOUT)
        for f in filtfiles:
            os.replace(os.path.join(in_folder, f.split(".")[0]+".svg"),os.path.join(out_folder, f.split(".")[0]+".svg"))
    else:
        for f in filenames:
            check_call('{} "{}" -b svg -o "{}"'.format(
                os.path.join(base_path,potrace_path),
                os.path.join(in_folder, f),
                os.path.join(out_folder, f.split(".")[0]+".svg")
            ),shell=True, stdout=DEVNULL, stderr=STDOUT)
if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("provide the folder name containing the bmp images and the output folder")
    bmp_to_svg(sys.argv[1],sys.argv[2])