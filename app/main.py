from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_safe_ping(host):
    args = ['ping', host]
    return subprocess.run(args, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    result = run_safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}