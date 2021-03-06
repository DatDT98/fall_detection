# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protobufs import fallalert_pb2 as protobufs_dot_fallalert__pb2


class FallAlarmServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Alarm = channel.unary_stream(
                '/FallAlarmService/Alarm',
                request_serializer=protobufs_dot_fallalert__pb2.FallAlarmRequest.SerializeToString,
                response_deserializer=protobufs_dot_fallalert__pb2.FallAlarmResponse.FromString,
                )


class FallAlarmServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Alarm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FallAlarmServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Alarm': grpc.unary_stream_rpc_method_handler(
                    servicer.Alarm,
                    request_deserializer=protobufs_dot_fallalert__pb2.FallAlarmRequest.FromString,
                    response_serializer=protobufs_dot_fallalert__pb2.FallAlarmResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FallAlarmService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FallAlarmService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Alarm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/FallAlarmService/Alarm',
            protobufs_dot_fallalert__pb2.FallAlarmRequest.SerializeToString,
            protobufs_dot_fallalert__pb2.FallAlarmResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
