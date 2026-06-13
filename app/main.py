from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command, *args):
    return subprocess.run([command] + list(args), capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    try:
        result = execute_safe_command('ping', host)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}