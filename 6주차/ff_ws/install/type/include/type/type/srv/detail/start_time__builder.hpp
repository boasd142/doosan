// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from type:srv/StartTime.idl
// generated code does not contain a copyright notice

#ifndef TYPE__SRV__DETAIL__START_TIME__BUILDER_HPP_
#define TYPE__SRV__DETAIL__START_TIME__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "type/srv/detail/start_time__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace type
{

namespace srv
{

namespace builder
{

class Init_StartTime_Request_datastatus
{
public:
  explicit Init_StartTime_Request_datastatus(::type::srv::StartTime_Request & msg)
  : msg_(msg)
  {}
  ::type::srv::StartTime_Request datastatus(::type::srv::StartTime_Request::_datastatus_type arg)
  {
    msg_.datastatus = std::move(arg);
    return std::move(msg_);
  }

private:
  ::type::srv::StartTime_Request msg_;
};

class Init_StartTime_Request_constatus
{
public:
  explicit Init_StartTime_Request_constatus(::type::srv::StartTime_Request & msg)
  : msg_(msg)
  {}
  Init_StartTime_Request_datastatus constatus(::type::srv::StartTime_Request::_constatus_type arg)
  {
    msg_.constatus = std::move(arg);
    return Init_StartTime_Request_datastatus(msg_);
  }

private:
  ::type::srv::StartTime_Request msg_;
};

class Init_StartTime_Request_job_list
{
public:
  explicit Init_StartTime_Request_job_list(::type::srv::StartTime_Request & msg)
  : msg_(msg)
  {}
  Init_StartTime_Request_constatus job_list(::type::srv::StartTime_Request::_job_list_type arg)
  {
    msg_.job_list = std::move(arg);
    return Init_StartTime_Request_constatus(msg_);
  }

private:
  ::type::srv::StartTime_Request msg_;
};

class Init_StartTime_Request_start_value
{
public:
  Init_StartTime_Request_start_value()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_StartTime_Request_job_list start_value(::type::srv::StartTime_Request::_start_value_type arg)
  {
    msg_.start_value = std::move(arg);
    return Init_StartTime_Request_job_list(msg_);
  }

private:
  ::type::srv::StartTime_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::type::srv::StartTime_Request>()
{
  return type::srv::builder::Init_StartTime_Request_start_value();
}

}  // namespace type


namespace type
{

namespace srv
{

namespace builder
{

class Init_StartTime_Response_data
{
public:
  explicit Init_StartTime_Response_data(::type::srv::StartTime_Response & msg)
  : msg_(msg)
  {}
  ::type::srv::StartTime_Response data(::type::srv::StartTime_Response::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::type::srv::StartTime_Response msg_;
};

class Init_StartTime_Response_conv
{
public:
  explicit Init_StartTime_Response_conv(::type::srv::StartTime_Response & msg)
  : msg_(msg)
  {}
  Init_StartTime_Response_data conv(::type::srv::StartTime_Response::_conv_type arg)
  {
    msg_.conv = std::move(arg);
    return Init_StartTime_Response_data(msg_);
  }

private:
  ::type::srv::StartTime_Response msg_;
};

class Init_StartTime_Response_status
{
public:
  explicit Init_StartTime_Response_status(::type::srv::StartTime_Response & msg)
  : msg_(msg)
  {}
  Init_StartTime_Response_conv status(::type::srv::StartTime_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_StartTime_Response_conv(msg_);
  }

private:
  ::type::srv::StartTime_Response msg_;
};

class Init_StartTime_Response_result_value
{
public:
  Init_StartTime_Response_result_value()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_StartTime_Response_status result_value(::type::srv::StartTime_Response::_result_value_type arg)
  {
    msg_.result_value = std::move(arg);
    return Init_StartTime_Response_status(msg_);
  }

private:
  ::type::srv::StartTime_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::type::srv::StartTime_Response>()
{
  return type::srv::builder::Init_StartTime_Response_result_value();
}

}  // namespace type

#endif  // TYPE__SRV__DETAIL__START_TIME__BUILDER_HPP_
