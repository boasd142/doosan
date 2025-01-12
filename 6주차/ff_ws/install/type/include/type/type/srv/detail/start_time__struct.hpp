// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from type:srv/StartTime.idl
// generated code does not contain a copyright notice

#ifndef TYPE__SRV__DETAIL__START_TIME__STRUCT_HPP_
#define TYPE__SRV__DETAIL__START_TIME__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__type__srv__StartTime_Request __attribute__((deprecated))
#else
# define DEPRECATED__type__srv__StartTime_Request __declspec(deprecated)
#endif

namespace type
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct StartTime_Request_
{
  using Type = StartTime_Request_<ContainerAllocator>;

  explicit StartTime_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->start_value = 0l;
      this->job_list = "";
      this->constatus = 0l;
      this->datastatus = 0l;
    }
  }

  explicit StartTime_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : job_list(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->start_value = 0l;
      this->job_list = "";
      this->constatus = 0l;
      this->datastatus = 0l;
    }
  }

  // field types and members
  using _start_value_type =
    int32_t;
  _start_value_type start_value;
  using _job_list_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _job_list_type job_list;
  using _constatus_type =
    int32_t;
  _constatus_type constatus;
  using _datastatus_type =
    int32_t;
  _datastatus_type datastatus;

  // setters for named parameter idiom
  Type & set__start_value(
    const int32_t & _arg)
  {
    this->start_value = _arg;
    return *this;
  }
  Type & set__job_list(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->job_list = _arg;
    return *this;
  }
  Type & set__constatus(
    const int32_t & _arg)
  {
    this->constatus = _arg;
    return *this;
  }
  Type & set__datastatus(
    const int32_t & _arg)
  {
    this->datastatus = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    type::srv::StartTime_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const type::srv::StartTime_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<type::srv::StartTime_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<type::srv::StartTime_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      type::srv::StartTime_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<type::srv::StartTime_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      type::srv::StartTime_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<type::srv::StartTime_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<type::srv::StartTime_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<type::srv::StartTime_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__type__srv__StartTime_Request
    std::shared_ptr<type::srv::StartTime_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__type__srv__StartTime_Request
    std::shared_ptr<type::srv::StartTime_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StartTime_Request_ & other) const
  {
    if (this->start_value != other.start_value) {
      return false;
    }
    if (this->job_list != other.job_list) {
      return false;
    }
    if (this->constatus != other.constatus) {
      return false;
    }
    if (this->datastatus != other.datastatus) {
      return false;
    }
    return true;
  }
  bool operator!=(const StartTime_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StartTime_Request_

// alias to use template instance with default allocator
using StartTime_Request =
  type::srv::StartTime_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace type


#ifndef _WIN32
# define DEPRECATED__type__srv__StartTime_Response __attribute__((deprecated))
#else
# define DEPRECATED__type__srv__StartTime_Response __declspec(deprecated)
#endif

namespace type
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct StartTime_Response_
{
  using Type = StartTime_Response_<ContainerAllocator>;

  explicit StartTime_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->result_value = 0l;
      this->status = "";
      this->conv = "";
      this->data = "";
    }
  }

  explicit StartTime_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : status(_alloc),
    conv(_alloc),
    data(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->result_value = 0l;
      this->status = "";
      this->conv = "";
      this->data = "";
    }
  }

  // field types and members
  using _result_value_type =
    int32_t;
  _result_value_type result_value;
  using _status_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _status_type status;
  using _conv_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _conv_type conv;
  using _data_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _data_type data;

  // setters for named parameter idiom
  Type & set__result_value(
    const int32_t & _arg)
  {
    this->result_value = _arg;
    return *this;
  }
  Type & set__status(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__conv(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->conv = _arg;
    return *this;
  }
  Type & set__data(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    type::srv::StartTime_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const type::srv::StartTime_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<type::srv::StartTime_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<type::srv::StartTime_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      type::srv::StartTime_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<type::srv::StartTime_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      type::srv::StartTime_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<type::srv::StartTime_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<type::srv::StartTime_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<type::srv::StartTime_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__type__srv__StartTime_Response
    std::shared_ptr<type::srv::StartTime_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__type__srv__StartTime_Response
    std::shared_ptr<type::srv::StartTime_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StartTime_Response_ & other) const
  {
    if (this->result_value != other.result_value) {
      return false;
    }
    if (this->status != other.status) {
      return false;
    }
    if (this->conv != other.conv) {
      return false;
    }
    if (this->data != other.data) {
      return false;
    }
    return true;
  }
  bool operator!=(const StartTime_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StartTime_Response_

// alias to use template instance with default allocator
using StartTime_Response =
  type::srv::StartTime_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace type

namespace type
{

namespace srv
{

struct StartTime
{
  using Request = type::srv::StartTime_Request;
  using Response = type::srv::StartTime_Response;
};

}  // namespace srv

}  // namespace type

#endif  // TYPE__SRV__DETAIL__START_TIME__STRUCT_HPP_
