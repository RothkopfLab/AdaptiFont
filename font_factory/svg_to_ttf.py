import os,sys
from subprocess import DEVNULL, STDOUT, check_call, check_output,Popen,PIPE
if (os.name != "nt"):
    sys.path.append('/usr/lib/python3/dist-packages')


def svg_to_ttf(in_file,out_file):
    if os.name == 'nt':
        command = f'cmd ./FontForgeBuilds/fontforge.bat -c "\'\\"open(\\\\\\"{in_file}\\\\\\").generate(\\\\\\"{out_file}\\\\\\")\'"'
        check_call(command,shell=True, stdout=DEVNULL, stderr=STDOUT)
    else:
        import fontforge
        fontforge.open(in_file).generate(out_file)
if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("Provide input and output filename")
    svg_to_ttf(sys.argv[1],sys.argv[2])