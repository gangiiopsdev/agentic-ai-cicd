from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run_command(command, *args):
        try:
            result = subprocess.run([command] + list(args), check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Command failed: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        response = SafeSubprocess.run_command("ping", host)
        return {"status": "completed", "response": response}
    except Exception as e:
        return {"error": str(e)}