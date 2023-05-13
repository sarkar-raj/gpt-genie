import os
import subprocess
import sys
import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_requirements(file):
    with open(file, 'r') as f:
        requirements = f.read().splitlines()
        print(requirements)
    for requirement in requirements:
        try:
            pkg_resources.require(requirement)
        except (DistributionNotFound, VersionConflict):
            install(requirement)

def run_streamlit(file):
    os.system('streamlit run ' + file)

if __name__ == "__main__":
    check_requirements('requirements.txt')
    run_streamlit('app.py')
