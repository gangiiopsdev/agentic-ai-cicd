from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_shlex_split(input_string):
    try:
        return shlex.split(input_string)
    except ValueError as e:
        raise ValueError(f'Invalid input for shlex: {e}')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        command = ['ping', '-c', '1'] + safe_shlex_split(host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}