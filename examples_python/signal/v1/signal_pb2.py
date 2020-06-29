# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: signal/v1/signal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='signal/v1/signal.proto',
  package='signal.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16signal/v1/signal.proto\x12\tsignal.v1\"\xa4\x04\n\x06Signal\x12*\n\x07\x63ommand\x18\x01 \x01(\x0b\x32\x19.signal.v1.Signal.Command\x1a\xf4\x01\n\x07\x43ommand\x12\'\n\x04mode\x18\x01 \x01(\x0e\x32\x19.signal.v1.Signal.CmdMode\x12\'\n\x04type\x18\x02 \x01(\x0e\x32\x19.signal.v1.Signal.CmdType\x12\x12\n\nboard_name\x18\x03 \x01(\t\x12%\n\x08location\x18\x04 \x01(\x0b\x32\x13.signal.v1.Location\x12\x1b\n\x03pin\x18\x05 \x01(\x0b\x32\x0e.signal.v1.Pin\x12\x1b\n\x03pwm\x18\x06 \x01(\x0b\x32\x0e.signal.v1.PWM\x12\"\n\x07sensors\x18\x07 \x03(\x0b\x32\x11.signal.v1.Sensor\"G\n\x07\x43mdMode\x12\x18\n\x14\x43MD_MODE_UNSPECIFIED\x10\x00\x12\x10\n\x0c\x43MD_MODE_GET\x10\x01\x12\x10\n\x0c\x43MD_MODE_SET\x10\x02\"\xad\x01\n\x07\x43mdType\x12\x18\n\x14\x43MD_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11\x43MD_TYPE_LOCATION\x10\x01\x12\x14\n\x10\x43MD_TYPE_BATTERY\x10\x02\x12\x16\n\x12\x43MD_TYPE_PIN_VALUE\x10\x03\x12\x15\n\x11\x43MD_TYPE_PIN_MODE\x10\x04\x12\x17\n\x13\x43MD_TYPE_PWM_OUTPUT\x10\x05\x12\x13\n\x0f\x43MD_TYPE_SENSOR\x10\x06\"\xe2\x07\n\x06Sensor\x12$\n\x04type\x18\x01 \x01(\x0b\x32\x16.signal.v1.Sensor.Type\x12&\n\x05\x65vent\x18\x02 \x01(\x0b\x32\x17.signal.v1.Sensor.Event\x1a\xb1\x05\n\x04Type\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tsensor_id\x18\x02 \x01(\x05\x12/\n\x04type\x18\x03 \x01(\x0e\x32!.signal.v1.Sensor.Type.SensorType\x12\x11\n\tmax_value\x18\x04 \x01(\x02\x12\x11\n\tmin_value\x18\x05 \x01(\x02\x12\x12\n\nresolution\x18\x06 \x01(\x02\x12\x1a\n\x12measurement_period\x18\x07 \x01(\x05\"\x80\x04\n\nSensorType\x12\x1b\n\x17SENSOR_TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19SENSOR_TYPE_ACCELEROMETER\x10\x01\x12\x1e\n\x1aSENSOR_TYPE_MAGNETIC_FIELD\x10\x02\x12\x1b\n\x17SENSOR_TYPE_ORIENTATION\x10\x03\x12\x19\n\x15SENSOR_TYPE_GYROSCOPE\x10\x04\x12\x15\n\x11SENSOR_TYPE_LIGHT\x10\x05\x12\x18\n\x14SENSOR_TYPE_PRESSURE\x10\x06\x12\x19\n\x15SENSOR_TYPE_PROXIMITY\x10\x08\x12\x17\n\x13SENSOR_TYPE_GRAVITY\x10\t\x12#\n\x1fSENSOR_TYPE_LINEAR_ACCELERATION\x10\n\x12\x1f\n\x1bSENSOR_TYPE_ROTATION_VECTOR\x10\x0b\x12!\n\x1dSENSOR_TYPE_RELATIVE_HUMIDITY\x10\x0c\x12#\n\x1fSENSOR_TYPE_AMBIENT_TEMPERATURE\x10\r\x12\"\n\x1eSENSOR_TYPE_OBJECT_TEMPERATURE\x10\x0e\x12\x17\n\x13SENSOR_TYPE_VOLTAGE\x10\x0f\x12\x17\n\x13SENSOR_TYPE_CURRENT\x10\x10\x12\x15\n\x11SENSOR_TYPE_COLOR\x10\x11\x1a\xd5\x01\n\x05\x45vent\x12\x11\n\tsensor_id\x18\x01 \x01(\x05\x12\x13\n\x0bsensor_type\x18\x02 \x01(\x05\x12\x11\n\ttimestamp\x18\x03 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x02\x12\x13\n\x0btemperature\x18\x05 \x01(\x02\x12\x10\n\x08\x64istance\x18\x06 \x01(\x02\x12\r\n\x05light\x18\x07 \x01(\x02\x12\x10\n\x08pressure\x18\x08 \x01(\x02\x12\x19\n\x11relative_humidity\x18\t \x01(\x02\x12\x0f\n\x07\x63urrent\x18\n \x01(\x02\x12\x0f\n\x07voltage\x18\x0b \x01(\x02\"A\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x02\x12\x11\n\tlongitude\x18\x02 \x01(\x02\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x02\"\x85\x03\n\x03Pin\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x04mode\x18\x02 \x01(\x0e\x32\x13.signal.v1.Pin.Mode\x12+\n\tdirection\x18\x03 \x01(\x0e\x32\x18.signal.v1.Pin.Direction\x12!\n\x04pull\x18\x04 \x01(\x0e\x32\x13.signal.v1.Pin.Pull\x12\r\n\x05value\x18\x05 \x01(\t\x12\x0e\n\x06period\x18\x06 \x01(\x05\"Q\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bMODE_ANALOG\x10\x01\x12\x10\n\x0cMODE_DIGITAL\x10\x02\x12\x10\n\x0cMODE_PULL_UP\x10\x03\"Q\n\tDirection\x12\x19\n\x15\x44IRECTION_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x44IRECTION_INPUT\x10\x01\x12\x14\n\x10\x44IRECTION_OUTPUT\x10\x02\"8\n\x04Pull\x12\x14\n\x10PULL_UNSPECIFIED\x10\x00\x12\x0b\n\x07PULL_UP\x10\x01\x12\r\n\tPULL_DOWN\x10\x02\">\n\x03PWM\x12\x10\n\x08pin_name\x18\x01 \x01(\t\x12\x12\n\nduty_cycle\x18\x02 \x01(\x05\x12\x11\n\tfrequency\x18\x03 \x01(\x05\x62\x06proto3'
)



_SIGNAL_CMDMODE = _descriptor.EnumDescriptor(
  name='CmdMode',
  full_name='signal.v1.Signal.CmdMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CMD_MODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_MODE_GET', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_MODE_SET', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=339,
  serialized_end=410,
)
_sym_db.RegisterEnumDescriptor(_SIGNAL_CMDMODE)

_SIGNAL_CMDTYPE = _descriptor.EnumDescriptor(
  name='CmdType',
  full_name='signal.v1.Signal.CmdType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_LOCATION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_BATTERY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_PIN_VALUE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_PIN_MODE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_PWM_OUTPUT', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_TYPE_SENSOR', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=413,
  serialized_end=586,
)
_sym_db.RegisterEnumDescriptor(_SIGNAL_CMDTYPE)

_SENSOR_TYPE_SENSORTYPE = _descriptor.EnumDescriptor(
  name='SensorType',
  full_name='signal.v1.Sensor.Type.SensorType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_ACCELEROMETER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_MAGNETIC_FIELD', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_ORIENTATION', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_GYROSCOPE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_LIGHT', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_PRESSURE', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_PROXIMITY', index=7, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_GRAVITY', index=8, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_LINEAR_ACCELERATION', index=9, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_ROTATION_VECTOR', index=10, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_RELATIVE_HUMIDITY', index=11, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_AMBIENT_TEMPERATURE', index=12, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_OBJECT_TEMPERATURE', index=13, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_VOLTAGE', index=14, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_CURRENT', index=15, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SENSOR_TYPE_COLOR', index=16, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=855,
  serialized_end=1367,
)
_sym_db.RegisterEnumDescriptor(_SENSOR_TYPE_SENSORTYPE)

_PIN_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='signal.v1.Pin.Mode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MODE_ANALOG', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MODE_DIGITAL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MODE_PULL_UP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1820,
  serialized_end=1901,
)
_sym_db.RegisterEnumDescriptor(_PIN_MODE)

_PIN_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='signal.v1.Pin.Direction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIRECTION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIRECTION_INPUT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIRECTION_OUTPUT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1903,
  serialized_end=1984,
)
_sym_db.RegisterEnumDescriptor(_PIN_DIRECTION)

_PIN_PULL = _descriptor.EnumDescriptor(
  name='Pull',
  full_name='signal.v1.Pin.Pull',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PULL_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PULL_UP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PULL_DOWN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1986,
  serialized_end=2042,
)
_sym_db.RegisterEnumDescriptor(_PIN_PULL)


_SIGNAL_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='signal.v1.Signal.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='signal.v1.Signal.Command.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='signal.v1.Signal.Command.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='board_name', full_name='signal.v1.Signal.Command.board_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='signal.v1.Signal.Command.location', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pin', full_name='signal.v1.Signal.Command.pin', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pwm', full_name='signal.v1.Signal.Command.pwm', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensors', full_name='signal.v1.Signal.Command.sensors', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=93,
  serialized_end=337,
)

_SIGNAL = _descriptor.Descriptor(
  name='Signal',
  full_name='signal.v1.Signal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='signal.v1.Signal.command', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SIGNAL_COMMAND, ],
  enum_types=[
    _SIGNAL_CMDMODE,
    _SIGNAL_CMDTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=586,
)


_SENSOR_TYPE = _descriptor.Descriptor(
  name='Type',
  full_name='signal.v1.Sensor.Type',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='signal.v1.Sensor.Type.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensor_id', full_name='signal.v1.Sensor.Type.sensor_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='signal.v1.Sensor.Type.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_value', full_name='signal.v1.Sensor.Type.max_value', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_value', full_name='signal.v1.Sensor.Type.min_value', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resolution', full_name='signal.v1.Sensor.Type.resolution', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='measurement_period', full_name='signal.v1.Sensor.Type.measurement_period', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SENSOR_TYPE_SENSORTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=678,
  serialized_end=1367,
)

_SENSOR_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='signal.v1.Sensor.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensor_id', full_name='signal.v1.Sensor.Event.sensor_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensor_type', full_name='signal.v1.Sensor.Event.sensor_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='signal.v1.Sensor.Event.timestamp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='signal.v1.Sensor.Event.data', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='signal.v1.Sensor.Event.temperature', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distance', full_name='signal.v1.Sensor.Event.distance', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='light', full_name='signal.v1.Sensor.Event.light', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pressure', full_name='signal.v1.Sensor.Event.pressure', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relative_humidity', full_name='signal.v1.Sensor.Event.relative_humidity', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current', full_name='signal.v1.Sensor.Event.current', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voltage', full_name='signal.v1.Sensor.Event.voltage', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=1370,
  serialized_end=1583,
)

_SENSOR = _descriptor.Descriptor(
  name='Sensor',
  full_name='signal.v1.Sensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='signal.v1.Sensor.type', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event', full_name='signal.v1.Sensor.event', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SENSOR_TYPE, _SENSOR_EVENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=589,
  serialized_end=1583,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='signal.v1.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='signal.v1.Location.latitude', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='signal.v1.Location.longitude', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='signal.v1.Location.altitude', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=1585,
  serialized_end=1650,
)


_PIN = _descriptor.Descriptor(
  name='Pin',
  full_name='signal.v1.Pin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='signal.v1.Pin.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='signal.v1.Pin.mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='signal.v1.Pin.direction', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pull', full_name='signal.v1.Pin.pull', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='signal.v1.Pin.value', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='period', full_name='signal.v1.Pin.period', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PIN_MODE,
    _PIN_DIRECTION,
    _PIN_PULL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1653,
  serialized_end=2042,
)


_PWM = _descriptor.Descriptor(
  name='PWM',
  full_name='signal.v1.PWM',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pin_name', full_name='signal.v1.PWM.pin_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duty_cycle', full_name='signal.v1.PWM.duty_cycle', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='signal.v1.PWM.frequency', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=2044,
  serialized_end=2106,
)

_SIGNAL_COMMAND.fields_by_name['mode'].enum_type = _SIGNAL_CMDMODE
_SIGNAL_COMMAND.fields_by_name['type'].enum_type = _SIGNAL_CMDTYPE
_SIGNAL_COMMAND.fields_by_name['location'].message_type = _LOCATION
_SIGNAL_COMMAND.fields_by_name['pin'].message_type = _PIN
_SIGNAL_COMMAND.fields_by_name['pwm'].message_type = _PWM
_SIGNAL_COMMAND.fields_by_name['sensors'].message_type = _SENSOR
_SIGNAL_COMMAND.containing_type = _SIGNAL
_SIGNAL.fields_by_name['command'].message_type = _SIGNAL_COMMAND
_SIGNAL_CMDMODE.containing_type = _SIGNAL
_SIGNAL_CMDTYPE.containing_type = _SIGNAL
_SENSOR_TYPE.fields_by_name['type'].enum_type = _SENSOR_TYPE_SENSORTYPE
_SENSOR_TYPE.containing_type = _SENSOR
_SENSOR_TYPE_SENSORTYPE.containing_type = _SENSOR_TYPE
_SENSOR_EVENT.containing_type = _SENSOR
_SENSOR.fields_by_name['type'].message_type = _SENSOR_TYPE
_SENSOR.fields_by_name['event'].message_type = _SENSOR_EVENT
_PIN.fields_by_name['mode'].enum_type = _PIN_MODE
_PIN.fields_by_name['direction'].enum_type = _PIN_DIRECTION
_PIN.fields_by_name['pull'].enum_type = _PIN_PULL
_PIN_MODE.containing_type = _PIN
_PIN_DIRECTION.containing_type = _PIN
_PIN_PULL.containing_type = _PIN
DESCRIPTOR.message_types_by_name['Signal'] = _SIGNAL
DESCRIPTOR.message_types_by_name['Sensor'] = _SENSOR
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['Pin'] = _PIN
DESCRIPTOR.message_types_by_name['PWM'] = _PWM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Signal = _reflection.GeneratedProtocolMessageType('Signal', (_message.Message,), {

  'Command' : _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
    'DESCRIPTOR' : _SIGNAL_COMMAND,
    '__module__' : 'signal.v1.signal_pb2'
    # @@protoc_insertion_point(class_scope:signal.v1.Signal.Command)
    })
  ,
  'DESCRIPTOR' : _SIGNAL,
  '__module__' : 'signal.v1.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.v1.Signal)
  })
_sym_db.RegisterMessage(Signal)
_sym_db.RegisterMessage(Signal.Command)

Sensor = _reflection.GeneratedProtocolMessageType('Sensor', (_message.Message,), {

  'Type' : _reflection.GeneratedProtocolMessageType('Type', (_message.Message,), {
    'DESCRIPTOR' : _SENSOR_TYPE,
    '__module__' : 'signal.v1.signal_pb2'
    # @@protoc_insertion_point(class_scope:signal.v1.Sensor.Type)
    })
  ,

  'Event' : _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
    'DESCRIPTOR' : _SENSOR_EVENT,
    '__module__' : 'signal.v1.signal_pb2'
    # @@protoc_insertion_point(class_scope:signal.v1.Sensor.Event)
    })
  ,
  'DESCRIPTOR' : _SENSOR,
  '__module__' : 'signal.v1.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.v1.Sensor)
  })
_sym_db.RegisterMessage(Sensor)
_sym_db.RegisterMessage(Sensor.Type)
_sym_db.RegisterMessage(Sensor.Event)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'signal.v1.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.v1.Location)
  })
_sym_db.RegisterMessage(Location)

Pin = _reflection.GeneratedProtocolMessageType('Pin', (_message.Message,), {
  'DESCRIPTOR' : _PIN,
  '__module__' : 'signal.v1.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.v1.Pin)
  })
_sym_db.RegisterMessage(Pin)

PWM = _reflection.GeneratedProtocolMessageType('PWM', (_message.Message,), {
  'DESCRIPTOR' : _PWM,
  '__module__' : 'signal.v1.signal_pb2'
  # @@protoc_insertion_point(class_scope:signal.v1.PWM)
  })
_sym_db.RegisterMessage(PWM)


# @@protoc_insertion_point(module_scope)
