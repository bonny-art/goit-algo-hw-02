import queue
import random
import time
from request_generator import generate_request
from request_processor import process_request

def main() -> None:
    """
    Main loop to generate and process requests in real-time.

    This function continuously generates and processes requests at random intervals
    until interrupted by the user.
    """
    request_id = 0
    request_queue = queue.Queue()

    try:
        while True:
            time.sleep(random.uniform(1.0, 3.0))

            if random.random() < 0.5:
                request_id += 1
                generate_request(request_id, request_queue)

            if random.random() < 0.5:
                process_request(request_queue)

    except KeyboardInterrupt:
        print('Exiting...')

if __name__ == "__main__":
    main()
