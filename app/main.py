from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': ping_safe(host)}