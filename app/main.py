from fastapi import FastAPI
import subprocess
from typing import Dict, Any
import shlex

global app = FastAPI()

def ping(host: str) -> Dict[str, Any]:
    try:
        args = shlex.split(f'ping -c 1 {host}')
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}