# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yaclips.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\ryaclips.proto"&\n\x07NDarray\x12\r\n\x05shape\x18\x01 \x03(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c"0\n\x07RawData\x12\x17\n\x04type\x18\x01 \x01(\x0e\x32\t.DataType\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c")\n\rListOfRawData\x12\x18\n\x06\x61rrays\x18\x01 \x03(\x0b\x32\x08.RawData"-\n\x11ListOfEncodedData\x12\x18\n\x06\x61rrays\x18\x01 \x03(\x0b\x32\x08.NDarray*1\n\x08\x44\x61taType\x12\x10\n\x0cNotSupported\x10\x00\x12\x08\n\x04Text\x10\x01\x12\t\n\x05Image\x10\x02\x32\x34\n\x04\x63lip\x12,\n\x06\x65ncode\x12\x0e.ListOfRawData\x1a\x12.ListOfEncodedDatab\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "yaclips_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_DATATYPE"]._serialized_start = 197
    _globals["_DATATYPE"]._serialized_end = 246
    _globals["_NDARRAY"]._serialized_start = 17
    _globals["_NDARRAY"]._serialized_end = 55
    _globals["_RAWDATA"]._serialized_start = 57
    _globals["_RAWDATA"]._serialized_end = 105
    _globals["_LISTOFRAWDATA"]._serialized_start = 107
    _globals["_LISTOFRAWDATA"]._serialized_end = 148
    _globals["_LISTOFENCODEDDATA"]._serialized_start = 150
    _globals["_LISTOFENCODEDDATA"]._serialized_end = 195
    _globals["_CLIP"]._serialized_start = 248
    _globals["_CLIP"]._serialized_end = 300
# @@protoc_insertion_point(module_scope)
