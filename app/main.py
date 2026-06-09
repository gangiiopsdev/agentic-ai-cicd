from fastapi import FastAPI
global allowed_hosts = {'example.com'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in allowed_hosts:
        # Use subprocess.run for safer command execution, sanitize input first
        sanitized_host = ''.join(filter(str.isalnum, host))
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError('Host not allowed')
    return {'status': 'completed'}