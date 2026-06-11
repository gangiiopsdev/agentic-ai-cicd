from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}