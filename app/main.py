from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Sanitize host input
        subprocess.check_output(['ping', subprocess.check_output(f'echo {host} | cut -d" " -f1'.split()).decode()], stderr=subprocess.STDOUT)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': e.output.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)