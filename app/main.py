from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not is_valid_host(host):
        return "Invalid host"
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    return ping(host)
def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., check for allowed IP ranges or hostnames.
    return True