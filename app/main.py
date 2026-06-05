from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Secure implementation using subprocess.Popen without shell=True
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = run_ping(host)
    return {"status": "completed", "output": result}