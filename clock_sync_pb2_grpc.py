# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import clock_sync_pb2 as clock__sync__pb2


class ClockSyncStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTime = channel.unary_unary(
                '/ClockSync/GetTime',
                request_serializer=clock__sync__pb2.TimeRequest.SerializeToString,
                response_deserializer=clock__sync__pb2.TimeResponse.FromString,
                )
        self.UpdateTime = channel.unary_unary(
                '/ClockSync/UpdateTime',
                request_serializer=clock__sync__pb2.TimeRequest.SerializeToString,
                response_deserializer=clock__sync__pb2.TimeResponse.FromString,
                )


class ClockSyncServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClockSyncServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTime,
                    request_deserializer=clock__sync__pb2.TimeRequest.FromString,
                    response_serializer=clock__sync__pb2.TimeResponse.SerializeToString,
            ),
            'UpdateTime': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTime,
                    request_deserializer=clock__sync__pb2.TimeRequest.FromString,
                    response_serializer=clock__sync__pb2.TimeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ClockSync', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClockSync(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClockSync/GetTime',
            clock__sync__pb2.TimeRequest.SerializeToString,
            clock__sync__pb2.TimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClockSync/UpdateTime',
            clock__sync__pb2.TimeRequest.SerializeToString,
            clock__sync__pb2.TimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)