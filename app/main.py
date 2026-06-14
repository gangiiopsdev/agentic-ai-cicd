from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', *shlex.split(host)], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Error: {e.output.decode('utf-8')}'

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}