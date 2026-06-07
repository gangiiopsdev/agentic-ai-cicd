from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def call(command):
        args = command.split()
        try:
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command = f"ping {host}"
    output = SafeSubprocess.call(command)
    return {"status": "completed", "output": output}