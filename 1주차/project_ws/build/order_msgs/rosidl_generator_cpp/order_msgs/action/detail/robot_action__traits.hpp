// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from order_msgs:action/RobotAction.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__ACTION__DETAIL__ROBOT_ACTION__TRAITS_HPP_
#define ORDER_MSGS__ACTION__DETAIL__ROBOT_ACTION__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "order_msgs/action/detail/robot_action__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace order_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotAction_Goal & msg,
  std::ostream & out)
{
  out << "{";
  // member: table_num
  {
    out << "table_num: ";
    rosidl_generator_traits::value_to_yaml(msg.table_num, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotAction_Goal & msg,
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
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotAction_Goal & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace order_msgs

namespace rosidl_generator_traits
{

[[deprecated("use order_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const order_msgs::action::RobotAction_Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  order_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use order_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const order_msgs::action::RobotAction_Goal & msg)
{
  return order_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<order_msgs::action::RobotAction_Goal>()
{
  return "order_msgs::action::RobotAction_Goal";
}

template<>
inline const char * name<order_msgs::action::RobotAction_Goal>()
{
  return "order_msgs/action/RobotAction_Goal";
}

template<>
struct has_fixed_size<order_msgs::action::RobotAction_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<order_msgs::action::RobotAction_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<order_msgs::action::RobotAction_Goal>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace order_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotAction_Result & msg,
  std::ostream & out)
{
  out << "{";
  // member: result
  {
    out << "result: ";
    rosidl_generator_traits::value_to_yaml(msg.result, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotAction_Result & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: result
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "result: ";
    rosidl_generator_traits::value_to_yaml(msg.result, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotAction_Result & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace order_msgs

namespace rosidl_generator_traits
{

[[deprecated("use order_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const order_msgs::action::RobotAction_Result & msg,
  std::ostream & out, size_t indentation = 0)
{
  order_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use order_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const order_msgs::action::RobotAction_Result & msg)
{
  return order_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<order_msgs::action::RobotAction_Result>()
{
  return "order_msgs::action::RobotAction_Result";
}

template<>
inline const char * name<order_msgs::action::RobotAction_Result>()
{
  return "order_msgs/action/RobotAction_Result";
}

template<>
struct has_fixed_size<order_msgs::action::RobotAction_Result>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<order_msgs::action::RobotAction_Result>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<order_msgs::action::RobotAction_Result>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace order_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotAction_Feedback & msg,
  std::ostream & out)
{
  out << "{";
  // member: delivery
  {
    if (msg.delivery.size() == 0) {
      out << "delivery: []";
    } else {
      out << "delivery: [";
      size_t pending_items = msg.delivery.size();
      for (auto item : msg.delivery) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotAction_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: delivery
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.delivery.size() == 0) {
      out << "delivery: []\n";
    } else {
      out << "delivery:\n";
      for (auto item : msg.delivery) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotAction_Feedback & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace order_msgs

namespace rosidl_generator_traits
{

[[deprecated("use order_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const order_msgs::action::RobotAction_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  order_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use order_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const order_msgs::action::RobotAction_Feedback & msg)
{
  return order_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<order_msgs::action::RobotAction_Feedback>()
{
  return "order_msgs::action::RobotAction_Feedback";
}

template<>
inline const char * name<order_msgs::action::RobotAction_Feedback>()
{
  return "order_msgs/action/RobotAction_Feedback";
}

template<>
struct has_fixed_size<order_msgs::action::RobotAction_Feedback>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<order_msgs::action::RobotAction_Feedback>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<order_msgs::action::RobotAction_Feedback>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'goal'
#include "order_msgs/action/detail/robot_action__traits.hpp"

namespace order_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotAction_SendGoal_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
    out << ", ";
  }

  // member: goal
  {
    out << "goal: ";
    to_flow_style_yaml(msg.goal, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotAction_SendGoal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: goal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal:\n";
    to_block_style_yaml(msg.goal, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotAction_SendGoal_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace order_msgs

namespace rosidl_generator_traits
{

[[deprecated("use order_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const order_msgs::action::RobotAction_SendGoal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  order_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use order_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const order_msgs::action::RobotAction_SendGoal_Request & msg)
{
  return order_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<order_msgs::action::RobotAction_SendGoal_Request>()
{
  return "order_msgs::action::RobotAction_SendGoal_Request";
}

template<>
inline const char * name<order_msgs::action::RobotAction_SendGoal_Request>()
{
  return "order_msgs/action/RobotAction_SendGoal_Request";
}

template<>
struct has_fixed_size<order_msgs::action::RobotAction_SendGoal_Request>
  : std::integral_constant<bool, has_fixed_size<order_msgs::action::RobotAction_Goal>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<order_msgs::action::RobotAction_SendGoal_Request>
  : std::integral_constant<bool, has_bounded_size<order_msgs::action::RobotAction_Goal>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<order_msgs::action::RobotAction_SendGoal_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace order_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotAction_SendGoal_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: accepted
  {
    out << "accepted: ";
    rosidl_generator_traits::value_to_yaml(msg.accepted, out);
    out << ", ";
  }

  // member: stamp
  {
    out << "stamp: ";
    to_flow_style_yaml(msg.stamp, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotAction_SendGoal_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: accepted
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "accepted: ";
    rosidl_generator_traits::value_to_yaml(msg.accepted, out);
    out << "\n";
  }

  // member: stamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stamp:\n";
    to_block_style_yaml(msg.stamp, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotAction_SendGoal_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace order_msgs

namespace rosidl_generator_traits
{

[[deprecated("use order_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const order_msgs::action::RobotAction_SendGoal_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  order_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use order_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const order_msgs::action::RobotAction_SendGoal_Response & msg)
{
  return order_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<order_msgs::action::RobotAction_SendGoal_Response>()
{
  return "order_msgs::action::RobotAction_SendGoal_Response";
}

template<>
inline const char * name<order_msgs::action::RobotAction_SendGoal_Response>()
{
  return "order_msgs/action/RobotAction_SendGoal_Response";
}

template<>
struct has_fixed_size<order_msgs::action::RobotAction_SendGoal_Response>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<order_msgs::action::RobotAction_SendGoal_Response>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<order_msgs::action::RobotAction_SendGoal_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<order_msgs::action::RobotAction_SendGoal>()
{
  return "order_msgs::action::RobotAction_SendGoal";
}

template<>
inline const char * name<order_msgs::action::RobotAction_SendGoal>()
{
  return "order_msgs/action/RobotAction_SendGoal";
}

template<>
struct has_fixed_size<order_msgs::action::RobotAction_SendGoal>
  : std::integral_constant<
    bool,
    has_fixed_size<order_msgs::action::RobotAction_SendGoal_Request>::value &&
    has_fixed_size<order_msgs::action::RobotAction_SendGoal_Response>::value
  >
{
};

template<>
struct has_bounded_size<order_msgs::action::RobotAction_SendGoal>
  : std::integral_constant<
    bool,
    has_bounded_size<order_msgs::action::RobotAction_SendGoal_Request>::value &&
    has_bounded_size<order_msgs::action::RobotAction_SendGoal_Response>::value
  >
{
};

template<>
struct is_service<order_msgs::action::RobotAction_SendGoal>
  : std::true_type
{
};

template<>
struct is_service_request<order_msgs::action::RobotAction_SendGoal_Request>
  : std::true_type
{
};

template<>
struct is_service_response<order_msgs::action::RobotAction_SendGoal_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"

namespace order_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotAction_GetResult_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotAction_GetResult_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotAction_GetResult_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace order_msgs

namespace rosidl_generator_traits
{

[[deprecated("use order_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const order_msgs::action::RobotAction_GetResult_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  order_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use order_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const order_msgs::action::RobotAction_GetResult_Request & msg)
{
  return order_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<order_msgs::action::RobotAction_GetResult_Request>()
{
  return "order_msgs::action::RobotAction_GetResult_Request";
}

template<>
inline const char * name<order_msgs::action::RobotAction_GetResult_Request>()
{
  return "order_msgs/action/RobotAction_GetResult_Request";
}

template<>
struct has_fixed_size<order_msgs::action::RobotAction_GetResult_Request>
  : std::integral_constant<bool, has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<order_msgs::action::RobotAction_GetResult_Request>
  : std::integral_constant<bool, has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<order_msgs::action::RobotAction_GetResult_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'result'
// already included above
// #include "order_msgs/action/detail/robot_action__traits.hpp"

namespace order_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotAction_GetResult_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: status
  {
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << ", ";
  }

  // member: result
  {
    out << "result: ";
    to_flow_style_yaml(msg.result, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotAction_GetResult_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << "\n";
  }

  // member: result
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "result:\n";
    to_block_style_yaml(msg.result, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotAction_GetResult_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace order_msgs

namespace rosidl_generator_traits
{

[[deprecated("use order_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const order_msgs::action::RobotAction_GetResult_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  order_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use order_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const order_msgs::action::RobotAction_GetResult_Response & msg)
{
  return order_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<order_msgs::action::RobotAction_GetResult_Response>()
{
  return "order_msgs::action::RobotAction_GetResult_Response";
}

template<>
inline const char * name<order_msgs::action::RobotAction_GetResult_Response>()
{
  return "order_msgs/action/RobotAction_GetResult_Response";
}

template<>
struct has_fixed_size<order_msgs::action::RobotAction_GetResult_Response>
  : std::integral_constant<bool, has_fixed_size<order_msgs::action::RobotAction_Result>::value> {};

template<>
struct has_bounded_size<order_msgs::action::RobotAction_GetResult_Response>
  : std::integral_constant<bool, has_bounded_size<order_msgs::action::RobotAction_Result>::value> {};

template<>
struct is_message<order_msgs::action::RobotAction_GetResult_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<order_msgs::action::RobotAction_GetResult>()
{
  return "order_msgs::action::RobotAction_GetResult";
}

template<>
inline const char * name<order_msgs::action::RobotAction_GetResult>()
{
  return "order_msgs/action/RobotAction_GetResult";
}

template<>
struct has_fixed_size<order_msgs::action::RobotAction_GetResult>
  : std::integral_constant<
    bool,
    has_fixed_size<order_msgs::action::RobotAction_GetResult_Request>::value &&
    has_fixed_size<order_msgs::action::RobotAction_GetResult_Response>::value
  >
{
};

template<>
struct has_bounded_size<order_msgs::action::RobotAction_GetResult>
  : std::integral_constant<
    bool,
    has_bounded_size<order_msgs::action::RobotAction_GetResult_Request>::value &&
    has_bounded_size<order_msgs::action::RobotAction_GetResult_Response>::value
  >
{
};

template<>
struct is_service<order_msgs::action::RobotAction_GetResult>
  : std::true_type
{
};

template<>
struct is_service_request<order_msgs::action::RobotAction_GetResult_Request>
  : std::true_type
{
};

template<>
struct is_service_response<order_msgs::action::RobotAction_GetResult_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'feedback'
// already included above
// #include "order_msgs/action/detail/robot_action__traits.hpp"

namespace order_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const RobotAction_FeedbackMessage & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
    out << ", ";
  }

  // member: feedback
  {
    out << "feedback: ";
    to_flow_style_yaml(msg.feedback, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotAction_FeedbackMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: feedback
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "feedback:\n";
    to_block_style_yaml(msg.feedback, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotAction_FeedbackMessage & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace order_msgs

namespace rosidl_generator_traits
{

[[deprecated("use order_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const order_msgs::action::RobotAction_FeedbackMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  order_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use order_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const order_msgs::action::RobotAction_FeedbackMessage & msg)
{
  return order_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<order_msgs::action::RobotAction_FeedbackMessage>()
{
  return "order_msgs::action::RobotAction_FeedbackMessage";
}

template<>
inline const char * name<order_msgs::action::RobotAction_FeedbackMessage>()
{
  return "order_msgs/action/RobotAction_FeedbackMessage";
}

template<>
struct has_fixed_size<order_msgs::action::RobotAction_FeedbackMessage>
  : std::integral_constant<bool, has_fixed_size<order_msgs::action::RobotAction_Feedback>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<order_msgs::action::RobotAction_FeedbackMessage>
  : std::integral_constant<bool, has_bounded_size<order_msgs::action::RobotAction_Feedback>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<order_msgs::action::RobotAction_FeedbackMessage>
  : std::true_type {};

}  // namespace rosidl_generator_traits


namespace rosidl_generator_traits
{

template<>
struct is_action<order_msgs::action::RobotAction>
  : std::true_type
{
};

template<>
struct is_action_goal<order_msgs::action::RobotAction_Goal>
  : std::true_type
{
};

template<>
struct is_action_result<order_msgs::action::RobotAction_Result>
  : std::true_type
{
};

template<>
struct is_action_feedback<order_msgs::action::RobotAction_Feedback>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits


#endif  // ORDER_MSGS__ACTION__DETAIL__ROBOT_ACTION__TRAITS_HPP_
