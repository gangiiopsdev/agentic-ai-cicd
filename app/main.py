from fastapi import FastAPI
import subprocess
def safe_command(command_parts):
    allowed_commands = ['ping']
    if not all(cmd in allowed_commands for cmd in command_parts):
        raise ValueError('Unsafe command detected')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        safe_command(['ping', host])
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}