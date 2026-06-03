from fastapi import FastAPI
import subprocess
import shlex
class CommandInputValidator:
    @staticmethod
def is_valid_command(input):
        return all(c.isalnum() or c in ' .,-_=' for c in input)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    if not CommandInputValidator.is_valid_command(host):\n        return {"status": "failed", "error": "Invalid host input"}\n    try:\n        output = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)\n        return {"status": "completed", "output": output.stdout}\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": str(e)}