from fastapi import FastAPI
import subprocess
from starlette.exceptions import HTTPException

app = FastAPI()

def validate_host(host: str) -> bool:
    # Implement your validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}