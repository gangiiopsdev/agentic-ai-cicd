from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(hostname: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9-.]+$')
    return bool(pattern.match(hostname))

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', hostname]
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed"}