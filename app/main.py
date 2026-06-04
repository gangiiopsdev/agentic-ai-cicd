from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    if host.startswith('192.168.') or host.startswith('10.'):  # Example of basic validation
        args = ['ping', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    return ping(host)