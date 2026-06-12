from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Secure implementation without shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return run_ping(host)