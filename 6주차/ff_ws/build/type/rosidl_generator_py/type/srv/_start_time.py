# generated from rosidl_generator_py/resource/_idl.py.em
# with input from type:srv/StartTime.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_StartTime_Request(type):
    """Metaclass of message 'StartTime_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('type')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'type.srv.StartTime_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__start_time__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__start_time__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__start_time__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__start_time__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__start_time__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class StartTime_Request(metaclass=Metaclass_StartTime_Request):
    """Message class 'StartTime_Request'."""

    __slots__ = [
        '_start_value',
        '_job_list',
        '_constatus',
        '_datastatus',
    ]

    _fields_and_field_types = {
        'start_value': 'int32',
        'job_list': 'string',
        'constatus': 'int32',
        'datastatus': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.start_value = kwargs.get('start_value', int())
        self.job_list = kwargs.get('job_list', str())
        self.constatus = kwargs.get('constatus', int())
        self.datastatus = kwargs.get('datastatus', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.start_value != other.start_value:
            return False
        if self.job_list != other.job_list:
            return False
        if self.constatus != other.constatus:
            return False
        if self.datastatus != other.datastatus:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def start_value(self):
        """Message field 'start_value'."""
        return self._start_value

    @start_value.setter
    def start_value(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'start_value' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'start_value' field must be an integer in [-2147483648, 2147483647]"
        self._start_value = value

    @builtins.property
    def job_list(self):
        """Message field 'job_list'."""
        return self._job_list

    @job_list.setter
    def job_list(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'job_list' field must be of type 'str'"
        self._job_list = value

    @builtins.property
    def constatus(self):
        """Message field 'constatus'."""
        return self._constatus

    @constatus.setter
    def constatus(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'constatus' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'constatus' field must be an integer in [-2147483648, 2147483647]"
        self._constatus = value

    @builtins.property
    def datastatus(self):
        """Message field 'datastatus'."""
        return self._datastatus

    @datastatus.setter
    def datastatus(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'datastatus' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'datastatus' field must be an integer in [-2147483648, 2147483647]"
        self._datastatus = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_StartTime_Response(type):
    """Metaclass of message 'StartTime_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('type')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'type.srv.StartTime_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__start_time__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__start_time__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__start_time__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__start_time__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__start_time__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class StartTime_Response(metaclass=Metaclass_StartTime_Response):
    """Message class 'StartTime_Response'."""

    __slots__ = [
        '_result_value',
        '_status',
        '_conv',
        '_data',
    ]

    _fields_and_field_types = {
        'result_value': 'int32',
        'status': 'string',
        'conv': 'string',
        'data': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.result_value = kwargs.get('result_value', int())
        self.status = kwargs.get('status', str())
        self.conv = kwargs.get('conv', str())
        self.data = kwargs.get('data', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.result_value != other.result_value:
            return False
        if self.status != other.status:
            return False
        if self.conv != other.conv:
            return False
        if self.data != other.data:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def result_value(self):
        """Message field 'result_value'."""
        return self._result_value

    @result_value.setter
    def result_value(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'result_value' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'result_value' field must be an integer in [-2147483648, 2147483647]"
        self._result_value = value

    @builtins.property
    def status(self):
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'status' field must be of type 'str'"
        self._status = value

    @builtins.property
    def conv(self):
        """Message field 'conv'."""
        return self._conv

    @conv.setter
    def conv(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'conv' field must be of type 'str'"
        self._conv = value

    @builtins.property
    def data(self):
        """Message field 'data'."""
        return self._data

    @data.setter
    def data(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'data' field must be of type 'str'"
        self._data = value


class Metaclass_StartTime(type):
    """Metaclass of service 'StartTime'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('type')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'type.srv.StartTime')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__start_time

            from type.srv import _start_time
            if _start_time.Metaclass_StartTime_Request._TYPE_SUPPORT is None:
                _start_time.Metaclass_StartTime_Request.__import_type_support__()
            if _start_time.Metaclass_StartTime_Response._TYPE_SUPPORT is None:
                _start_time.Metaclass_StartTime_Response.__import_type_support__()


class StartTime(metaclass=Metaclass_StartTime):
    from type.srv._start_time import StartTime_Request as Request
    from type.srv._start_time import StartTime_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
