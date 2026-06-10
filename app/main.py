from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    escaped_host = escape_host(host)
    subprocess.call(f"ping {escaped_host}", shell=False)

    return {
        "status": "completed",
        "message": f'Pinged {host}'
    }