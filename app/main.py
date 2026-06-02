from fastapi import FastAPI
import subprocess
import shlex

cmd = ["ping", host]
subprocess.run(cmd, check=True)
return {"status": "completed"}