import requests  # for posting  HTTP requests this library requires ( Manual installation required via pip) (Requests, n.d.).
import time     # for adding delays this library requires (Python Software Foundation, n.d.)

def send_request(url, client_id): 
    # Send a request to apache2 server
    # This function simulates an IoT device sending data to a apache2 server (Python Software Foundation, n.d.).
    try: 
        #  Posting http request to get response  from apache2 server (Requests, n.d.)
        # This URL should be the endpoint where the IoT device sends data
        resp = requests.get(url)
        print(f"Device {client_id} -> Status: {resp.status_code}, URL: {url}") # Logging the response with status code and IP or URL (Kennedy, 2023.)
        
    except requests.exceptions.RequestException as e:
        # Logging error when apache2 server  fail to process the request (Requests, n.d.)
        print(f"Device {client_id} failed: {e}") 

# Test server URL where apache2 is running on KALI Linux 
SERVER_URL = 'http://192.168.65.2/' # (Python Software Foundation, n.d.)

# Simulate a few IoT devices
NUM_DEVICES = 10 # Number of devices for  simulating requests (python Software Foundation, n.d.)
DELAY = 2  # Delay between the http requests. this is to avoid DDOS attack (python Software Foundation, n.d.)

# Send test requests
for device in range(1, NUM_DEVICES + 1): # this loop to simulate 10 IOT devices (Python Software Foundation, n.d.)
    send_request(SERVER_URL, device) # senting request to apache2 server
    time.sleep(DELAY)  # delay between the http requests. this is to avoid DDOS attack. (Python Software Foundation, n.d.)


    """
# References used for this script are documented in:
# 'Code_References.docx' – available in the project folder.
# Full Harvard-style referencing is included in that document.

"""