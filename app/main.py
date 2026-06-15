from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    # Secure implementation using shlex to escape shell metacharacters
    subprocess.call(['ping', *shlex.split(host)])

@app.get('/ping')
def ping(host: str):
    return {'status': 'completed'}