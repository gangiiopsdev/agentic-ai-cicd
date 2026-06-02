from fastapi import FastAPI
import subprocess
import shlex
class CommandInputValidator:
    @staticmethod
def is_valid_command(input):
        return all(c.isalnum() or c in ' .,-_=' for c in input)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    if not CommandInputValidator.is_valid_command(host):
        return {"status": "failed", "error": "Invalid host input"}
    try:
        output = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}