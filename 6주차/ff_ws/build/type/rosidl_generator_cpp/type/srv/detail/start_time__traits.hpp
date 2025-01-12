// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from type:srv/StartTime.idl
// generated code does not contain a copyright notice

#ifndef TYPE__SRV__DETAIL__START_TIME__TRAITS_HPP_
#define TYPE__SRV__DETAIL__START_TIME__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "type/srv/detail/start_time__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace type
{

namespace srv
{

inline void to_flow_style_yaml(
  const StartTime_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: start_value
  {
    out << "start_value: ";
    rosidl_generator_traits::value_to_yaml(msg.start_value, out);
    out << ", ";
  }

  // member: job_list
  {
    out << "job_list: ";
    rosidl_generator_traits::value_to_yaml(msg.job_list, out);
    out << ", ";
  }

  // member: constatus
  {
    out << "constatus: ";
    rosidl_generator_traits::value_to_yaml(msg.constatus, out);
    out << ", ";
  }

  // member: datastatus
  {
    out << "datastatus: ";
    rosidl_generator_traits::value_to_yaml(msg.datastatus, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const StartTime_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: start_value
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "start_value: ";
    rosidl_generator_traits::value_to_yaml(msg.start_value, out);
    out << "\n";
  }

  // member: job_list
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "job_list: ";
    rosidl_generator_traits::value_to_yaml(msg.job_list, out);
    out << "\n";
  }

  // member: constatus
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "constatus: ";
    rosidl_generator_traits::value_to_yaml(msg.constatus, out);
    out << "\n";
  }

  // member: datastatus
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "datastatus: ";
    rosidl_generator_traits::value_to_yaml(msg.datastatus, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const StartTime_Request & msg, bool use_flow_style = false)
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

}  // namespace type

namespace rosidl_generator_traits
{

[[deprecated("use type::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const type::srv::StartTime_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  type::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use type::srv::to_yaml() instead")]]
inline std::string to_yaml(const type::srv::StartTime_Request & msg)
{
  return type::srv::to_yaml(msg);
}

template<>
inline const char * data_type<type::srv::StartTime_Request>()
{
  return "type::srv::StartTime_Request";
}

template<>
inline const char * name<type::srv::StartTime_Request>()
{
  return "type/srv/StartTime_Request";
}

template<>
struct has_fixed_size<type::srv::StartTime_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<type::srv::StartTime_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<type::srv::StartTime_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace type
{

namespace srv
{

inline void to_flow_style_yaml(
  const StartTime_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: result_value
  {
    out << "result_value: ";
    rosidl_generator_traits::value_to_yaml(msg.result_value, out);
    out << ", ";
  }

  // member: status
  {
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << ", ";
  }

  // member: conv
  {
    out << "conv: ";
    rosidl_generator_traits::value_to_yaml(msg.conv, out);
    out << ", ";
  }

  // member: data
  {
    out << "data: ";
    rosidl_generator_traits::value_to_yaml(msg.data, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const StartTime_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: result_value
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "result_value: ";
    rosidl_generator_traits::value_to_yaml(msg.result_value, out);
    out << "\n";
  }

  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << "\n";
  }

  // member: conv
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "conv: ";
    rosidl_generator_traits::value_to_yaml(msg.conv, out);
    out << "\n";
  }

  // member: data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "data: ";
    rosidl_generator_traits::value_to_yaml(msg.data, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const StartTime_Response & msg, bool use_flow_style = false)
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

}  // namespace type

namespace rosidl_generator_traits
{

[[deprecated("use type::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const type::srv::StartTime_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  type::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use type::srv::to_yaml() instead")]]
inline std::string to_yaml(const type::srv::StartTime_Response & msg)
{
  return type::srv::to_yaml(msg);
}

template<>
inline const char * data_type<type::srv::StartTime_Response>()
{
  return "type::srv::StartTime_Response";
}

template<>
inline const char * name<type::srv::StartTime_Response>()
{
  return "type/srv/StartTime_Response";
}

template<>
struct has_fixed_size<type::srv::StartTime_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<type::srv::StartTime_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<type::srv::StartTime_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<type::srv::StartTime>()
{
  return "type::srv::StartTime";
}

template<>
inline const char * name<type::srv::StartTime>()
{
  return "type/srv/StartTime";
}

template<>
struct has_fixed_size<type::srv::StartTime>
  : std::integral_constant<
    bool,
    has_fixed_size<type::srv::StartTime_Request>::value &&
    has_fixed_size<type::srv::StartTime_Response>::value
  >
{
};

template<>
struct has_bounded_size<type::srv::StartTime>
  : std::integral_constant<
    bool,
    has_bounded_size<type::srv::StartTime_Request>::value &&
    has_bounded_size<type::srv::StartTime_Response>::value
  >
{
};

template<>
struct is_service<type::srv::StartTime>
  : std::true_type
{
};

template<>
struct is_service_request<type::srv::StartTime_Request>
  : std::true_type
{
};

template<>
struct is_service_response<type::srv::StartTime_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // TYPE__SRV__DETAIL__START_TIME__TRAITS_HPP_
