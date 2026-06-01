from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return ' '.join(subprocess.list2cmdline([arg]).split())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', escape_shell_arg(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}