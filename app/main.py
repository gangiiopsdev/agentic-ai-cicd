from fastapi import FastAPI
import subprocess
def run_safe_command(command):
    import shlex
    args = shlex.split(command)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    output = run_safe_command(command)
    return {'status': 'completed', 'output': output}