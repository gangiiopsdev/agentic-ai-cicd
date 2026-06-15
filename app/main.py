from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def call(command):
        # Validate and sanitize the input command
        if not all(isinstance(arg, str) for arg in command):
            raise ValueError('Invalid command arguments')
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        output, error = process.communicate()
        return output, error

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host:
        raise ValueError('Host parameter is required')
    command = ['ping', host]
    output, error = SafeSubprocess.call(command)
    if error:
        return {"status": "failed", "error": error.decode()}
    else:
        return {"status": "completed", "output": output.decode()}