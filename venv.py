#!/usr/bin/env python
import os
import subprocess
import virtualenv

def after_install(option, home_dir):
    pip = os.path.join(home_dir, 'bin', 'pip')
    subprocess.call([pip, 'install', '-r', 'requirements.txt'])

virtualenv.after_install = after_install

if __name__ == '__main__':
    virtualenv.main()
