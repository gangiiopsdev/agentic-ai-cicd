from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: list, *args, **kwargs):
        try:
            result = subprocess.run(command, *args, capture_output=True, text=True, check=True, **kwargs)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise Exception(f'Command failed with error: {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    output = SafeSubprocess.run(command)
    return {'status': 'completed', 'output': output}