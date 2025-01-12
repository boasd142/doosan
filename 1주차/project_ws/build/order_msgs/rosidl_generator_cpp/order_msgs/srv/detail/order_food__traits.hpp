// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from order_msgs:srv/OrderFood.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__SRV__DETAIL__ORDER_FOOD__TRAITS_HPP_
#define ORDER_MSGS__SRV__DETAIL__ORDER_FOOD__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "order_msgs/srv/detail/order_food__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace order_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const OrderFood_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: item_name
  {
    out << "item_name: ";
    rosidl_generator_traits::value_to_yaml(msg.item_name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const OrderFood_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: item_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "item_name: ";
    rosidl_generator_traits::value_to_yaml(msg.item_name, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const OrderFood_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace order_msgs

namespace rosidl_generator_traits
{

[[deprecated("use order_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const order_msgs::srv::OrderFood_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  order_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use order_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const order_msgs::srv::OrderFood_Request & msg)
{
  return order_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<order_msgs::srv::OrderFood_Request>()
{
  return "order_msgs::srv::OrderFood_Request";
}

template<>
inline const char * name<order_msgs::srv::OrderFood_Request>()
{
  return "order_msgs/srv/OrderFood_Request";
}

template<>
struct has_fixed_size<order_msgs::srv::OrderFood_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<order_msgs::srv::OrderFood_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<order_msgs::srv::OrderFood_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace order_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const OrderFood_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: message
  {
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const OrderFood_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }

  // member: message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const OrderFood_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace order_msgs

namespace rosidl_generator_traits
{

[[deprecated("use order_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const order_msgs::srv::OrderFood_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  order_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use order_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const order_msgs::srv::OrderFood_Response & msg)
{
  return order_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<order_msgs::srv::OrderFood_Response>()
{
  return "order_msgs::srv::OrderFood_Response";
}

template<>
inline const char * name<order_msgs::srv::OrderFood_Response>()
{
  return "order_msgs/srv/OrderFood_Response";
}

template<>
struct has_fixed_size<order_msgs::srv::OrderFood_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<order_msgs::srv::OrderFood_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<order_msgs::srv::OrderFood_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<order_msgs::srv::OrderFood>()
{
  return "order_msgs::srv::OrderFood";
}

template<>
inline const char * name<order_msgs::srv::OrderFood>()
{
  return "order_msgs/srv/OrderFood";
}

template<>
struct has_fixed_size<order_msgs::srv::OrderFood>
  : std::integral_constant<
    bool,
    has_fixed_size<order_msgs::srv::OrderFood_Request>::value &&
    has_fixed_size<order_msgs::srv::OrderFood_Response>::value
  >
{
};

template<>
struct has_bounded_size<order_msgs::srv::OrderFood>
  : std::integral_constant<
    bool,
    has_bounded_size<order_msgs::srv::OrderFood_Request>::value &&
    has_bounded_size<order_msgs::srv::OrderFood_Response>::value
  >
{
};

template<>
struct is_service<order_msgs::srv::OrderFood>
  : std::true_type
{
};

template<>
struct is_service_request<order_msgs::srv::OrderFood_Request>
  : std::true_type
{
};

template<>
struct is_service_response<order_msgs::srv::OrderFood_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ORDER_MSGS__SRV__DETAIL__ORDER_FOOD__TRAITS_HPP_
