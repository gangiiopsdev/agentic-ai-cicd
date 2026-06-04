from fastapi import FastAPI
import subprocess
def execute_ping(host):
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode()
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    status = execute_ping(host)
    return {'status': 'completed', 'output': status}