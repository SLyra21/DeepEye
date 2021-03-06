import sys
sys.path.append('..')

from DeepLib import *

def main(args):
    # Check input arguments
    if len(args) != 2:
        sys.stderr.write("usage: %s <media file or uri>\n" % args[0])
        sys.exit(1)

    else:
        filePath = args[1]

    # initialize DeepLib
    DeepLib.init()

    # build pipeline
    pipeline = DeepLib \
        .pipeline() \
        .withFileInput(filePath) \
        .withEGLOutput() \
        .build()

    # run on the main thread
    DeepLib.runOnMain(pipeline)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
