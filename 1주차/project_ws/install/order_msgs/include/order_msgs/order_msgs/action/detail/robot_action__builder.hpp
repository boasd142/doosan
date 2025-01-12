// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from order_msgs:action/RobotAction.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__ACTION__DETAIL__ROBOT_ACTION__BUILDER_HPP_
#define ORDER_MSGS__ACTION__DETAIL__ROBOT_ACTION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "order_msgs/action/detail/robot_action__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace order_msgs
{

namespace action
{

namespace builder
{

class Init_RobotAction_Goal_table_num
{
public:
  Init_RobotAction_Goal_table_num()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::order_msgs::action::RobotAction_Goal table_num(::order_msgs::action::RobotAction_Goal::_table_num_type arg)
  {
    msg_.table_num = std::move(arg);
    return std::move(msg_);
  }

private:
  ::order_msgs::action::RobotAction_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::order_msgs::action::RobotAction_Goal>()
{
  return order_msgs::action::builder::Init_RobotAction_Goal_table_num();
}

}  // namespace order_msgs


namespace order_msgs
{

namespace action
{

namespace builder
{

class Init_RobotAction_Result_result
{
public:
  Init_RobotAction_Result_result()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::order_msgs::action::RobotAction_Result result(::order_msgs::action::RobotAction_Result::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::order_msgs::action::RobotAction_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::order_msgs::action::RobotAction_Result>()
{
  return order_msgs::action::builder::Init_RobotAction_Result_result();
}

}  // namespace order_msgs


namespace order_msgs
{

namespace action
{

namespace builder
{

class Init_RobotAction_Feedback_delivery
{
public:
  Init_RobotAction_Feedback_delivery()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::order_msgs::action::RobotAction_Feedback delivery(::order_msgs::action::RobotAction_Feedback::_delivery_type arg)
  {
    msg_.delivery = std::move(arg);
    return std::move(msg_);
  }

private:
  ::order_msgs::action::RobotAction_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::order_msgs::action::RobotAction_Feedback>()
{
  return order_msgs::action::builder::Init_RobotAction_Feedback_delivery();
}

}  // namespace order_msgs


namespace order_msgs
{

namespace action
{

namespace builder
{

class Init_RobotAction_SendGoal_Request_goal
{
public:
  explicit Init_RobotAction_SendGoal_Request_goal(::order_msgs::action::RobotAction_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::order_msgs::action::RobotAction_SendGoal_Request goal(::order_msgs::action::RobotAction_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::order_msgs::action::RobotAction_SendGoal_Request msg_;
};

class Init_RobotAction_SendGoal_Request_goal_id
{
public:
  Init_RobotAction_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotAction_SendGoal_Request_goal goal_id(::order_msgs::action::RobotAction_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_RobotAction_SendGoal_Request_goal(msg_);
  }

private:
  ::order_msgs::action::RobotAction_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::order_msgs::action::RobotAction_SendGoal_Request>()
{
  return order_msgs::action::builder::Init_RobotAction_SendGoal_Request_goal_id();
}

}  // namespace order_msgs


namespace order_msgs
{

namespace action
{

namespace builder
{

class Init_RobotAction_SendGoal_Response_stamp
{
public:
  explicit Init_RobotAction_SendGoal_Response_stamp(::order_msgs::action::RobotAction_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::order_msgs::action::RobotAction_SendGoal_Response stamp(::order_msgs::action::RobotAction_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::order_msgs::action::RobotAction_SendGoal_Response msg_;
};

class Init_RobotAction_SendGoal_Response_accepted
{
public:
  Init_RobotAction_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotAction_SendGoal_Response_stamp accepted(::order_msgs::action::RobotAction_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_RobotAction_SendGoal_Response_stamp(msg_);
  }

private:
  ::order_msgs::action::RobotAction_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::order_msgs::action::RobotAction_SendGoal_Response>()
{
  return order_msgs::action::builder::Init_RobotAction_SendGoal_Response_accepted();
}

}  // namespace order_msgs


namespace order_msgs
{

namespace action
{

namespace builder
{

class Init_RobotAction_GetResult_Request_goal_id
{
public:
  Init_RobotAction_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::order_msgs::action::RobotAction_GetResult_Request goal_id(::order_msgs::action::RobotAction_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::order_msgs::action::RobotAction_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::order_msgs::action::RobotAction_GetResult_Request>()
{
  return order_msgs::action::builder::Init_RobotAction_GetResult_Request_goal_id();
}

}  // namespace order_msgs


namespace order_msgs
{

namespace action
{

namespace builder
{

class Init_RobotAction_GetResult_Response_result
{
public:
  explicit Init_RobotAction_GetResult_Response_result(::order_msgs::action::RobotAction_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::order_msgs::action::RobotAction_GetResult_Response result(::order_msgs::action::RobotAction_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::order_msgs::action::RobotAction_GetResult_Response msg_;
};

class Init_RobotAction_GetResult_Response_status
{
public:
  Init_RobotAction_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotAction_GetResult_Response_result status(::order_msgs::action::RobotAction_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_RobotAction_GetResult_Response_result(msg_);
  }

private:
  ::order_msgs::action::RobotAction_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::order_msgs::action::RobotAction_GetResult_Response>()
{
  return order_msgs::action::builder::Init_RobotAction_GetResult_Response_status();
}

}  // namespace order_msgs


namespace order_msgs
{

namespace action
{

namespace builder
{

class Init_RobotAction_FeedbackMessage_feedback
{
public:
  explicit Init_RobotAction_FeedbackMessage_feedback(::order_msgs::action::RobotAction_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::order_msgs::action::RobotAction_FeedbackMessage feedback(::order_msgs::action::RobotAction_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::order_msgs::action::RobotAction_FeedbackMessage msg_;
};

class Init_RobotAction_FeedbackMessage_goal_id
{
public:
  Init_RobotAction_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotAction_FeedbackMessage_feedback goal_id(::order_msgs::action::RobotAction_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_RobotAction_FeedbackMessage_feedback(msg_);
  }

private:
  ::order_msgs::action::RobotAction_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::order_msgs::action::RobotAction_FeedbackMessage>()
{
  return order_msgs::action::builder::Init_RobotAction_FeedbackMessage_goal_id();
}

}  // namespace order_msgs

#endif  // ORDER_MSGS__ACTION__DETAIL__ROBOT_ACTION__BUILDER_HPP_
