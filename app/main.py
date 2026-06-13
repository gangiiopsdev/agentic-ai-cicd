from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if os.name == 'posix':
        subprocess.call(['ping', host])
    elif os.name == 'nt':
        subprocess.call(['ping', '/n', host])
    return {"status": "completed"}