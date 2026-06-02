from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.Popen to avoid shell injection
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    # Using the safe function to prevent shell injection
    result = safe_ping(host)
    return {"status": "completed", "result": result}