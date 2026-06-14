from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    if not host.strip():
        raise ValueError('Invalid host value')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return execute_ping(host)