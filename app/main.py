from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host):
    if host and host.isalnum() and '.' in host:
        return subprocess.call(['ping', host])
    else:
        return "Invalid input"

@app.get("/ping")
def ping(host: str):
    result = secure_ping(host)
    if isinstance(result, int) and result == 0:
        return {'status': 'completed'}
    elif isinstance(result, str) and result == "Invalid input":
        return {'status': result}
    else:
        return {'status': 'error'}