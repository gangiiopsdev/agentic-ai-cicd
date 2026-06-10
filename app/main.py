from fastapi import FastAPI
import subprocess
class CommandRunner:
    def run(self, command: str):
        try:
            result = subprocess.run(command.split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return e.stderr.decode()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    runner = CommandRunner()
    result = runner.run(f"ping {host}")
    return {"status": "completed", "result": result}