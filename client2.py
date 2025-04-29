from concurrent import futures
import grpc
import time
from llama_cpp import Llama
import commonai_pb2
import commonai_pb2_grpc

# Load your GGUF model
llm = Llama(model_path="Llama/Meta-Llama-3-8B-Instruct.Q4_0.gguf")

SYSTEM_PROMPT = (
    "You are part of CommonAI — a decentralized inference system that enables students, researchers, "
    "and innovators to collaboratively run large language models like LLaMA 3 8B using pooled idle computing resources. "
    "Your role is to assist in partial model inference across distributed clients by forwarding and processing segments "
    "of the model as assigned by the server.\n\n"
)

class InferenceService(commonai_pb2_grpc.InferenceServiceServicer):
    def Generate(self, request, context):
        print("[Client2] Generating output...")
        result = llm(SYSTEM_PROMPT+request.prompt)
        output = result["choices"][0]["text"]  # ✅ Correct way to extract text
        return commonai_pb2.PromptResponse(output=output)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    commonai_pb2_grpc.add_InferenceServiceServicer_to_server(InferenceService(), server)
    server.add_insecure_port('[::]:60051')
    server.start()
    print("[Client2] gRPC server started at port 60051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
