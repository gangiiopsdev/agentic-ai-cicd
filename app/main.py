from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    return {'status': 'completed', 'output': safe_ping(host)}