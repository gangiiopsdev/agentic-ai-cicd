from fastapi import FastAPI
import subprocess
def ping(host: str):
    if host.strip() and all(c.isalnum() or c in '-.' for c in host):
        # Secure implementation using subprocess.run with proper sanitization
        command = ['ping', subprocess.list2cmdline([host])]
        subprocess.run(command, check=True, text=True)
    else:
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)