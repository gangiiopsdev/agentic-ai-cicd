from fastapi import FastAPI
import subprocess
class SafeCommand:
    @staticmethod
def ping(host):
        if not all(char.isalnum() or char in '.,-_' for char in host):
            return "Invalid input"
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e.output.decode('utf-8'))
        except subprocess.TimeoutExpired:
            return "Ping timed out"

app = FastAPI()

@app.get("/ping")
def ping_command(host: str):
    result = SafeCommand.ping(host)
    if isinstance(result, dict):
        return result
    else:
        return {"status": "completed", "message": result}