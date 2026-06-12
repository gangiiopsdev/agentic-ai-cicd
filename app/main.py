from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        # Secure implementation using subprocess.run with shell=False and proper argument handling
        args = shlex.split(f"ping {host}")
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}