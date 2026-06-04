from fastapi import FastAPI
import subprocess
global_command = ['ping']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Use subprocess.run with shell=False for a safer approach
        result = subprocess.run(global_command + [host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))