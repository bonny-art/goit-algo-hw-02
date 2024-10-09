import time
import random
import queue

def process_request(request_queue: queue.Queue) -> None:
    """
    Process a request from the queue, simulating the time it takes to handle it.

    Args:
        request_queue (queue.Queue): The queue from which requests are taken.

    The function retrieves a request from the queue and simulates processing
    it by pausing for a random duration. If the queue is empty, it prints a message.
    """
    if not request_queue.empty():
        request_id, request_time, request_data = request_queue.get()

        estimated_time = request_time * random.uniform(0.5, 1.5)
        print(f'\nProcessing request {request_id}...\n{request_data}\nEstimated time: {estimated_time:.2f} seconds.')

        time.sleep(request_time)

        print(f'Request {request_id} processed in {request_time:.2f} seconds.')
    else:
        print('\nThe queue is empty. No requests to process.')
