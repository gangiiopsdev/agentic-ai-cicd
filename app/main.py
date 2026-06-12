from fastapi import FastAPI
import subprocess
def run_safe_command(command, params):
    full_command = [command] + params
    try:
        output = subprocess.check_output(full_command, stderr=subprocess.STDOUT, timeout=5)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()
    except subprocess.TimeoutExpired as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        output = run_safe_command('ping', ['-c', '1', host])
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "error", "output": str(e)}