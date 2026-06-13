from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_secure_command(command: str):    try:        result = subprocess.run(command.split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)        return {'status': 'completed', 'output': result.stdout.decode()}    except subprocess.CalledProcessError as e:        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):    # Secure implementation    return run_secure_command(['ping', host])