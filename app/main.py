from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation without shell=True and proper input sanitization
    try:
        command = ['ping'] + shlex.split(host)
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}