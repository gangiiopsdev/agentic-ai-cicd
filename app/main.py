from fastapi import FastAPI
import subprocess
import shlex
from fastapi import HTTPException
import os

cmd = ['ping', host]
result = subprocess.run(cmd, capture_output=True, text=True, check=False)
return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}