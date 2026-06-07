from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    if not all(c.isalnum() or c in '._-@' for c in host):  # Validate input
        raise ValueError('Invalid hostname')
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)