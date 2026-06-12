from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Use the safe function to avoid injection vulnerabilities
    return {'status': 'completed', 'output': safe_ping(host)}