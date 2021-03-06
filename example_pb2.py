# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rexample.proto\"#\n\x0e\x45xampleRequest\x12\x11\n\tinmessage\x18\x01 \x01(\t\"\"\n\x0c\x45xampleReply\x12\x12\n\noutmessage\x18\x01 \x01(\t26\n\x03RPC\x12/\n\x0bMsgDelivery\x12\x0f.ExampleRequest\x1a\r.ExampleReply\"\x00\x62\x06proto3'
)




_EXAMPLEREQUEST = _descriptor.Descriptor(
  name='ExampleRequest',
  full_name='ExampleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='inmessage', full_name='ExampleRequest.inmessage', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=52,
)


_EXAMPLEREPLY = _descriptor.Descriptor(
  name='ExampleReply',
  full_name='ExampleReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='outmessage', full_name='ExampleReply.outmessage', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['ExampleRequest'] = _EXAMPLEREQUEST
DESCRIPTOR.message_types_by_name['ExampleReply'] = _EXAMPLEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExampleRequest = _reflection.GeneratedProtocolMessageType('ExampleRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXAMPLEREQUEST,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:ExampleRequest)
  })
_sym_db.RegisterMessage(ExampleRequest)

ExampleReply = _reflection.GeneratedProtocolMessageType('ExampleReply', (_message.Message,), {
  'DESCRIPTOR' : _EXAMPLEREPLY,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:ExampleReply)
  })
_sym_db.RegisterMessage(ExampleReply)



_RPC = _descriptor.ServiceDescriptor(
  name='RPC',
  full_name='RPC',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=90,
  serialized_end=144,
  methods=[
  _descriptor.MethodDescriptor(
    name='MsgDelivery',
    full_name='RPC.MsgDelivery',
    index=0,
    containing_service=None,
    input_type=_EXAMPLEREQUEST,
    output_type=_EXAMPLEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RPC)

DESCRIPTOR.services_by_name['RPC'] = _RPC

# @@protoc_insertion_point(module_scope)
