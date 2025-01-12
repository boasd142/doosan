// NOLINT: This file starts with a BOM since it contain non-ASCII characters
// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from order_msgs:srv/Order.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__SRV__DETAIL__ORDER__STRUCT_H_
#define ORDER_MSGS__SRV__DETAIL__ORDER__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'table_num'
// Member 'item'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/Order in the package order_msgs.
typedef struct order_msgs__srv__Order_Request
{
  /// 테이블 번호
  rosidl_runtime_c__String table_num;
  /// 메뉴 항목
  rosidl_runtime_c__String item;
  /// 수량
  int32_t quantity;
  /// 가격
  int32_t price;
} order_msgs__srv__Order_Request;

// Struct for a sequence of order_msgs__srv__Order_Request.
typedef struct order_msgs__srv__Order_Request__Sequence
{
  order_msgs__srv__Order_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} order_msgs__srv__Order_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/Order in the package order_msgs.
typedef struct order_msgs__srv__Order_Response
{
  /// 처리 성공 여부
  bool success;
  /// 추가 메시지 (예: "주문이 완료되었습니다.")
  rosidl_runtime_c__String message;
} order_msgs__srv__Order_Response;

// Struct for a sequence of order_msgs__srv__Order_Response.
typedef struct order_msgs__srv__Order_Response__Sequence
{
  order_msgs__srv__Order_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} order_msgs__srv__Order_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ORDER_MSGS__SRV__DETAIL__ORDER__STRUCT_H_
