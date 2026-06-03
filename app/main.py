from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    output = run_ping(host)
    return {"status": "completed", "output": output}