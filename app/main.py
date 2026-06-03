from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        result = subprocess.run([command] + list(args), capture_output=True, text=True, check=True, **kwargs)
        return result

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = subprocess.list2cmdline([host])
        result = SafeSubprocess.run('ping', sanitized_host)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}