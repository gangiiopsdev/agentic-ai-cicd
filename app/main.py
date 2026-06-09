from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

@app.get("/ping")
def ping(host: str):

    # Safer implementation
    output = safe_ping(host)

    return {"status": "completed", "output": output}