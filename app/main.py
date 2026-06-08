from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if '||' in host or ';' in host or '&' in host:
        raise ValueError('Unsafe input detected')
    try:
        args = ['ping', host]
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result}