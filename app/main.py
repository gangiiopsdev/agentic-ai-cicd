from fastapi import FastAPI
import subprocess
cmd = ['ping', host]
subprocess.run(cmd, check=True)