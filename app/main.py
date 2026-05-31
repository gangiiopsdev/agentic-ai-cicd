from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    return shlex.quote(host)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', escape_host(host)])
    return {"status": "completed"}