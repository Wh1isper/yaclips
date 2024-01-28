#!/usr/bin/env bash
set -e

pip install "grpcio-tools>=1.15.0"

echo "Generating main package's proto..."
python -m grpc_tools.protoc -I./proto --pyi_out=./yaclips/proto --python_out=./yaclips/proto --grpc_python_out=./yaclips/proto ./proto/yaclips.proto
2to3 -n -w ./yaclips/proto/*_pb2*

echo "Generating client package's proto..."
python -m grpc_tools.protoc -I./proto --pyi_out=./yaclips/client/proto --python_out=./yaclips/client/proto --grpc_python_out=./yaclips/client/proto ./proto/yaclips.proto

