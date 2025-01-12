// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from type:srv/StartTime.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "type/srv/detail/start_time__rosidl_typesupport_introspection_c.h"
#include "type/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "type/srv/detail/start_time__functions.h"
#include "type/srv/detail/start_time__struct.h"


// Include directives for member types
// Member `job_list`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void type__srv__StartTime_Request__rosidl_typesupport_introspection_c__StartTime_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  type__srv__StartTime_Request__init(message_memory);
}

void type__srv__StartTime_Request__rosidl_typesupport_introspection_c__StartTime_Request_fini_function(void * message_memory)
{
  type__srv__StartTime_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember type__srv__StartTime_Request__rosidl_typesupport_introspection_c__StartTime_Request_message_member_array[4] = {
  {
    "start_value",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(type__srv__StartTime_Request, start_value),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "job_list",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(type__srv__StartTime_Request, job_list),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "constatus",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(type__srv__StartTime_Request, constatus),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "datastatus",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(type__srv__StartTime_Request, datastatus),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers type__srv__StartTime_Request__rosidl_typesupport_introspection_c__StartTime_Request_message_members = {
  "type__srv",  // message namespace
  "StartTime_Request",  // message name
  4,  // number of fields
  sizeof(type__srv__StartTime_Request),
  type__srv__StartTime_Request__rosidl_typesupport_introspection_c__StartTime_Request_message_member_array,  // message members
  type__srv__StartTime_Request__rosidl_typesupport_introspection_c__StartTime_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  type__srv__StartTime_Request__rosidl_typesupport_introspection_c__StartTime_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t type__srv__StartTime_Request__rosidl_typesupport_introspection_c__StartTime_Request_message_type_support_handle = {
  0,
  &type__srv__StartTime_Request__rosidl_typesupport_introspection_c__StartTime_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_type
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, type, srv, StartTime_Request)() {
  if (!type__srv__StartTime_Request__rosidl_typesupport_introspection_c__StartTime_Request_message_type_support_handle.typesupport_identifier) {
    type__srv__StartTime_Request__rosidl_typesupport_introspection_c__StartTime_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &type__srv__StartTime_Request__rosidl_typesupport_introspection_c__StartTime_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "type/srv/detail/start_time__rosidl_typesupport_introspection_c.h"
// already included above
// #include "type/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "type/srv/detail/start_time__functions.h"
// already included above
// #include "type/srv/detail/start_time__struct.h"


// Include directives for member types
// Member `status`
// Member `conv`
// Member `data`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void type__srv__StartTime_Response__rosidl_typesupport_introspection_c__StartTime_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  type__srv__StartTime_Response__init(message_memory);
}

void type__srv__StartTime_Response__rosidl_typesupport_introspection_c__StartTime_Response_fini_function(void * message_memory)
{
  type__srv__StartTime_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember type__srv__StartTime_Response__rosidl_typesupport_introspection_c__StartTime_Response_message_member_array[4] = {
  {
    "result_value",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(type__srv__StartTime_Response, result_value),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "status",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(type__srv__StartTime_Response, status),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "conv",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(type__srv__StartTime_Response, conv),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "data",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(type__srv__StartTime_Response, data),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers type__srv__StartTime_Response__rosidl_typesupport_introspection_c__StartTime_Response_message_members = {
  "type__srv",  // message namespace
  "StartTime_Response",  // message name
  4,  // number of fields
  sizeof(type__srv__StartTime_Response),
  type__srv__StartTime_Response__rosidl_typesupport_introspection_c__StartTime_Response_message_member_array,  // message members
  type__srv__StartTime_Response__rosidl_typesupport_introspection_c__StartTime_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  type__srv__StartTime_Response__rosidl_typesupport_introspection_c__StartTime_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t type__srv__StartTime_Response__rosidl_typesupport_introspection_c__StartTime_Response_message_type_support_handle = {
  0,
  &type__srv__StartTime_Response__rosidl_typesupport_introspection_c__StartTime_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_type
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, type, srv, StartTime_Response)() {
  if (!type__srv__StartTime_Response__rosidl_typesupport_introspection_c__StartTime_Response_message_type_support_handle.typesupport_identifier) {
    type__srv__StartTime_Response__rosidl_typesupport_introspection_c__StartTime_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &type__srv__StartTime_Response__rosidl_typesupport_introspection_c__StartTime_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "type/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "type/srv/detail/start_time__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers type__srv__detail__start_time__rosidl_typesupport_introspection_c__StartTime_service_members = {
  "type__srv",  // service namespace
  "StartTime",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // type__srv__detail__start_time__rosidl_typesupport_introspection_c__StartTime_Request_message_type_support_handle,
  NULL  // response message
  // type__srv__detail__start_time__rosidl_typesupport_introspection_c__StartTime_Response_message_type_support_handle
};

static rosidl_service_type_support_t type__srv__detail__start_time__rosidl_typesupport_introspection_c__StartTime_service_type_support_handle = {
  0,
  &type__srv__detail__start_time__rosidl_typesupport_introspection_c__StartTime_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, type, srv, StartTime_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, type, srv, StartTime_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_type
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, type, srv, StartTime)() {
  if (!type__srv__detail__start_time__rosidl_typesupport_introspection_c__StartTime_service_type_support_handle.typesupport_identifier) {
    type__srv__detail__start_time__rosidl_typesupport_introspection_c__StartTime_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)type__srv__detail__start_time__rosidl_typesupport_introspection_c__StartTime_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, type, srv, StartTime_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, type, srv, StartTime_Response)()->data;
  }

  return &type__srv__detail__start_time__rosidl_typesupport_introspection_c__StartTime_service_type_support_handle;
}
