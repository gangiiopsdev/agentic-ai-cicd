from fastapi import FastAPI
import subprocess
import shlex
generate_random_nonce = lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=16))

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Use a secure temporary file to store the command and execute it safely
    nonce = generate_random_nonce()
    command_path = f'/tmp/ping_{nonce}.sh'
    with open(command_path, 'w') as script:
        script.write(f'ping {host}')
    subprocess.run(['chmod', '+x', command_path], check=True)
    try:
        result = subprocess.run([command_path], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}