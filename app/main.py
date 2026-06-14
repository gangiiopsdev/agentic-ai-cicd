from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def call(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        output, error = process.communicate()
        return output, error

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    output, error = SafeSubprocess.call(command)
    if error:
        return {'status': 'failed', 'error': error.decode()}
    else:
        return {'status': 'completed', 'output': output.decode()}