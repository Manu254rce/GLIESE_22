import os
import sys
import subprocess

def install_and_update_env(package):
    try:
        subprocess.check_call(f"conda install {package} -y", shell=True)        
        subprocess.check_call("conda env export > environment.yml", shell=True)

    except subprocess.CalledProcessError as e:
            print(f"An error occured while installing the package or updating the env file: {e}")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python autoconf.py <package>")
        sys.exit(1)
    else:
        install_and_update_env(sys.argv[1])