from twwhatever.demo import service_pb2_grpc
from twwhatever.demo import message_pb2

class Demo(service_pb2_grpc.DemoServiceServicer):
    def Function(self, request, context):
        return message_pb2.DemoMessage(m='Hi there!')

if __name__ == '__main__':
    demo = Demo()
    print(demo.Function(None, None))
