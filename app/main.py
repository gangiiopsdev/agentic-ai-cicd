from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use a whitelist of allowed hosts or validate host input
        if host in ['allowed_host1', 'allowed_host2']:
            result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')</span><span class="hljs-keyword">def</span> home():
    <span class="hljs-keyword">return</span> {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')</span><span class="hljs-keyword">def</span> ping(host: str):
    return safe_ping(host)