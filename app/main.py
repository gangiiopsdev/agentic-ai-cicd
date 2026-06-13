from fastapi import FastAPI
import subprocess
class CommandExecutor:
    @staticmethod
def safe_execute(command, args):
        try:
            result = subprocess.run([command] + args, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

def validate_host(host):
    # Basic validation: only allow alphanumeric characters and a few special characters
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    if not all(char in allowed_chars for char in host):
        return False
    return True

def safe_ping(host):
    executor = CommandExecutor()
    result = executor.safe_execute("ping", [host])
    return {"status": "completed", "result": result}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        return safe_ping(host)
    else:
        return {"status": "error", "message": "Invalid host"}