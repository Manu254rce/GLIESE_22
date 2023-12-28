import sys
import subprocess

def install_and_update_env(package):
    try:
        subprocess.check_call(f"conda install {package} -y", shell=True)        
        subprocess.check_call("conda env export > environment.yml", shell=True)

    except subprocess.CalledProcessError as e:
            print(f"An error occured while installing the package or updating the env file: {e}")
            sys.exit(1)

def remove_and_update_env(paackage):
    try:
        subprocess.check_call(f"conda remove {package} -y", shell=True)
        subprocess.check_call("conda env export > environment.yml", shell=True)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while removing the package or updating the environment file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python autoconf.py <command> <package>")
        print("where <command>: install, remove")
        sys.exit(1)
    else:
        command, package = sys.argv[1], sys.argv[2]
        if command == 'install':
            install_and_update_env(package)
        elif command == 'remove':
            remove_and_update_env(package)
        else:
            print(f"Unknown command: {command}")
            print("Usage: python autoconf.py <command> <package>")
            print("<command> can be 'install' or 'remove'")
            sys.exit(1)