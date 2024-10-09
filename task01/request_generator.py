import random
import queue

# List of available requests
requests = [
    "Fix login issue", "Update account info", "Reset password", "Request refund", "Change email address",
    "Cancel subscription", "Track shipment", "Report bug", "Upgrade plan", "Request documentation",
    "Schedule appointment", "Verify payment", "Close account", "Technical support", "Billing question",
    "Transfer funds", "Feedback submission", "Modify order", "Activate account", "Service outage"
]

def generate_request(request_id: int, request_queue: queue.Queue) -> None:
    """
    Generate a request and add it to the queue.

    Args:
        request_id (int): The ID of the request.
        request_queue (queue.Queue): The queue where requests will be placed.

    The request contains a random issue from the available list and is added
    to the queue along with a random time for processing.
    """
    request_time = random.uniform(0.1, 1.0)
    request_data = f"Request {request_id}: {random.choice(requests)}"
    request_queue.put((request_id, request_time, request_data))
    print(f'\nRequest {request_id} generated.')
