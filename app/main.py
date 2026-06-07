from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: list):
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return e.stderr.decode('utf-8')

app = FastAPI()

@app.get("/{host:path}")
def ping(host: str):
    safe_command = ["ping", host]
    result = SafeSubprocess.run(safe_command)
    return {"status": "completed", "result": result}