from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host input
    if not host or '@' in host or '%' in host:
        raise ValueError("Invalid hostname")

    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)