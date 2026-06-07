from fastapi import FastAPI
import shlex
import subprocess
class SafeCommand:
    @staticmethod
def escape_shell_arg(arg):
        return ' '.join(shlex.split(arg))
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_host = SafeCommand.escape_shell_arg(host)
    result = subprocess.run(['ping', shlex.quote(safe_host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}