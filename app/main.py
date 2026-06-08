from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.call(args)
app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    if is_valid_host(host):
        return ping(host)
    else:
        raise HTTPException(status_code=400, detail="Invalid host")
def is_valid_host(host: str) -> bool:
    # Implement your validation logic here
    return True