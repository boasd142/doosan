// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from order_msgs:msg/OrderMsg.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__MSG__DETAIL__ORDER_MSG__TRAITS_HPP_
#define ORDER_MSGS__MSG__DETAIL__ORDER_MSG__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "order_msgs/msg/detail/order_msg__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace order_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const OrderMsg & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const OrderMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const OrderMsg & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace order_msgs

namespace rosidl_generator_traits
{

[[deprecated("use order_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const order_msgs::msg::OrderMsg & msg,
  std::ostream & out, size_t indentation = 0)
{
  order_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use order_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const order_msgs::msg::OrderMsg & msg)
{
  return order_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<order_msgs::msg::OrderMsg>()
{
  return "order_msgs::msg::OrderMsg";
}

template<>
inline const char * name<order_msgs::msg::OrderMsg>()
{
  return "order_msgs/msg/OrderMsg";
}

template<>
struct has_fixed_size<order_msgs::msg::OrderMsg>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<order_msgs::msg::OrderMsg>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<order_msgs::msg::OrderMsg>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ORDER_MSGS__MSG__DETAIL__ORDER_MSG__TRAITS_HPP_
