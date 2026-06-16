from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use a safe way to ping without shell=True
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

def unsafe_ping(host: str):
    # Vulnerable implementation
    subprocess.call(f"ping {host}", shell=True)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)