from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def safe_ping_fixed(host: str):
    try:
        output = subprocess.run(['/bin/ping', '-c', '1', host], check=True, text=True, capture_output=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {"status": safe_ping_fixed(host)}