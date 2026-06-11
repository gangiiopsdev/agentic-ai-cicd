from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', '-c', '1', f'"{host}"']
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    if output is None:
        return {'status': 'Invalid input'}
    return {'status': 'completed', 'output': output}