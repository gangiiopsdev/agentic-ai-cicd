from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        args = ['ping', host]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.output}