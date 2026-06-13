from fastapi import FastAPI
import subprocess
cmd = ['ping', host]
subprocess.call(cmd, shell=False)
return {"status": "completed"}