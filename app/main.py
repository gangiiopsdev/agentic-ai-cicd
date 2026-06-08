from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'
app = FastAPI()
@app.get="/ping")
def ping(host: str):
    completed_process = subprocess.run(generate_ping_command(host), shell=False, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': completed_process.stdout, 'stderr': completed_process.stderr}