# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/duration.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from ext_libs.google.protobuf import descriptor as _descriptor
from ext_libs.google.protobuf import message as _message
from ext_libs.google.protobuf import reflection as _reflection
from ext_libs.google.protobuf import symbol_database as _symbol_database
from ext_libs.google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/duration.proto',
  package='google.protobuf',
  syntax='proto3',
  serialized_pb=_b('\n\x1egoogle/protobuf/duration.proto\x12\x0fgoogle.protobuf\"*\n\x08\x44uration\x12\x0f\n\x07seconds\x18\x01 \x01(\x03\x12\r\n\x05nanos\x18\x02 \x01(\x05\x42|\n\x13\x63om.google.protobufB\rDurationProtoP\x01Z*github.com/golang/protobuf/ptypes/duration\xa0\x01\x01\xa2\x02\x03GPB\xaa\x02\x1eGoogle.Protobuf.WellKnownTypesb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DURATION = _descriptor.Descriptor(
  name='Duration',
  full_name='google.protobuf.Duration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seconds', full_name='google.protobuf.Duration.seconds', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nanos', full_name='google.protobuf.Duration.nanos', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['Duration'] = _DURATION

Duration = _reflection.GeneratedProtocolMessageType('Duration', (_message.Message,), dict(
  DESCRIPTOR = _DURATION,
  __module__ = 'google.protobuf.duration_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Duration)
  ))
_sym_db.RegisterMessage(Duration)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.google.protobufB\rDurationProtoP\001Z*github.com/golang/protobuf/ptypes/duration\240\001\001\242\002\003GPB\252\002\036Google.Protobuf.WellKnownTypes'))
# @@protoc_insertion_point(module_scope)
