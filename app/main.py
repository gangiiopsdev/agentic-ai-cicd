from fastapi import FastAPI
import subprocess
def sanitize_input(host):
    allowed_hosts = ['localhost', '127.0.0.1']  # Define a list of allowed hosts
    return host if host in allowed_hosts else None

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    cleaned_host = sanitize_input(host)
    if cleaned_host is not None:
        command = ['ping', '-c 1', '--'] + [cleaned_host]
        subprocess.run(command, capture_output=True, text=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}