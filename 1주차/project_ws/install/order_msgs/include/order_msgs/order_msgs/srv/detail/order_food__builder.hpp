// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from order_msgs:srv/OrderFood.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__SRV__DETAIL__ORDER_FOOD__BUILDER_HPP_
#define ORDER_MSGS__SRV__DETAIL__ORDER_FOOD__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "order_msgs/srv/detail/order_food__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace order_msgs
{

namespace srv
{

namespace builder
{

class Init_OrderFood_Request_item_name
{
public:
  Init_OrderFood_Request_item_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::order_msgs::srv::OrderFood_Request item_name(::order_msgs::srv::OrderFood_Request::_item_name_type arg)
  {
    msg_.item_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::order_msgs::srv::OrderFood_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::order_msgs::srv::OrderFood_Request>()
{
  return order_msgs::srv::builder::Init_OrderFood_Request_item_name();
}

}  // namespace order_msgs


namespace order_msgs
{

namespace srv
{

namespace builder
{

class Init_OrderFood_Response_message
{
public:
  explicit Init_OrderFood_Response_message(::order_msgs::srv::OrderFood_Response & msg)
  : msg_(msg)
  {}
  ::order_msgs::srv::OrderFood_Response message(::order_msgs::srv::OrderFood_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::order_msgs::srv::OrderFood_Response msg_;
};

class Init_OrderFood_Response_success
{
public:
  Init_OrderFood_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_OrderFood_Response_message success(::order_msgs::srv::OrderFood_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_OrderFood_Response_message(msg_);
  }

private:
  ::order_msgs::srv::OrderFood_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::order_msgs::srv::OrderFood_Response>()
{
  return order_msgs::srv::builder::Init_OrderFood_Response_success();
}

}  // namespace order_msgs

#endif  // ORDER_MSGS__SRV__DETAIL__ORDER_FOOD__BUILDER_HPP_
