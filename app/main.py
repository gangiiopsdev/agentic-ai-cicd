from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command_parts):
        command = ' '.join(shlex.quote(part) for part in command_parts)
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = SafeSubprocess.run(['ping', host])
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}