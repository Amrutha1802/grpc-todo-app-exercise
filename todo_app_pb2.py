# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo_app.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0etodo_app.proto\"K\n\x04Todo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\r\n\x05title\x18\x03 \x01(\t\x12\x17\n\x06status\x18\x04 \x01(\x0e\x32\x07.Status\"\x12\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\"!\n\tUserTodos\x12\x14\n\x05todos\x18\x01 \x03(\x0b\x32\x05.Todo\"\x0f\n\rEmptyResponse\"\x1f\n\x11\x44\x65leteTodoRequest\x12\n\n\x02id\x18\x01 \x01(\x05*<\n\x06Status\x12\x14\n\x10UNDEFINED_STATUS\x10\x00\x12\x0e\n\nINCOMPLETE\x10\x01\x12\x0c\n\x08\x43OMPLETE\x10\x02\x32\x9d\x01\n\x0bTodoService\x12#\n\x0cGetUserTodos\x12\x05.User\x1a\n.UserTodos\"\x00\x12\x19\n\x07\x41\x64\x64Todo\x12\x05.Todo\x1a\x05.Todo\"\x00\x12\x32\n\nDeleteTodo\x12\x12.DeleteTodoRequest\x1a\x0e.EmptyResponse\"\x00\x12\x1a\n\x08\x45\x64itTodo\x12\x05.Todo\x1a\x05.Todo\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'todo_app_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_STATUS']._serialized_start=200
  _globals['_STATUS']._serialized_end=260
  _globals['_TODO']._serialized_start=18
  _globals['_TODO']._serialized_end=93
  _globals['_USER']._serialized_start=95
  _globals['_USER']._serialized_end=113
  _globals['_USERTODOS']._serialized_start=115
  _globals['_USERTODOS']._serialized_end=148
  _globals['_EMPTYRESPONSE']._serialized_start=150
  _globals['_EMPTYRESPONSE']._serialized_end=165
  _globals['_DELETETODOREQUEST']._serialized_start=167
  _globals['_DELETETODOREQUEST']._serialized_end=198
  _globals['_TODOSERVICE']._serialized_start=263
  _globals['_TODOSERVICE']._serialized_end=420
# @@protoc_insertion_point(module_scope)
