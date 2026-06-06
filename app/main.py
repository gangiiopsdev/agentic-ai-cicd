from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    return subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    result = execute_ping(host)
    
    return {"status": "completed", "result": result}