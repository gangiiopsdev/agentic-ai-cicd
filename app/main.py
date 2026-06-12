from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Using subprocess.run instead of subprocess.call and avoiding shell=True
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
    except Exception as e:
        return str(e), ''

@app.get("/ping")
def ping(host: str):
    output, error = safe_ping(host)
    if error:
        return {'status': 'error', 'message': error}
    else:
        return {'status': 'completed', 'output': output}