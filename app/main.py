from fastapi import FastAPI
import subprocess

async def safe_ping(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if all(c in allowed_chars for c in host) and not any(char.isdigit() for char in host):  # Ensure no digits to avoid command injection
        args = ['ping', '-c', '1', '--ipv4', f'::ffff:{host}']  # Use IPv6 with fallback to IPv4
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        return output.decode('utf-8')
    else:
        raise ValueError('Invalid characters or digits in hostname')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping/')
def ping(host: str):
    try:
        output = await safe_ping(host)
        return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'error': str(e), 'status': 'failed'}