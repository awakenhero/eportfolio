import requests
import time

def send_request(url, client_id):
    try:
        # Start time before sending request
        start_time = time.time()
        
        # Send the request
        response = requests.get(url)
        
        # End time after receiving response
        end_time = time.time()
        
        # Calculate response time in milliseconds
        response_time = (end_time - start_time) * 1000
        
        print(f"[Client {client_id}] Status Code: {response.status_code}, Response Time: {response_time:.2f}ms")
        
    except requests.exceptions.RequestException as e:
        print(f"[Client {client_id}] Error: {e}")

# Server URL
SERVER_URL = 'http://192.168.65.2/'
NUM_REQUESTS = 10000
DELAY = 0

# Track average response time
total_response_time = 0
successful_requests = 0

for request_id in range(1, NUM_REQUESTS + 1):
    start_time = time.time()
    send_request(SERVER_URL, request_id)
    time.sleep(DELAY)
