from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command, host, timeout=5):
        cmd = ['ping', shlex.quote(host)]
        try:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=timeout)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/" )
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return SafeSubprocess.run('ping', host)