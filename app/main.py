from fastapi import FastAPI
import subprocess
app = FastAPI()

def validate_host(host: str) -> bool:
    # Implement a simple regex to allow only alphanumeric characters and hyphens
    allowed_chars = re.compile(r'^[a-zA-Z0-9-]+$')
    return bool(allowed_chars.match(host))

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        args = ['ping', host]
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host name"}