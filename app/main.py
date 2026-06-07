from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping'] + [arg for arg in host.split() if arg.isalnum()]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if 'error' in result:
        return result
    else:
        return result