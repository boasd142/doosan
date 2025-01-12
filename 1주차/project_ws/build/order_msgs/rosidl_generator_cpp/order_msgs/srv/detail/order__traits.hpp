// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from order_msgs:srv/Order.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__SRV__DETAIL__ORDER__TRAITS_HPP_
#define ORDER_MSGS__SRV__DETAIL__ORDER__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "order_msgs/srv/detail/order__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace order_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const Order_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: table_num
  {
    out << "table_num: ";
    rosidl_generator_traits::value_to_yaml(msg.table_num, out);
    out << ", ";
  }

  // member: item
  {
    out << "item: ";
    rosidl_generator_traits::value_to_yaml(msg.item, out);
    out << ", ";
  }

  // member: quantity
  {
    out << "quantity: ";
    rosidl_generator_traits::value_to_yaml(msg.quantity, out);
    out << ", ";
  }

  // member: price
  {
    out << "price: ";
    rosidl_generator_traits::value_to_yaml(msg.price, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Order_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: table_num
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "table_num: ";
    rosidl_generator_traits::value_to_yaml(msg.table_num, out);
    out << "\n";
  }

  // member: item
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "item: ";
    rosidl_generator_traits::value_to_yaml(msg.item, out);
    out << "\n";
  }

  // member: quantity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "quantity: ";
    rosidl_generator_traits::value_to_yaml(msg.quantity, out);
    out << "\n";
  }

  // member: price
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "price: ";
    rosidl_generator_traits::value_to_yaml(msg.price, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Order_Request & msg, bool use_flow_style = false)
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
  const order_msgs::srv::Order_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  order_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use order_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const order_msgs::srv::Order_Request & msg)
{
  return order_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<order_msgs::srv::Order_Request>()
{
  return "order_msgs::srv::Order_Request";
}

template<>
inline const char * name<order_msgs::srv::Order_Request>()
{
  return "order_msgs/srv/Order_Request";
}

template<>
struct has_fixed_size<order_msgs::srv::Order_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<order_msgs::srv::Order_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<order_msgs::srv::Order_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace order_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const Order_Response & msg,
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
  const Order_Response & msg,
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

inline std::string to_yaml(const Order_Response & msg, bool use_flow_style = false)
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
  const order_msgs::srv::Order_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  order_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use order_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const order_msgs::srv::Order_Response & msg)
{
  return order_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<order_msgs::srv::Order_Response>()
{
  return "order_msgs::srv::Order_Response";
}

template<>
inline const char * name<order_msgs::srv::Order_Response>()
{
  return "order_msgs/srv/Order_Response";
}

template<>
struct has_fixed_size<order_msgs::srv::Order_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<order_msgs::srv::Order_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<order_msgs::srv::Order_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<order_msgs::srv::Order>()
{
  return "order_msgs::srv::Order";
}

template<>
inline const char * name<order_msgs::srv::Order>()
{
  return "order_msgs/srv/Order";
}

template<>
struct has_fixed_size<order_msgs::srv::Order>
  : std::integral_constant<
    bool,
    has_fixed_size<order_msgs::srv::Order_Request>::value &&
    has_fixed_size<order_msgs::srv::Order_Response>::value
  >
{
};

template<>
struct has_bounded_size<order_msgs::srv::Order>
  : std::integral_constant<
    bool,
    has_bounded_size<order_msgs::srv::Order_Request>::value &&
    has_bounded_size<order_msgs::srv::Order_Response>::value
  >
{
};

template<>
struct is_service<order_msgs::srv::Order>
  : std::true_type
{
};

template<>
struct is_service_request<order_msgs::srv::Order_Request>
  : std::true_type
{
};

template<>
struct is_service_response<order_msgs::srv::Order_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ORDER_MSGS__SRV__DETAIL__ORDER__TRAITS_HPP_
