// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from type:srv/StartTime.idl
// generated code does not contain a copyright notice

#ifndef TYPE__SRV__DETAIL__START_TIME__STRUCT_H_
#define TYPE__SRV__DETAIL__START_TIME__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'job_list'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/StartTime in the package type.
typedef struct type__srv__StartTime_Request
{
  /// 요청 부분 (요청 메시지)
  /// 작업을 시작할 때 전달하는 값
  int32_t start_value;
  /// 작업 이름
  rosidl_runtime_c__String job_list;
  int32_t constatus;
  int32_t datastatus;
} type__srv__StartTime_Request;

// Struct for a sequence of type__srv__StartTime_Request.
typedef struct type__srv__StartTime_Request__Sequence
{
  type__srv__StartTime_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} type__srv__StartTime_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'status'
// Member 'conv'
// Member 'data'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/StartTime in the package type.
typedef struct type__srv__StartTime_Response
{
  /// 응답 부분 (응답 메시지)
  /// 처리된 결과 값
  int32_t result_value;
  /// 작업 처리 상태 (예: SUCCESS, FAILURE 등)
  rosidl_runtime_c__String status;
  rosidl_runtime_c__String conv;
  rosidl_runtime_c__String data;
} type__srv__StartTime_Response;

// Struct for a sequence of type__srv__StartTime_Response.
typedef struct type__srv__StartTime_Response__Sequence
{
  type__srv__StartTime_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} type__srv__StartTime_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TYPE__SRV__DETAIL__START_TIME__STRUCT_H_
