#!/usr/bin/env bash
set -e

pip install "grpcio-tools>=1.15.0"
python -m grpc_tools.protoc -I./proto --pyi_out=./yaclips/proto --python_out=./yaclips/proto --grpc_python_out=./yaclips/proto ./proto/yaclips.proto
2to3 -n -w ./yaclips/proto/*_pb2*
