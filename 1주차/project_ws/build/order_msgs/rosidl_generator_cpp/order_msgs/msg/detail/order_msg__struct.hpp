// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from order_msgs:msg/OrderMsg.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__MSG__DETAIL__ORDER_MSG__STRUCT_HPP_
#define ORDER_MSGS__MSG__DETAIL__ORDER_MSG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__order_msgs__msg__OrderMsg __attribute__((deprecated))
#else
# define DEPRECATED__order_msgs__msg__OrderMsg __declspec(deprecated)
#endif

namespace order_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct OrderMsg_
{
  using Type = OrderMsg_<ContainerAllocator>;

  explicit OrderMsg_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit OrderMsg_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    order_msgs::msg::OrderMsg_<ContainerAllocator> *;
  using ConstRawPtr =
    const order_msgs::msg::OrderMsg_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<order_msgs::msg::OrderMsg_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<order_msgs::msg::OrderMsg_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      order_msgs::msg::OrderMsg_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<order_msgs::msg::OrderMsg_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      order_msgs::msg::OrderMsg_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<order_msgs::msg::OrderMsg_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<order_msgs::msg::OrderMsg_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<order_msgs::msg::OrderMsg_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__order_msgs__msg__OrderMsg
    std::shared_ptr<order_msgs::msg::OrderMsg_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__order_msgs__msg__OrderMsg
    std::shared_ptr<order_msgs::msg::OrderMsg_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const OrderMsg_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const OrderMsg_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct OrderMsg_

// alias to use template instance with default allocator
using OrderMsg =
  order_msgs::msg::OrderMsg_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace order_msgs

#endif  // ORDER_MSGS__MSG__DETAIL__ORDER_MSG__STRUCT_HPP_
