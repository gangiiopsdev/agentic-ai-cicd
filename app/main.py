from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Construct the ping command safely
        args = ['ping', host]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'output': response}