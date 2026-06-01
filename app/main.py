from fastapi import FastAPI
import subprocess
import shlex
def safe_git_command(command):
    try:
        args = shlex.split(' '.join(command))
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stderr)