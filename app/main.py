from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)