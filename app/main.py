from fastapi import FastAPI
import subprocess
genpy.from_path('fastapi')
app = FastAPI()
def escape_shell_command(user_input):
    return subprocess.list2cmdline(user_input.split())
@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        subprocess.run(escape_shell_command(f"ping {host}"), shell=False, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}