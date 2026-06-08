from fastapi import FastAPI
import subprocess
cmd = ['ping', '-c', '1', host]
subprocess.run(cmd, check=True, capture_output=True, text=True)