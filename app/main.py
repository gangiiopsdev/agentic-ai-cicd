from fastapi import FastAPI
import subprocess
import shlex

cmd = ['ping', host]
subprocess.call(cmd)