// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from order_msgs:msg/OrderMsg.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__MSG__DETAIL__ORDER_MSG__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define ORDER_MSGS__MSG__DETAIL__ORDER_MSG__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "order_msgs/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "order_msgs/msg/detail/order_msg__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace order_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_order_msgs
cdr_serialize(
  const order_msgs::msg::OrderMsg & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_order_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  order_msgs::msg::OrderMsg & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_order_msgs
get_serialized_size(
  const order_msgs::msg::OrderMsg & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_order_msgs
max_serialized_size_OrderMsg(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace order_msgs

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_order_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, order_msgs, msg, OrderMsg)();

#ifdef __cplusplus
}
#endif

#endif  // ORDER_MSGS__MSG__DETAIL__ORDER_MSG__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
