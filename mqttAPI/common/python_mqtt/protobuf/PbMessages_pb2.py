# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PbMessages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import PbConsts_pb2 as PbConsts__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='PbMessages.proto',
  package='pb',
  syntax='proto3',
  serialized_pb=_b('\n\x10PbMessages.proto\x12\x02pb\x1a\x0ePbConsts.proto\"K\n\x07PbTwist\x12\x13\n\x0blinearSpeed\x18\x01 \x01(\x02\x12\x14\n\x0c\x61ngularSpeed\x18\x02 \x01(\x02\x12\x0c\n\x02id\x18\x03 \x01(\x05H\x00\x42\x07\n\x05hasID\"9\n\nPbPoint2Df\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\x0c\n\x02id\x18\x03 \x01(\x05H\x00\x42\x07\n\x05hasID\"G\n\tPbPose2Df\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\r\n\x05theta\x18\x03 \x01(\x02\x12\x0c\n\x02id\x18\x04 \x01(\x05H\x00\x42\x07\n\x05hasID\"K\n\nPbSchedule\x12\x1f\n\x06opType\x18\x01 \x01(\x0e\x32\x0f.pb.ScheduleOpT\x12\x0c\n\x04time\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\"\xef\x03\n\x0cPbDeviceInfo\x12$\n\twifiState\x18\x01 \x01(\x0e\x32\x0f.pb.WifiStatusTH\x00\x12\x19\n\x0fwifiLinkQuality\x18\x02 \x01(\x05H\x01\x12\x19\n\x0fwifiSignalLevel\x18\x03 \x01(\x05H\x02\x12\x11\n\x07netPing\x18\x04 \x01(\x05H\x03\x12\x12\n\x08netState\x18\x05 \x01(\x05H\x04\x12\x11\n\x07\x62\x61ttery\x18\x08 \x01(\x05H\x05\x12\x14\n\nwaterLevel\x18\t \x01(\x05H\x06\x12\x13\n\tdustLevel\x18\n \x01(\x05H\x07\x12\x15\n\x0btemperature\x18\x0b \x01(\x05H\x08\x12\x11\n\x07utcTime\x18\x10 \x01(\x05H\t\x12\x11\n\tIPAddress\x18\x11 \x01(\t\x12\x13\n\x0blanguagePkg\x18\x12 \x01(\t\x12\x13\n\tmemFreeKB\x18\x13 \x01(\x05H\nB\x0f\n\rhasWifiStatusB\x10\n\x0ehasWifiQualityB\x14\n\x12hasWifiSignalLevelB\x12\n\x10hasNetPingStatusB\r\n\x0bhasNetStateB\x0c\n\nhasBatteryB\x0f\n\rhasWaterLevelB\x0e\n\x0chasDustLevelB\x10\n\x0ehasTemperatureB\x0c\n\nhasUTCTimeB\x0c\n\nhasMemFree\"G\n\x0cPbWakeUpInfo\x12#\n\nwakeUpType\x18\x01 \x01(\x0e\x32\x0f.pb.WakeUpTypeT\x12\x12\n\nwakeUpTime\x18\x02 \x01(\x05\"\xa0\x01\n\x0bPbCleanMode\x12\x1c\n\x04mode\x18\x01 \x01(\x0e\x32\x0e.pb.CleanModeT\x12\x12\n\x08\x66\x61nSpeed\x18\x02 \x01(\x05H\x00\x12\x13\n\tpumpSpeed\x18\x03 \x01(\x05H\x01\x12\x17\n\rvibratorSpeed\x18\x04 \x01(\x05H\x02\x42\r\n\x0bhasFanSpeedB\x0e\n\x0chasPumpSpeedB\x12\n\x10hasVibratorSpeed\"~\n\x12\x46loorControlParams\x12\x11\n\tfloorHash\x18\x03 \x01(\t\x12\x13\n\x0bgoZoneHashs\x18\x01 \x03(\t\x12\x15\n\rnogoZoneHashs\x18\x02 \x03(\t\x12\x13\n\x0b\x66loorsLists\x18\x04 \x03(\t\x12\x14\n\x0c\x63\x61ndidateIDs\x18\x05 \x03(\x05\"w\n\tPbAedInfo\x12\x1b\n\x11hatchDoorOpenTime\x18\x01 \x01(\x05H\x00\x12\x1c\n\x12hatchDoorCloseTime\x18\x02 \x01(\x05H\x01\x42\x16\n\x14hasHatchDoorOpenTimeB\x17\n\x15hasHatchDoorCloseTimeB\x02H\x03\x62\x06proto3')
  ,
  dependencies=[PbConsts__pb2.DESCRIPTOR,])




_PBTWIST = _descriptor.Descriptor(
  name='PbTwist',
  full_name='pb.PbTwist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='linearSpeed', full_name='pb.PbTwist.linearSpeed', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angularSpeed', full_name='pb.PbTwist.angularSpeed', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='pb.PbTwist.id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='hasID', full_name='pb.PbTwist.hasID',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=40,
  serialized_end=115,
)


_PBPOINT2DF = _descriptor.Descriptor(
  name='PbPoint2Df',
  full_name='pb.PbPoint2Df',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='pb.PbPoint2Df.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='pb.PbPoint2Df.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='pb.PbPoint2Df.id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='hasID', full_name='pb.PbPoint2Df.hasID',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=117,
  serialized_end=174,
)


_PBPOSE2DF = _descriptor.Descriptor(
  name='PbPose2Df',
  full_name='pb.PbPose2Df',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='pb.PbPose2Df.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='pb.PbPose2Df.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='theta', full_name='pb.PbPose2Df.theta', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='pb.PbPose2Df.id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='hasID', full_name='pb.PbPose2Df.hasID',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=176,
  serialized_end=247,
)


_PBSCHEDULE = _descriptor.Descriptor(
  name='PbSchedule',
  full_name='pb.PbSchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opType', full_name='pb.PbSchedule.opType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='pb.PbSchedule.time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='pb.PbSchedule.action', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=249,
  serialized_end=324,
)


_PBDEVICEINFO = _descriptor.Descriptor(
  name='PbDeviceInfo',
  full_name='pb.PbDeviceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wifiState', full_name='pb.PbDeviceInfo.wifiState', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wifiLinkQuality', full_name='pb.PbDeviceInfo.wifiLinkQuality', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wifiSignalLevel', full_name='pb.PbDeviceInfo.wifiSignalLevel', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='netPing', full_name='pb.PbDeviceInfo.netPing', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='netState', full_name='pb.PbDeviceInfo.netState', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='battery', full_name='pb.PbDeviceInfo.battery', index=5,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waterLevel', full_name='pb.PbDeviceInfo.waterLevel', index=6,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dustLevel', full_name='pb.PbDeviceInfo.dustLevel', index=7,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='pb.PbDeviceInfo.temperature', index=8,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='utcTime', full_name='pb.PbDeviceInfo.utcTime', index=9,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='IPAddress', full_name='pb.PbDeviceInfo.IPAddress', index=10,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='languagePkg', full_name='pb.PbDeviceInfo.languagePkg', index=11,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memFreeKB', full_name='pb.PbDeviceInfo.memFreeKB', index=12,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='hasWifiStatus', full_name='pb.PbDeviceInfo.hasWifiStatus',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasWifiQuality', full_name='pb.PbDeviceInfo.hasWifiQuality',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasWifiSignalLevel', full_name='pb.PbDeviceInfo.hasWifiSignalLevel',
      index=2, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasNetPingStatus', full_name='pb.PbDeviceInfo.hasNetPingStatus',
      index=3, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasNetState', full_name='pb.PbDeviceInfo.hasNetState',
      index=4, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasBattery', full_name='pb.PbDeviceInfo.hasBattery',
      index=5, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasWaterLevel', full_name='pb.PbDeviceInfo.hasWaterLevel',
      index=6, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasDustLevel', full_name='pb.PbDeviceInfo.hasDustLevel',
      index=7, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasTemperature', full_name='pb.PbDeviceInfo.hasTemperature',
      index=8, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasUTCTime', full_name='pb.PbDeviceInfo.hasUTCTime',
      index=9, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasMemFree', full_name='pb.PbDeviceInfo.hasMemFree',
      index=10, containing_type=None, fields=[]),
  ],
  serialized_start=327,
  serialized_end=822,
)


_PBWAKEUPINFO = _descriptor.Descriptor(
  name='PbWakeUpInfo',
  full_name='pb.PbWakeUpInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wakeUpType', full_name='pb.PbWakeUpInfo.wakeUpType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wakeUpTime', full_name='pb.PbWakeUpInfo.wakeUpTime', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=824,
  serialized_end=895,
)


_PBCLEANMODE = _descriptor.Descriptor(
  name='PbCleanMode',
  full_name='pb.PbCleanMode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='pb.PbCleanMode.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fanSpeed', full_name='pb.PbCleanMode.fanSpeed', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pumpSpeed', full_name='pb.PbCleanMode.pumpSpeed', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vibratorSpeed', full_name='pb.PbCleanMode.vibratorSpeed', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='hasFanSpeed', full_name='pb.PbCleanMode.hasFanSpeed',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasPumpSpeed', full_name='pb.PbCleanMode.hasPumpSpeed',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasVibratorSpeed', full_name='pb.PbCleanMode.hasVibratorSpeed',
      index=2, containing_type=None, fields=[]),
  ],
  serialized_start=898,
  serialized_end=1058,
)


_FLOORCONTROLPARAMS = _descriptor.Descriptor(
  name='FloorControlParams',
  full_name='pb.FloorControlParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='floorHash', full_name='pb.FloorControlParams.floorHash', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='goZoneHashs', full_name='pb.FloorControlParams.goZoneHashs', index=1,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nogoZoneHashs', full_name='pb.FloorControlParams.nogoZoneHashs', index=2,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floorsLists', full_name='pb.FloorControlParams.floorsLists', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='candidateIDs', full_name='pb.FloorControlParams.candidateIDs', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1060,
  serialized_end=1186,
)


_PBAEDINFO = _descriptor.Descriptor(
  name='PbAedInfo',
  full_name='pb.PbAedInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hatchDoorOpenTime', full_name='pb.PbAedInfo.hatchDoorOpenTime', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hatchDoorCloseTime', full_name='pb.PbAedInfo.hatchDoorCloseTime', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='hasHatchDoorOpenTime', full_name='pb.PbAedInfo.hasHatchDoorOpenTime',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='hasHatchDoorCloseTime', full_name='pb.PbAedInfo.hasHatchDoorCloseTime',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=1188,
  serialized_end=1307,
)

_PBTWIST.oneofs_by_name['hasID'].fields.append(
  _PBTWIST.fields_by_name['id'])
_PBTWIST.fields_by_name['id'].containing_oneof = _PBTWIST.oneofs_by_name['hasID']
_PBPOINT2DF.oneofs_by_name['hasID'].fields.append(
  _PBPOINT2DF.fields_by_name['id'])
_PBPOINT2DF.fields_by_name['id'].containing_oneof = _PBPOINT2DF.oneofs_by_name['hasID']
_PBPOSE2DF.oneofs_by_name['hasID'].fields.append(
  _PBPOSE2DF.fields_by_name['id'])
_PBPOSE2DF.fields_by_name['id'].containing_oneof = _PBPOSE2DF.oneofs_by_name['hasID']
_PBSCHEDULE.fields_by_name['opType'].enum_type = PbConsts__pb2._SCHEDULEOPT
_PBDEVICEINFO.fields_by_name['wifiState'].enum_type = PbConsts__pb2._WIFISTATUST
_PBDEVICEINFO.oneofs_by_name['hasWifiStatus'].fields.append(
  _PBDEVICEINFO.fields_by_name['wifiState'])
_PBDEVICEINFO.fields_by_name['wifiState'].containing_oneof = _PBDEVICEINFO.oneofs_by_name['hasWifiStatus']
_PBDEVICEINFO.oneofs_by_name['hasWifiQuality'].fields.append(
  _PBDEVICEINFO.fields_by_name['wifiLinkQuality'])
_PBDEVICEINFO.fields_by_name['wifiLinkQuality'].containing_oneof = _PBDEVICEINFO.oneofs_by_name['hasWifiQuality']
_PBDEVICEINFO.oneofs_by_name['hasWifiSignalLevel'].fields.append(
  _PBDEVICEINFO.fields_by_name['wifiSignalLevel'])
_PBDEVICEINFO.fields_by_name['wifiSignalLevel'].containing_oneof = _PBDEVICEINFO.oneofs_by_name['hasWifiSignalLevel']
_PBDEVICEINFO.oneofs_by_name['hasNetPingStatus'].fields.append(
  _PBDEVICEINFO.fields_by_name['netPing'])
_PBDEVICEINFO.fields_by_name['netPing'].containing_oneof = _PBDEVICEINFO.oneofs_by_name['hasNetPingStatus']
_PBDEVICEINFO.oneofs_by_name['hasNetState'].fields.append(
  _PBDEVICEINFO.fields_by_name['netState'])
_PBDEVICEINFO.fields_by_name['netState'].containing_oneof = _PBDEVICEINFO.oneofs_by_name['hasNetState']
_PBDEVICEINFO.oneofs_by_name['hasBattery'].fields.append(
  _PBDEVICEINFO.fields_by_name['battery'])
_PBDEVICEINFO.fields_by_name['battery'].containing_oneof = _PBDEVICEINFO.oneofs_by_name['hasBattery']
_PBDEVICEINFO.oneofs_by_name['hasWaterLevel'].fields.append(
  _PBDEVICEINFO.fields_by_name['waterLevel'])
_PBDEVICEINFO.fields_by_name['waterLevel'].containing_oneof = _PBDEVICEINFO.oneofs_by_name['hasWaterLevel']
_PBDEVICEINFO.oneofs_by_name['hasDustLevel'].fields.append(
  _PBDEVICEINFO.fields_by_name['dustLevel'])
_PBDEVICEINFO.fields_by_name['dustLevel'].containing_oneof = _PBDEVICEINFO.oneofs_by_name['hasDustLevel']
_PBDEVICEINFO.oneofs_by_name['hasTemperature'].fields.append(
  _PBDEVICEINFO.fields_by_name['temperature'])
_PBDEVICEINFO.fields_by_name['temperature'].containing_oneof = _PBDEVICEINFO.oneofs_by_name['hasTemperature']
_PBDEVICEINFO.oneofs_by_name['hasUTCTime'].fields.append(
  _PBDEVICEINFO.fields_by_name['utcTime'])
_PBDEVICEINFO.fields_by_name['utcTime'].containing_oneof = _PBDEVICEINFO.oneofs_by_name['hasUTCTime']
_PBDEVICEINFO.oneofs_by_name['hasMemFree'].fields.append(
  _PBDEVICEINFO.fields_by_name['memFreeKB'])
_PBDEVICEINFO.fields_by_name['memFreeKB'].containing_oneof = _PBDEVICEINFO.oneofs_by_name['hasMemFree']
_PBWAKEUPINFO.fields_by_name['wakeUpType'].enum_type = PbConsts__pb2._WAKEUPTYPET
_PBCLEANMODE.fields_by_name['mode'].enum_type = PbConsts__pb2._CLEANMODET
_PBCLEANMODE.oneofs_by_name['hasFanSpeed'].fields.append(
  _PBCLEANMODE.fields_by_name['fanSpeed'])
_PBCLEANMODE.fields_by_name['fanSpeed'].containing_oneof = _PBCLEANMODE.oneofs_by_name['hasFanSpeed']
_PBCLEANMODE.oneofs_by_name['hasPumpSpeed'].fields.append(
  _PBCLEANMODE.fields_by_name['pumpSpeed'])
_PBCLEANMODE.fields_by_name['pumpSpeed'].containing_oneof = _PBCLEANMODE.oneofs_by_name['hasPumpSpeed']
_PBCLEANMODE.oneofs_by_name['hasVibratorSpeed'].fields.append(
  _PBCLEANMODE.fields_by_name['vibratorSpeed'])
_PBCLEANMODE.fields_by_name['vibratorSpeed'].containing_oneof = _PBCLEANMODE.oneofs_by_name['hasVibratorSpeed']
_PBAEDINFO.oneofs_by_name['hasHatchDoorOpenTime'].fields.append(
  _PBAEDINFO.fields_by_name['hatchDoorOpenTime'])
_PBAEDINFO.fields_by_name['hatchDoorOpenTime'].containing_oneof = _PBAEDINFO.oneofs_by_name['hasHatchDoorOpenTime']
_PBAEDINFO.oneofs_by_name['hasHatchDoorCloseTime'].fields.append(
  _PBAEDINFO.fields_by_name['hatchDoorCloseTime'])
_PBAEDINFO.fields_by_name['hatchDoorCloseTime'].containing_oneof = _PBAEDINFO.oneofs_by_name['hasHatchDoorCloseTime']
DESCRIPTOR.message_types_by_name['PbTwist'] = _PBTWIST
DESCRIPTOR.message_types_by_name['PbPoint2Df'] = _PBPOINT2DF
DESCRIPTOR.message_types_by_name['PbPose2Df'] = _PBPOSE2DF
DESCRIPTOR.message_types_by_name['PbSchedule'] = _PBSCHEDULE
DESCRIPTOR.message_types_by_name['PbDeviceInfo'] = _PBDEVICEINFO
DESCRIPTOR.message_types_by_name['PbWakeUpInfo'] = _PBWAKEUPINFO
DESCRIPTOR.message_types_by_name['PbCleanMode'] = _PBCLEANMODE
DESCRIPTOR.message_types_by_name['FloorControlParams'] = _FLOORCONTROLPARAMS
DESCRIPTOR.message_types_by_name['PbAedInfo'] = _PBAEDINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PbTwist = _reflection.GeneratedProtocolMessageType('PbTwist', (_message.Message,), dict(
  DESCRIPTOR = _PBTWIST,
  __module__ = 'PbMessages_pb2'
  # @@protoc_insertion_point(class_scope:pb.PbTwist)
  ))
_sym_db.RegisterMessage(PbTwist)

PbPoint2Df = _reflection.GeneratedProtocolMessageType('PbPoint2Df', (_message.Message,), dict(
  DESCRIPTOR = _PBPOINT2DF,
  __module__ = 'PbMessages_pb2'
  # @@protoc_insertion_point(class_scope:pb.PbPoint2Df)
  ))
_sym_db.RegisterMessage(PbPoint2Df)

PbPose2Df = _reflection.GeneratedProtocolMessageType('PbPose2Df', (_message.Message,), dict(
  DESCRIPTOR = _PBPOSE2DF,
  __module__ = 'PbMessages_pb2'
  # @@protoc_insertion_point(class_scope:pb.PbPose2Df)
  ))
_sym_db.RegisterMessage(PbPose2Df)

PbSchedule = _reflection.GeneratedProtocolMessageType('PbSchedule', (_message.Message,), dict(
  DESCRIPTOR = _PBSCHEDULE,
  __module__ = 'PbMessages_pb2'
  # @@protoc_insertion_point(class_scope:pb.PbSchedule)
  ))
_sym_db.RegisterMessage(PbSchedule)

PbDeviceInfo = _reflection.GeneratedProtocolMessageType('PbDeviceInfo', (_message.Message,), dict(
  DESCRIPTOR = _PBDEVICEINFO,
  __module__ = 'PbMessages_pb2'
  # @@protoc_insertion_point(class_scope:pb.PbDeviceInfo)
  ))
_sym_db.RegisterMessage(PbDeviceInfo)

PbWakeUpInfo = _reflection.GeneratedProtocolMessageType('PbWakeUpInfo', (_message.Message,), dict(
  DESCRIPTOR = _PBWAKEUPINFO,
  __module__ = 'PbMessages_pb2'
  # @@protoc_insertion_point(class_scope:pb.PbWakeUpInfo)
  ))
_sym_db.RegisterMessage(PbWakeUpInfo)

PbCleanMode = _reflection.GeneratedProtocolMessageType('PbCleanMode', (_message.Message,), dict(
  DESCRIPTOR = _PBCLEANMODE,
  __module__ = 'PbMessages_pb2'
  # @@protoc_insertion_point(class_scope:pb.PbCleanMode)
  ))
_sym_db.RegisterMessage(PbCleanMode)

FloorControlParams = _reflection.GeneratedProtocolMessageType('FloorControlParams', (_message.Message,), dict(
  DESCRIPTOR = _FLOORCONTROLPARAMS,
  __module__ = 'PbMessages_pb2'
  # @@protoc_insertion_point(class_scope:pb.FloorControlParams)
  ))
_sym_db.RegisterMessage(FloorControlParams)

PbAedInfo = _reflection.GeneratedProtocolMessageType('PbAedInfo', (_message.Message,), dict(
  DESCRIPTOR = _PBAEDINFO,
  __module__ = 'PbMessages_pb2'
  # @@protoc_insertion_point(class_scope:pb.PbAedInfo)
  ))
_sym_db.RegisterMessage(PbAedInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)
