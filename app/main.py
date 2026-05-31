from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    cmd = ['ping', host]
    return execute_command(cmd)