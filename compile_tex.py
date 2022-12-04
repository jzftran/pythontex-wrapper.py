#%%
import subprocess
import sys, os

latexcommand = "pdflatex.exe"
python_path = r"C:\Users\makro\.conda\envs\thesis\python.exe"
pythontexcommand = r"C:\texlive\2022\texmf-dist\scripts\pythontex\pythontex.py"
secondrunfile = "pythontex-wrapper-runagain.tmp"

#%%
# if __name__ == '__main__':
print(f"Arguments: {sys.argv}")

basefilename = os.path.splitext(sys.argv[1])[0]
# rem
print(f"base {basefilename}")

logfilename=f"{basefilename}.log"
pytxcodefilename=f"{basefilename}.pytxcode"
print(f"Log file: {logfilename}")
print(f"Working directory: {os.getcwd()}")
print(f"Using latex command: {latexcommand}")
print(f"Using pythontex command: {pythontexcommand}")
# %%
# compile using latex
print(f"\n\npythontex-wrapper: Calling {latexcommand}")
print("------------------------------------------\n\n")
first_latex_run = subprocess.run([latexcommand, *sys.argv[1:] ] )


if first_latex_run.returncode != 0:
    with open(logfilename, "a") as f:
        log = """pythontex-wrapper: This was the first latex run, before pythontex was called!
    ppythontex-wrapper: pythontex may have been run previously by lyx, before bibtex was run.
    pythontex-wrapper: If the problem was due to bad python output and persists after fixing it,
    pythontex-wrapper: please delete the pythontex-file-"""+ basefilename+ """ folder in the output directory."""

        f.write(log)
        f.close()
        exit()

#%%
# compilation in latex worked, run pythontex3 if needed

if os.path.isfile(pytxcodefilename) == False:

    with open(logfilename, "a") as f:
        log = "pythontex-wrapper: No pytxcode file generated, no need to run pythontex!"
        f.write(log)
        f.close()
        exit()




print(f"\n\npythontex-wrapper: Calling {pythontexcommand}")
print("------------------------------------------\n\n")

f = open(logfilename, "a")
pythontex_run = subprocess.call([python_path, pythontexcommand, sys.argv[1] ] , stdout=f)
f.close




if pythontex_run != 0:
    print(logfilename)
    with open(logfilename, "a") as f:
        log = """! Undefined control sequence.
                    Actually there is a pythontex error, see complete log for details.
        """
        f.write(log)
        f.close()
        exit()

# remove second-run-request file
try:
    os.remove(secondrunfile)
    print(f"{secondrunfile} was removed.")
except:
    print(f"{secondrunfile} was not removed.")


if os.path.isfile(secondrunfile) == True:
    print(f"\n\npythontex-wrapper: Calling {pythontexcommand} for 2nd run")
    print(f"------------------------------------------\n\n")
    
    pythontex_run =  subprocess.call([python_path, pythontexcommand,  sys.argv[1], "--rerun=always"  ] , stdout=f)

    if pythontex_run != 0:
        print(logfilename)
        with open(logfilename, "a") as f:
            log = """! Undefined control sequence.
                        Actually there is a pythontex error, see complete log for details.
            """
            f.write(log)
            f.close()
            exit()



# pythontex worked, run latex again
print(f"\n\npythontex-wrapper: Calling {latexcommand} second time")
print("------------------------------------------\n\n")

second_latex_run = subprocess.run([latexcommand, *sys.argv[1:] ] )

with open(logfilename, "a") as f:
    log = """pythontex-wrapper: This was the second latex run, after pythontex was called!"""
    f.write(log)
    f.close()

if second_latex_run.returncode != 0:
    sys.exit(1)
else:
    exit()

