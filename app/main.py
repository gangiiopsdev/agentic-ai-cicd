from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command, args):
    full_command = [command] + list(map(shlex.quote, args))
    result = subprocess.run(full_command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    return safe_subprocess('ping', ['-c', '1', host])