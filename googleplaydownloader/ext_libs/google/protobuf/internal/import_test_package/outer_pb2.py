# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/internal/import_test_package/outer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from ext_libs.google.protobuf import descriptor as _descriptor
from ext_libs.google.protobuf import message as _message
from ext_libs.google.protobuf import reflection as _reflection
from ext_libs.google.protobuf import symbol_database as _symbol_database
from ext_libs.google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ext_libs.google.protobuf.internal.import_test_package import inner_pb2 as google_dot_protobuf_dot_internal_dot_import__test__package_dot_inner__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/internal/import_test_package/outer.proto',
  package='google.protobuf.python.internal.import_test_package',
  syntax='proto2',
  serialized_pb=_b('\n8google/protobuf/internal/import_test_package/outer.proto\x12\x33google.protobuf.python.internal.import_test_package\x1a\x38google/protobuf/internal/import_test_package/inner.proto\"R\n\x05Outer\x12I\n\x05inner\x18\x01 \x01(\x0b\x32:.google.protobuf.python.internal.import_test_package.Inner')
  ,
  dependencies=[google_dot_protobuf_dot_internal_dot_import__test__package_dot_inner__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_OUTER = _descriptor.Descriptor(
  name='Outer',
  full_name='google.protobuf.python.internal.import_test_package.Outer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inner', full_name='google.protobuf.python.internal.import_test_package.Outer.inner', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=171,
  serialized_end=253,
)

_OUTER.fields_by_name['inner'].message_type = google_dot_protobuf_dot_internal_dot_import__test__package_dot_inner__pb2._INNER
DESCRIPTOR.message_types_by_name['Outer'] = _OUTER

Outer = _reflection.GeneratedProtocolMessageType('Outer', (_message.Message,), dict(
  DESCRIPTOR = _OUTER,
  __module__ = 'google.protobuf.internal.import_test_package.outer_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.import_test_package.Outer)
  ))
_sym_db.RegisterMessage(Outer)


# @@protoc_insertion_point(module_scope)
