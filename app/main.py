from fastapi import FastAPI
import subprocess
class SafeCommand:
    @staticmethod
    def run(command: list):
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"

class PingHandler:
    @staticmethod
    def ping(host: str):
        if not host:
            raise ValueError("Host cannot be empty")
        command = ['ping', host]
        return SafeCommand.run(command)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = PingHandler.ping(host)
        return {"status": "completed", "result": result}
    except ValueError as e:
        return {"error": str(e)}