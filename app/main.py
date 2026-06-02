from fastapi import FastAPI
import subprocess
global pids = set()

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    sanitized = ''.join(char for char in input_string if char in allowed_chars)
    return sanitized

@app.get("/ping")
def ping(host: str):
    try:
        host = sanitize_input(host)
        pid = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pids.add(pid.pid)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.on_event("shutdown")
def shutdown_event():
    for pid in pids:
        subprocess.run(['kill', '-9', str(pid)])