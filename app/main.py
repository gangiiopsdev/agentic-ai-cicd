from fastapi import FastAPI
import shlex
import subprocess

cmd = ['ping', host]
args = shlex.split(' '.join(cmd))
subprocess.run(args, check=True)