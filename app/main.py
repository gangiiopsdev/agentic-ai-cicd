from fastapi import FastAPI
import subprocess
generate_random_command = lambda: 'ping 127.0.0.1'  # Replace with a safe alternative

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = generate_random_command().split()  # Split the command into arguments to prevent shell injection
    subprocess.run(command, check=True)
    return {'status': 'completed'}