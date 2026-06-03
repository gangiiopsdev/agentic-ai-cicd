from fastapi import FastAPI
import subprocess
def safe_subprocess(args):
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr.decode('utf-8')}'

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_host = host.replace(';', '').replace('&', '')
    args = ['ping', safe_host]
    return {'status': 'completed', 'output': safe_subprocess(args)}