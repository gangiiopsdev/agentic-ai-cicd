from fastapi import FastAPI
import subprocess
class CommandExecutor:
    @staticmethod
def safe_execute(command, *args):
        full_command = [command] + list(args)
        try:
            output = subprocess.run(full_command, capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = CommandExecutor.safe_execute('ping', host)
    return {'status': 'completed', 'result': result}