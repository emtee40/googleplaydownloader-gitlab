# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/unittest_mset_wire_format.proto

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
  name='google/protobuf/unittest_mset_wire_format.proto',
  package='proto2_wireformat_unittest',
  syntax='proto2',
  serialized_pb=_b('\n/google/protobuf/unittest_mset_wire_format.proto\x12\x1aproto2_wireformat_unittest\"\x1e\n\x0eTestMessageSet*\x08\x08\x04\x10\xff\xff\xff\xff\x07:\x02\x08\x01\"d\n!TestMessageSetWireFormatContainer\x12?\n\x0bmessage_set\x18\x01 \x01(\x0b\x32*.proto2_wireformat_unittest.TestMessageSetB)H\x01\xf8\x01\x01\xaa\x02!Google.ProtocolBuffers.TestProtos')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TESTMESSAGESET = _descriptor.Descriptor(
  name='TestMessageSet',
  full_name='proto2_wireformat_unittest.TestMessageSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\010\001')),
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(4, 2147483647), ],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=109,
)


_TESTMESSAGESETWIREFORMATCONTAINER = _descriptor.Descriptor(
  name='TestMessageSetWireFormatContainer',
  full_name='proto2_wireformat_unittest.TestMessageSetWireFormatContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_set', full_name='proto2_wireformat_unittest.TestMessageSetWireFormatContainer.message_set', index=0,
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
  serialized_start=111,
  serialized_end=211,
)

_TESTMESSAGESETWIREFORMATCONTAINER.fields_by_name['message_set'].message_type = _TESTMESSAGESET
DESCRIPTOR.message_types_by_name['TestMessageSet'] = _TESTMESSAGESET
DESCRIPTOR.message_types_by_name['TestMessageSetWireFormatContainer'] = _TESTMESSAGESETWIREFORMATCONTAINER

TestMessageSet = _reflection.GeneratedProtocolMessageType('TestMessageSet', (_message.Message,), dict(
  DESCRIPTOR = _TESTMESSAGESET,
  __module__ = 'google.protobuf.unittest_mset_wire_format_pb2'
  # @@protoc_insertion_point(class_scope:proto2_wireformat_unittest.TestMessageSet)
  ))
_sym_db.RegisterMessage(TestMessageSet)

TestMessageSetWireFormatContainer = _reflection.GeneratedProtocolMessageType('TestMessageSetWireFormatContainer', (_message.Message,), dict(
  DESCRIPTOR = _TESTMESSAGESETWIREFORMATCONTAINER,
  __module__ = 'google.protobuf.unittest_mset_wire_format_pb2'
  # @@protoc_insertion_point(class_scope:proto2_wireformat_unittest.TestMessageSetWireFormatContainer)
  ))
_sym_db.RegisterMessage(TestMessageSetWireFormatContainer)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001\370\001\001\252\002!Google.ProtocolBuffers.TestProtos'))
_TESTMESSAGESET.has_options = True
_TESTMESSAGESET._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\010\001'))
# @@protoc_insertion_point(module_scope)
