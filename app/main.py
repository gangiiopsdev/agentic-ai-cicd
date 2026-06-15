from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        # Using subprocess.run instead of subprocess.call
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr.decode('utf-8')}'

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)