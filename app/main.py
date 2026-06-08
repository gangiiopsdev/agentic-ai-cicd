from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate the input to ensure it does not contain malicious characters
    if not all(c.isalnum() or c in '.-:' for c in host):
        raise ValueError('Invalid hostname')
    return ping(host)