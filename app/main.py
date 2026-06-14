from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    cmd = ['ping', host]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

@app.get="/ping")
def ping(host: str):
    # Safe implementation
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}