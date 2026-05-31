from fastapi import FastAPI
import subprocess
c
app = FastAPI()

@app.get('/')</code></pre>
<code class="hljs"><pre name="code" class="language-python">def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

def ping(host: str):
    # Secure implementation with full path and proper input validation
    subprocess.run(['/bin/ping', '-c', '1', host], check=True)

@app.get('/ping')
def ping_endpoint(host: str):</code></pre>
<code class="hljs"><pre name="code" class="language-python">    if '@' not in host and len(host) < 256:
        return ping(host)
    else:
        return {'error': 'Invalid host'}, 400</code></pre>