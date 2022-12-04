pythontex-wrapper [![License: CC0-1.0](https://licensebuttons.net/l/zero/1.0/80x15.png)](http://creativecommons.org/publicdomain/zero/1.0/)
=================

pythontex-wrapper.py is a Python-based wrapper around pdflatex to use pythontex in lyx. The original idea comes from https://github.com/mghansen256/pythontex-wrapper. Because the script is implemented in Python, in theory is hould be a cross-platform solution.

## Usage

Modify an existing format converter in lyx (for example pdflatex) to use pythontex-wrapper.sh instead of pdflatex.

In the *CONVERTERS SECTION* in the lyx configuration file (preferences file), you should specify Python instance that will run the compile_tex.py to look similar to this:

    #
    # CONVERTERS SECTION ##########################
    #

    \converter "pdflatex" "pdf2" "\"C:\\Users\\makro\\.conda\\envs\\thesis\\python.exe\" \"C:\\Users\\makro\\Downloads\\pythontex-wrapper-master\\compile_tex.py\" $$i" "latex=pdflatex,hyperref-driver=pdftex"

Note that the Python instance should have installed pygments, and other dependencies that are used by pythontex and your LyX/LaTeX file uses.
