from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host.isdigit() or len(host) > 3:
        return {"error": "Invalid host input"}
    if os.name == 'posix':
        subprocess.call(['ping', host])
    elif os.name == 'nt':
        subprocess.call(['ping', '/n', host])
    return {"status": "completed"}