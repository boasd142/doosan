// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from order_msgs:msg/OrderMsg.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__MSG__DETAIL__ORDER_MSG__STRUCT_H_
#define ORDER_MSGS__MSG__DETAIL__ORDER_MSG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/OrderMsg in the package order_msgs.
typedef struct order_msgs__msg__OrderMsg
{
  uint8_t structure_needs_at_least_one_member;
} order_msgs__msg__OrderMsg;

// Struct for a sequence of order_msgs__msg__OrderMsg.
typedef struct order_msgs__msg__OrderMsg__Sequence
{
  order_msgs__msg__OrderMsg * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} order_msgs__msg__OrderMsg__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ORDER_MSGS__MSG__DETAIL__ORDER_MSG__STRUCT_H_
