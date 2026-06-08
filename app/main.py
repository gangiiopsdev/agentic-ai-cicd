from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with list of arguments and input validation
    if host.strip() == '':
        raise ValueError('Host cannot be empty')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):  
    return ping(host)