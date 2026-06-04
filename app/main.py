from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with shlex.quote for argument quoting
    subprocess.run(['ping', quote(host)], check=True)

@app.get("/ping")
def ping_endpoint(host: str):