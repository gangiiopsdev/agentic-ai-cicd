from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host: str) -> str:
    return ''.join(e if e.isalnum() else '_' for e in host)

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    # Secure implementation
    subprocess.call(['ping', f'"{safe_host}"'], check=True)

    return {"status": "completed"}