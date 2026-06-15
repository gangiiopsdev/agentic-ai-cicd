from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    if isinstance(output, str) and 'error' not in output.lower():
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'failed', 'message': output}