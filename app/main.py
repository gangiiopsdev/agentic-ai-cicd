from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the input to prevent command injection
        host = shlex.quote(host)
        command = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}