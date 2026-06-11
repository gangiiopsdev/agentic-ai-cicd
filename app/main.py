from fastapi import FastAPI
import httpx

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum())

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    sanitized_host = sanitize_input(host)
    try:
        async with httpx.AsyncClient() as client:
            response = await client.head(f'http://{sanitized_host}')
            return {'status': 'completed', 'output': str(response.status_code)}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}