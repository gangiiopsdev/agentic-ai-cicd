from fastapi import FastAPI
import subprocess

def execute_safe_command(command, *args):
    sanitized_args = [arg.strip() for arg in args]
    try:
        result = subprocess.run([command] + list(sanitized_args), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = execute_safe_command('ping', host.strip())
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'error': str(e)}