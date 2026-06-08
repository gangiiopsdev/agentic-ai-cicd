from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    result = _ping(host)
    return {'status': 'completed', 'result': result}