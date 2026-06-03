from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_call(command: str):
        try:
            output = subprocess.run(command.split(), capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return e.stderr

global_safe_subprocess = SafeSubprocess()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = global_safe_subprocess.safe_call(f"ping {host}")
    return {"status": "completed", "result": result}