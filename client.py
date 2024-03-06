import grpc
import time
import clock_sync_pb2
import clock_sync_pb2_grpc
from datetime import datetime

def get_server_time(stub):
    response = stub.GetTime(clock_sync_pb2.TimeRequest(client_time=int(time.time() * 1000)))
    return response.server_time

def update_local_time(stub, local_time):
    response = stub.UpdateTime(clock_sync_pb2.TimeRequest(client_time=local_time))
    return response.server_time

def format_time(timestamp):
        return datetime.fromtimestamp(timestamp/1000).strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]
        # return datetime.utcfromtimestamp(timestamp / 1000).strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]

def run_client():
    channel = grpc.insecure_channel("localhost:50051")
    stub = clock_sync_pb2_grpc.ClockSyncStub(channel)

    server_time = get_server_time(stub)
    local_time = int(time.time() * 1000) - 10000

    server_time_formated = format_time(server_time)
    local_time_formated = format_time(local_time)

    print()
    print(f"Server Time: {server_time_formated}")
    print(f"Local Time: {local_time_formated}")

    updated_time = update_local_time(stub, local_time)

    updated_time_formated = format_time(updated_time)

    print(f"Updated Time: {updated_time_formated}")
    print()
    time.sleep(5)

if __name__ == "__main__":
    run_client()
