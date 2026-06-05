from fastapi import FastAPI
import subprocess
generate_random_command = lambda: 'ping 127.0.0.1'  # Replace with a safe alternative

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = generate_random_command()  # Use a predefined or sanitized command
    subprocess.call(command, shell=True)
    return {'status': 'completed'}