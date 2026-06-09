from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        output = ping_safe(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}