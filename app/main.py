from fastapi import FastAPI
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Whitelist of allowed hostnames or use a regular expression to validate
    allowed_hostnames = ['example.com', 'test.example.com']  # Replace with actual list
    if host not in allowed_hostnames:
        raise ValueError('Invalid hostname')

    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, check=True, text=True, capture_output=True)

    return {'status': 'completed', 'output': result.stdout}