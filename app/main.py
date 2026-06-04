from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host: str):
    # Basic escaping for demonstration purposes. In production use a secure method.
    return host.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    try:
        # Secure implementation using subprocess.run with shell=False
        result = subprocess.run(['ping', escape_host(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}