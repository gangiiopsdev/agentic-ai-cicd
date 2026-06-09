from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if validate_host(host):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return f'Error: {e}'
def validate_host(host: str) -> bool:
    # Add validation logic here (e.g., allow only certain hosts)
    return True
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)