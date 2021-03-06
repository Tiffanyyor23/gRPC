# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: NPAF.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='NPAF.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nNPAF.proto\"\x8e\x01\n\x06Routes\x12\x1b\n\x03\x61\x66i\x18\x01 \x01(\x0e\x32\x0e.AddressFamily\x12\x1f\n\x04safi\x18\x02 \x01(\x0e\x32\x11.SubAddressFamily\x12\x1c\n\x05route\x18\x03 \x03(\x0b\x32\r.Routes.Route\x1a(\n\x05Route\x12\r\n\x05route\x18\x01 \x01(\t\x12\x10\n\x08next_hop\x18\x02 \x01(\t\"\\\n\x0c\x44\x65viceRoutes\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12\x15\n\rroutes_number\x18\x03 \x01(\x03\x12\x17\n\x06routes\x18\x04 \x01(\x0b\x32\x07.Routes\"^\n\x0cRouteRequest\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x1b\n\x03\x61\x66i\x18\x02 \x01(\x0e\x32\x0e.AddressFamily\x12\x1f\n\x04safi\x18\x03 \x01(\x0e\x32\x11.SubAddressFamily*D\n\rAddressFamily\x12\x08\n\x04IPV4\x10\x00\x12\x08\n\x04IPV6\x10\x01\x12\t\n\x05VPNV4\x10\x02\x12\t\n\x05VPNV6\x10\x03\x12\t\n\x05L2VPN\x10\x04*9\n\x10SubAddressFamily\x12\x0b\n\x07UNICAST\x10\x00\x12\r\n\tMULTICAST\x10\x01\x12\t\n\x05\x45VPN2\x10\x02\x32<\n\tRouteData\x12/\n\rCollectRoutes\x12\r.RouteRequest\x1a\r.DeviceRoutes\"\x00\x62\x06proto3'
)

_ADDRESSFAMILY = _descriptor.EnumDescriptor(
  name='AddressFamily',
  full_name='AddressFamily',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IPV4', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IPV6', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VPNV4', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VPNV6', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='L2VPN', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=349,
  serialized_end=417,
)
_sym_db.RegisterEnumDescriptor(_ADDRESSFAMILY)

AddressFamily = enum_type_wrapper.EnumTypeWrapper(_ADDRESSFAMILY)
_SUBADDRESSFAMILY = _descriptor.EnumDescriptor(
  name='SubAddressFamily',
  full_name='SubAddressFamily',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNICAST', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULTICAST', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EVPN2', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=419,
  serialized_end=476,
)
_sym_db.RegisterEnumDescriptor(_SUBADDRESSFAMILY)

SubAddressFamily = enum_type_wrapper.EnumTypeWrapper(_SUBADDRESSFAMILY)
IPV4 = 0
IPV6 = 1
VPNV4 = 2
VPNV6 = 3
L2VPN = 4
UNICAST = 0
MULTICAST = 1
EVPN2 = 2



_ROUTES_ROUTE = _descriptor.Descriptor(
  name='Route',
  full_name='Routes.Route',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='route', full_name='Routes.Route.route', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_hop', full_name='Routes.Route.next_hop', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=117,
  serialized_end=157,
)

_ROUTES = _descriptor.Descriptor(
  name='Routes',
  full_name='Routes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='afi', full_name='Routes.afi', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='safi', full_name='Routes.safi', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='route', full_name='Routes.route', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ROUTES_ROUTE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=157,
)


_DEVICEROUTES = _descriptor.Descriptor(
  name='DeviceRoutes',
  full_name='DeviceRoutes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='DeviceRoutes.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='DeviceRoutes.hostname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='routes_number', full_name='DeviceRoutes.routes_number', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='routes', full_name='DeviceRoutes.routes', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=159,
  serialized_end=251,
)


_ROUTEREQUEST = _descriptor.Descriptor(
  name='RouteRequest',
  full_name='RouteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostname', full_name='RouteRequest.hostname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='afi', full_name='RouteRequest.afi', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='safi', full_name='RouteRequest.safi', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=253,
  serialized_end=347,
)

_ROUTES_ROUTE.containing_type = _ROUTES
_ROUTES.fields_by_name['afi'].enum_type = _ADDRESSFAMILY
_ROUTES.fields_by_name['safi'].enum_type = _SUBADDRESSFAMILY
_ROUTES.fields_by_name['route'].message_type = _ROUTES_ROUTE
_DEVICEROUTES.fields_by_name['routes'].message_type = _ROUTES
_ROUTEREQUEST.fields_by_name['afi'].enum_type = _ADDRESSFAMILY
_ROUTEREQUEST.fields_by_name['safi'].enum_type = _SUBADDRESSFAMILY
DESCRIPTOR.message_types_by_name['Routes'] = _ROUTES
DESCRIPTOR.message_types_by_name['DeviceRoutes'] = _DEVICEROUTES
DESCRIPTOR.message_types_by_name['RouteRequest'] = _ROUTEREQUEST
DESCRIPTOR.enum_types_by_name['AddressFamily'] = _ADDRESSFAMILY
DESCRIPTOR.enum_types_by_name['SubAddressFamily'] = _SUBADDRESSFAMILY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Routes = _reflection.GeneratedProtocolMessageType('Routes', (_message.Message,), {

  'Route' : _reflection.GeneratedProtocolMessageType('Route', (_message.Message,), {
    'DESCRIPTOR' : _ROUTES_ROUTE,
    '__module__' : 'NPAF_pb2'
    # @@protoc_insertion_point(class_scope:Routes.Route)
    })
  ,
  'DESCRIPTOR' : _ROUTES,
  '__module__' : 'NPAF_pb2'
  # @@protoc_insertion_point(class_scope:Routes)
  })
_sym_db.RegisterMessage(Routes)
_sym_db.RegisterMessage(Routes.Route)

DeviceRoutes = _reflection.GeneratedProtocolMessageType('DeviceRoutes', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEROUTES,
  '__module__' : 'NPAF_pb2'
  # @@protoc_insertion_point(class_scope:DeviceRoutes)
  })
_sym_db.RegisterMessage(DeviceRoutes)

RouteRequest = _reflection.GeneratedProtocolMessageType('RouteRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEREQUEST,
  '__module__' : 'NPAF_pb2'
  # @@protoc_insertion_point(class_scope:RouteRequest)
  })
_sym_db.RegisterMessage(RouteRequest)



_ROUTEDATA = _descriptor.ServiceDescriptor(
  name='RouteData',
  full_name='RouteData',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=478,
  serialized_end=538,
  methods=[
  _descriptor.MethodDescriptor(
    name='CollectRoutes',
    full_name='RouteData.CollectRoutes',
    index=0,
    containing_service=None,
    input_type=_ROUTEREQUEST,
    output_type=_DEVICEROUTES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROUTEDATA)

DESCRIPTOR.services_by_name['RouteData'] = _ROUTEDATA

# @@protoc_insertion_point(module_scope)
