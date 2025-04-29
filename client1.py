from flask import Flask, request
import grpc
import commonai_pb2
import commonai_pb2_grpc

app = Flask(__name__)

@app.route('/forward_pass', methods=['POST'])
def forward_pass():
    prompt = request.form['prompt']

    # Simulate partial forward pass (delay)
    print("[Client1] Received prompt. Forwarding via gRPC to Client2.")

    # gRPC call to client2
    with grpc.insecure_channel('localhost:60051') as channel:
        stub = commonai_pb2_grpc.InferenceServiceStub(channel)
        response = stub.Generate(commonai_pb2.PromptRequest(prompt=prompt))

    return response.output

if __name__ == '__main__':
    app.run(port=5001)
