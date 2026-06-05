from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    output = _ping(host)
    return {"status": "completed", "output": output}