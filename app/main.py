from fastapi import FastAPI
import subprocess
global_params = {
    'ping': ['-c', '1'],
    # Add more commands as needed
}

def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_input(user_input):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    for char in user_input:
        if char not in allowed_chars:
            raise ValueError('Invalid input')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        validate_input(host)
        command = global_params['ping'] + [host]
        output = run_command(command)
        return {"status": "completed", "output": output}
    except ValueError as e:
        return {"error": str(e)}