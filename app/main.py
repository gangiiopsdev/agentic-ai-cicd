from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
    if result.returncode != 0:
        return f'Error: {result.stderr}'
    else:
        return result.stdout

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}