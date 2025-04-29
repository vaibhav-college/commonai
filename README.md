# 🧠 CommonAI: Distributed Forward Pass for LLaMA LLM

## Team Members
- Rahul (Lead Developer & Architect)

## 📄 Project Description

**CommonAI** is an ethical and cost-effective solution to enable *distributed inference* of large language models (LLMs) like LLaMA 3 by splitting the forward pass across multiple low-resource clients. This project simulates true model layer splitting: `client1` processes the first portion of the model layers, and `client2` completes the rest, communicating through a coordinating `server`.

Unlike naive simulations, this implementation performs real computations of transformer layers, backed by native C++ code compiled into a shared library. It is the foundational prototype for a decentralized AI compute network accessible to researchers and students with limited resources.

## 📽️ Video Explanation
[🔗 Watch the demo & architecture walkthrough]()

> *(Replace this link with your actual video once recorded.)*

## 💻 Technologies Used
- **LLaMA 3 GGUF Model** via [`llama-cpp-python`](https://github.com/abetlen/llama-cpp-python)
- **gRPC** for cross-client communication
- **C++** for efficient transformer layer computations
- **Python** for orchestration and glue code
- **NumPy** for numerical data manipulation
- **msgpack** for fast binary serialization
- **CFFI** for interfacing Python with C++

---

## 🚀 Steps to Run the Project

### 1. 📦 Prerequisites

- Python 3.8+
- g++ compiler (Linux/macOS) or MSVC (Windows)
- `protoc` compiler (for gRPC)
- Python packages:
  ```bash
  pip install grpcio grpcio-tools numpy cffi msgpack

Steps to run:

1- Generate gRPC code with commonai.proto file- python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. commonai.proto
2- Start the server- python server.py
3- Run the clients: (BEWARE! DO NOT RUN THIS ON AN UNDERPOWERED LAPTOP AS THIS WILL PUT STRESS YOUR LAPTOP AS INITIAL STARTING UP)
python client1.py
python client2.py
4- Open localhost to interact with server and distributed computing
