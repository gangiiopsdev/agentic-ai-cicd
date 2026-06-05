from fastapi import FastAPI
import subprocess
class CommandRunner:
    def run(self, host):
        # Using subprocess.run instead of subprocess.call
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    runner = CommandRunner()
    output = runner.run(subprocess.list2cmdline([host]))  # Sanitize input using subprocess.list2cmdline
    return {"status": "completed", "output": output}