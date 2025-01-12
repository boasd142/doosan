// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from order_msgs:srv/Order.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__SRV__DETAIL__ORDER__BUILDER_HPP_
#define ORDER_MSGS__SRV__DETAIL__ORDER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "order_msgs/srv/detail/order__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace order_msgs
{

namespace srv
{

namespace builder
{

class Init_Order_Request_price
{
public:
  explicit Init_Order_Request_price(::order_msgs::srv::Order_Request & msg)
  : msg_(msg)
  {}
  ::order_msgs::srv::Order_Request price(::order_msgs::srv::Order_Request::_price_type arg)
  {
    msg_.price = std::move(arg);
    return std::move(msg_);
  }

private:
  ::order_msgs::srv::Order_Request msg_;
};

class Init_Order_Request_quantity
{
public:
  explicit Init_Order_Request_quantity(::order_msgs::srv::Order_Request & msg)
  : msg_(msg)
  {}
  Init_Order_Request_price quantity(::order_msgs::srv::Order_Request::_quantity_type arg)
  {
    msg_.quantity = std::move(arg);
    return Init_Order_Request_price(msg_);
  }

private:
  ::order_msgs::srv::Order_Request msg_;
};

class Init_Order_Request_item
{
public:
  explicit Init_Order_Request_item(::order_msgs::srv::Order_Request & msg)
  : msg_(msg)
  {}
  Init_Order_Request_quantity item(::order_msgs::srv::Order_Request::_item_type arg)
  {
    msg_.item = std::move(arg);
    return Init_Order_Request_quantity(msg_);
  }

private:
  ::order_msgs::srv::Order_Request msg_;
};

class Init_Order_Request_table_num
{
public:
  Init_Order_Request_table_num()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Order_Request_item table_num(::order_msgs::srv::Order_Request::_table_num_type arg)
  {
    msg_.table_num = std::move(arg);
    return Init_Order_Request_item(msg_);
  }

private:
  ::order_msgs::srv::Order_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::order_msgs::srv::Order_Request>()
{
  return order_msgs::srv::builder::Init_Order_Request_table_num();
}

}  // namespace order_msgs


namespace order_msgs
{

namespace srv
{

namespace builder
{

class Init_Order_Response_message
{
public:
  explicit Init_Order_Response_message(::order_msgs::srv::Order_Response & msg)
  : msg_(msg)
  {}
  ::order_msgs::srv::Order_Response message(::order_msgs::srv::Order_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::order_msgs::srv::Order_Response msg_;
};

class Init_Order_Response_success
{
public:
  Init_Order_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Order_Response_message success(::order_msgs::srv::Order_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_Order_Response_message(msg_);
  }

private:
  ::order_msgs::srv::Order_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::order_msgs::srv::Order_Response>()
{
  return order_msgs::srv::builder::Init_Order_Response_success();
}

}  // namespace order_msgs

#endif  // ORDER_MSGS__SRV__DETAIL__ORDER__BUILDER_HPP_
