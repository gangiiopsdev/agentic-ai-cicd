from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}