from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Add logic to validate host input, e.g., IP address format
    return re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', host) is not None

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid host format"}, 400

    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}