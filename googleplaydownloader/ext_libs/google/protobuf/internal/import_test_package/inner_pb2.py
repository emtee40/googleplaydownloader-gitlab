# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/internal/import_test_package/inner.proto

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
  name='google/protobuf/internal/import_test_package/inner.proto',
  package='google.protobuf.python.internal.import_test_package',
  syntax='proto2',
  serialized_pb=_b('\n8google/protobuf/internal/import_test_package/inner.proto\x12\x33google.protobuf.python.internal.import_test_package\"\x1a\n\x05Inner\x12\x11\n\x05value\x18\x01 \x01(\x05:\x02\x35\x37')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INNER = _descriptor.Descriptor(
  name='Inner',
  full_name='google.protobuf.python.internal.import_test_package.Inner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='google.protobuf.python.internal.import_test_package.Inner.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=57,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=139,
)

DESCRIPTOR.message_types_by_name['Inner'] = _INNER

Inner = _reflection.GeneratedProtocolMessageType('Inner', (_message.Message,), dict(
  DESCRIPTOR = _INNER,
  __module__ = 'google.protobuf.internal.import_test_package.inner_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.import_test_package.Inner)
  ))
_sym_db.RegisterMessage(Inner)


# @@protoc_insertion_point(module_scope)
