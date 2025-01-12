// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from order_msgs:srv/OrderFood.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__SRV__DETAIL__ORDER_FOOD__STRUCT_H_
#define ORDER_MSGS__SRV__DETAIL__ORDER_FOOD__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'item_name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/OrderFood in the package order_msgs.
typedef struct order_msgs__srv__OrderFood_Request
{
  /// 주문할 항목 이름
  rosidl_runtime_c__String item_name;
} order_msgs__srv__OrderFood_Request;

// Struct for a sequence of order_msgs__srv__OrderFood_Request.
typedef struct order_msgs__srv__OrderFood_Request__Sequence
{
  order_msgs__srv__OrderFood_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} order_msgs__srv__OrderFood_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/OrderFood in the package order_msgs.
typedef struct order_msgs__srv__OrderFood_Response
{
  /// 주문 성공 여부
  bool success;
  /// 주문 결과 메시지
  rosidl_runtime_c__String message;
} order_msgs__srv__OrderFood_Response;

// Struct for a sequence of order_msgs__srv__OrderFood_Response.
typedef struct order_msgs__srv__OrderFood_Response__Sequence
{
  order_msgs__srv__OrderFood_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} order_msgs__srv__OrderFood_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ORDER_MSGS__SRV__DETAIL__ORDER_FOOD__STRUCT_H_
