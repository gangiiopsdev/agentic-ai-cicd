from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Fixed implementation using shlex.quote to safely escape host input
    subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True)

@app.get("/ping")
def ping_endpoint(host: str):  
    return {'result': ping(host)}