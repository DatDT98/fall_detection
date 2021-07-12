PROTOC_OUT=proto/
PROTOS=$(find ./protobufs | grep "\.proto$")
for p in $PROTOS; do
  python -m grpc.tools.protoc -I . --python_out=. --grpc_python_out=. $p
done
