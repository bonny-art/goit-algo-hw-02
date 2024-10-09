import queue
import time
import random

requests = [
    "Fix login issue", "Update account info", "Reset password", "Request refund", "Change email address",
    "Cancel subscription", "Track shipment", "Report bug", "Upgrade plan", "Request documentation",
    "Schedule appointment", "Verify payment", "Close account", "Technical support", "Billing question",
    "Transfer funds", "Feedback submission", "Modify order", "Activate account", "Service outage"
]

def generete_request(request_id, request_queue):
    request_time = random.uniform(0.1, 1.0)
    request_data = f"Request {request_id}: {random.choice(requests)}"
    request_queue.put((request_id, request_time, request_data))
    print(f'\nRequest {request_id} generated.')


def process_request(request_queue):
    if not request_queue.empty():
        request_id, request_time, request_data = request_queue.get()

        estimated_time = request_time * random.uniform(0.5, 1.5)
        print(f'\nProcessing request {request_id}...\n{request_data}\nEstimated time: {estimated_time:.2f} seconds.')

        time.sleep(request_time)

        print(f'Request {request_id} processed in {request_time:.2f} seconds.')
    else:
        print('\nThe queue is empty. No requests to process.')

def main():

    request_id = 0
    request_queue = queue.Queue()

    try:
        while True:
            time.sleep(random.uniform(1.0, 3.0))

            if random.random() < 0.5:
                request_id += 1
                generete_request(request_id, request_queue)

            if random.random() < 0.5:
                process_request(request_queue)

    except KeyboardInterrupt:
        print('Exiting...')

if __name__ == "__main__":
    main()
