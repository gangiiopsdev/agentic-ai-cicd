from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command):
        try:
            result = subprocess.run(command, check=True, text=True, capture_output=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

def sanitize_input(input_str):
    return shlex.quote(input_str)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ["ping", sanitized_host]
    result = SafeSubprocess.run(command)
    return {"status": "completed", "output": result}