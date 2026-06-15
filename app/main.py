from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return shlex.quote(input_str)

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', '-c 1', sanitize_input(host)], check=True, shell=False)
    return {'status': 'completed'}