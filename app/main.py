from fastapi import FastAPI
import subprocess
global host
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    global host
    host = host
    if host == "localhost":
        subprocess.call(f"ping {host}", shell=False)
    else:
        return {'status': 'Error', 'message': 'Invalid host'}
    return {'status': 'completed'}