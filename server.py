import time
import grpc
import clock_sync_pb2
import clock_sync_pb2_grpc
import concurrent.futures
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

class ClockSyncServicer(clock_sync_pb2_grpc.ClockSyncServicer):
    def __init__(self):
        self.client_times = {}

    def GetTime(self, request, context):
        client_id = context.peer()
        server_time = int(time.time() * 1000)
        formatted_time = self.format_time(server_time)

        logging.info(f"Client {client_id} connected. Server time: {formatted_time}")

        return clock_sync_pb2.TimeResponse(server_time=server_time)

    def UpdateTime(self, request, context):
        server_time = int(time.time() * 1000)
        client_id = context.peer()

        if client_id not in self.client_times:
            self.client_times[client_id] = []

        offset = server_time - request.client_time
        corrected_time = server_time - offset
        formatted_time = self.format_time(float(corrected_time))

        self.client_times[client_id].append(corrected_time)

        logging.info(f"\nClient {client_id} updated time to: {formatted_time}\n")

        average_time = (sum(self.client_times[client_id]) + server_time) / len(self.client_times)+1

        return clock_sync_pb2.TimeResponse(server_time=int(average_time))

    def format_time(self, timestamp):
        return datetime.fromtimestamp(timestamp/1000).strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]
        # return datetime.utcfromtimestamp(timestamp / 1000).strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]

    def __del__(self):
        logging.info("Server shutting down.")

def run_server():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    clock_sync_pb2_grpc.add_ClockSyncServicer_to_server(ClockSyncServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    run_server()
