from fastapi import FastAPI
import subprocess
global_result = None
def ping(host: str):
    global_result = subprocess.run(['ping', host], capture_output=True, text=True)
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    ping(host)
    return {'status': 'completed', 'result': global_result.stdout}