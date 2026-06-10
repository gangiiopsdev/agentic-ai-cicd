from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', '-c', '1', host]  # Use ping with count to limit the number of pings
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)