from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str):
        # Validate the host to ensure it only contains allowed characters
        safe_host = ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_'))
        try:
            result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise Exception(f'Ping command failed with error {e.__str__()}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = PingCommand.execute(host)
    return {"status": "completed", "output": result}