from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

def safe_ping(host: str):
    # Escape any shell meta-characters in the host parameter
    args = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}