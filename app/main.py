from fastapi import FastAPI
import subprocess
git diff --stat
app = FastAPI()

def escape_command(command: str):
    return ' '.join(subprocess.list2cmdline([arg]) for arg in command.split())

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        subprocess.run(escape_command(f"ping {host}").split(), check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}