import requests  # for posting  HTTP requests this library requires ( Manual installation required via pip) (Requests, n.d.).
import time     # for adding delays this library requires (Python Software Foundation, n.d.)

def send_request(url, client_id):
    # Send a request to apache2 server
    # This function simulates an IoT device sending data to a apache2 server (Python Software Foundation, n.d.).

    try:
        # Start counting  time before posting the request to apache2 endpoint (Python Software Foundation, n.d.)
        start_time = time.time()
        
        #  Posting http request to get response  from apache2 server (Requests, n.d.)
        # This URL should be the endpoint where the IoT device sends data
        response = requests.get(url)
        
        # End time after receiving response from apache2 server  (Python Software Foundation, n.d.)
        end_time = time.time()
        
        # Calculate response time from apache2 server in milliseconds (Python Software Foundation, n.d.)
        response_time = (end_time - start_time) * 1000
    
        print(f"[Client {client_id}] Status Code: {response.status_code}, Response Time: {response_time:.2f}ms") # status code, client ID and response time printing (Kennedy, 2023.)
        
    except requests.exceptions.RequestException as e:
        # Logging error when apache 2 server  fails to process the request (Requests, n.d.)
        print(f"[Client {client_id}] Error: {e}") # Printing error message with client ID


# # Test server URL where apache2 is running on KALI Linux
SERVER_URL = 'http://192.168.65.2/'  # (Python Software Foundation, n.d.)

# DDOS attack simulation by flooding 100000 requests to apache2 server without delay 
NUM_REQUESTS = 100000           # (python Software Foundation, n.d.)     
DELAY = 0                       # (python Software Foundation, n.d.)     

# The loop counts from 1 to 100,000 without any delay between requests
for request_id in range(1, NUM_REQUESTS + 1):  # (python Software Foundation, n.d.)
    send_request(SERVER_URL, request_id)
    # delay between the http requests. in this case no delay since DELAY is set to 0 (Python Software Foundation, n.d.)
    time.sleep(DELAY)  


"""

# References used for this script are documented in:
# 'Code_References.docx' – available in the project folder.
# Full Harvard-style referencing is included in that document.
"""