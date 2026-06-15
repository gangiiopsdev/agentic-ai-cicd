from fastapi import FastAPI

def ping(host: str):
    # Validate host input to prevent injection or other issues
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        # Simulating a successful response for demonstration purposes
        return {'status': 'success'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}