from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NotSupported: _ClassVar[DataType]
    Text: _ClassVar[DataType]
    Image: _ClassVar[DataType]
NotSupported: DataType
Text: DataType
Image: DataType

class NDarray(_message.Message):
    __slots__ = ("shape", "data")
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    shape: _containers.RepeatedScalarFieldContainer[int]
    data: bytes
    def __init__(self, shape: _Optional[_Iterable[int]] = ..., data: _Optional[bytes] = ...) -> None: ...

class RawData(_message.Message):
    __slots__ = ("type", "data")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    type: DataType
    data: bytes
    def __init__(self, type: _Optional[_Union[DataType, str]] = ..., data: _Optional[bytes] = ...) -> None: ...

class ListOfRawData(_message.Message):
    __slots__ = ("arrays",)
    ARRAYS_FIELD_NUMBER: _ClassVar[int]
    arrays: _containers.RepeatedCompositeFieldContainer[RawData]
    def __init__(self, arrays: _Optional[_Iterable[_Union[RawData, _Mapping]]] = ...) -> None: ...

class ListOfEncodedData(_message.Message):
    __slots__ = ("arrays",)
    ARRAYS_FIELD_NUMBER: _ClassVar[int]
    arrays: _containers.RepeatedCompositeFieldContainer[NDarray]
    def __init__(self, arrays: _Optional[_Iterable[_Union[NDarray, _Mapping]]] = ...) -> None: ...
