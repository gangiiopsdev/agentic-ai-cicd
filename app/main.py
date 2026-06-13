from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_execute(command, *args):
        if not isinstance(command, list) or any(not arg.isalnum() for arg in args):
            raise ValueError('Invalid command or arguments')
        try:
            return subprocess.run([command] + list(args), check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e), 'stdout': e.stdout, 'stderr': e.stderr}

app = FastAPI()

def execute_ping(host):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    return SafeSubprocess.safe_execute('ping', host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = execute_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return result
    else:
        return {
            "status": "completed",
            "stdout": result.stdout,
            "stderr": result.stderr
        }