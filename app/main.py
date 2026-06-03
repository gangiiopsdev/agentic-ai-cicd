from fastapi import FastAPI
import subprocess
cmd = ['ping', host]
subprocess.call(cmd)