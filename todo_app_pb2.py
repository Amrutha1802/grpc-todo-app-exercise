# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo_app.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0etodo_app.proto\":\n\x04Todo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x17\n\x06status\x18\x03 \x01(\x0e\x32\x07.Status\"\x15\n\x13ListAllTodosRequest\",\n\x14ListAllTodosResponse\x12\x14\n\x05todos\x18\x01 \x03(\x0b\x32\x05.Todo*<\n\x06Status\x12\x14\n\x10UNDEFINED_STATUS\x10\x00\x12\x0e\n\nINCOMPLETE\x10\x01\x12\x0c\n\x08\x43OMPLETE\x10\x02\x32g\n\x0bTodoService\x12=\n\x0cListAllTodos\x12\x14.ListAllTodosRequest\x1a\x15.ListAllTodosResponse\"\x00\x12\x19\n\x07\x41\x64\x64Todo\x12\x05.Todo\x1a\x05.Todo\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'todo_app_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_STATUS']._serialized_start=147
  _globals['_STATUS']._serialized_end=207
  _globals['_TODO']._serialized_start=18
  _globals['_TODO']._serialized_end=76
  _globals['_LISTALLTODOSREQUEST']._serialized_start=78
  _globals['_LISTALLTODOSREQUEST']._serialized_end=99
  _globals['_LISTALLTODOSRESPONSE']._serialized_start=101
  _globals['_LISTALLTODOSRESPONSE']._serialized_end=145
  _globals['_TODOSERVICE']._serialized_start=209
  _globals['_TODOSERVICE']._serialized_end=312
# @@protoc_insertion_point(module_scope)
