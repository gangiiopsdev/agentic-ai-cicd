from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping_host(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Basic validation of host input
        raise HTTPException(status_code=400, detail="Invalid host format")
    return ping(host)