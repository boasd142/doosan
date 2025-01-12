// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from order_msgs:srv/Order.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__SRV__DETAIL__ORDER__STRUCT_HPP_
#define ORDER_MSGS__SRV__DETAIL__ORDER__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__order_msgs__srv__Order_Request __attribute__((deprecated))
#else
# define DEPRECATED__order_msgs__srv__Order_Request __declspec(deprecated)
#endif

namespace order_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Order_Request_
{
  using Type = Order_Request_<ContainerAllocator>;

  explicit Order_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->table_num = "";
      this->item = "";
      this->quantity = 0l;
      this->price = 0l;
    }
  }

  explicit Order_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : table_num(_alloc),
    item(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->table_num = "";
      this->item = "";
      this->quantity = 0l;
      this->price = 0l;
    }
  }

  // field types and members
  using _table_num_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _table_num_type table_num;
  using _item_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _item_type item;
  using _quantity_type =
    int32_t;
  _quantity_type quantity;
  using _price_type =
    int32_t;
  _price_type price;

  // setters for named parameter idiom
  Type & set__table_num(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->table_num = _arg;
    return *this;
  }
  Type & set__item(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->item = _arg;
    return *this;
  }
  Type & set__quantity(
    const int32_t & _arg)
  {
    this->quantity = _arg;
    return *this;
  }
  Type & set__price(
    const int32_t & _arg)
  {
    this->price = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    order_msgs::srv::Order_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const order_msgs::srv::Order_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<order_msgs::srv::Order_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<order_msgs::srv::Order_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      order_msgs::srv::Order_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<order_msgs::srv::Order_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      order_msgs::srv::Order_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<order_msgs::srv::Order_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<order_msgs::srv::Order_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<order_msgs::srv::Order_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__order_msgs__srv__Order_Request
    std::shared_ptr<order_msgs::srv::Order_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__order_msgs__srv__Order_Request
    std::shared_ptr<order_msgs::srv::Order_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Order_Request_ & other) const
  {
    if (this->table_num != other.table_num) {
      return false;
    }
    if (this->item != other.item) {
      return false;
    }
    if (this->quantity != other.quantity) {
      return false;
    }
    if (this->price != other.price) {
      return false;
    }
    return true;
  }
  bool operator!=(const Order_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Order_Request_

// alias to use template instance with default allocator
using Order_Request =
  order_msgs::srv::Order_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace order_msgs


#ifndef _WIN32
# define DEPRECATED__order_msgs__srv__Order_Response __attribute__((deprecated))
#else
# define DEPRECATED__order_msgs__srv__Order_Response __declspec(deprecated)
#endif

namespace order_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Order_Response_
{
  using Type = Order_Response_<ContainerAllocator>;

  explicit Order_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  explicit Order_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _message_type message;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__message(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->message = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    order_msgs::srv::Order_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const order_msgs::srv::Order_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<order_msgs::srv::Order_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<order_msgs::srv::Order_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      order_msgs::srv::Order_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<order_msgs::srv::Order_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      order_msgs::srv::Order_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<order_msgs::srv::Order_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<order_msgs::srv::Order_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<order_msgs::srv::Order_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__order_msgs__srv__Order_Response
    std::shared_ptr<order_msgs::srv::Order_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__order_msgs__srv__Order_Response
    std::shared_ptr<order_msgs::srv::Order_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Order_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->message != other.message) {
      return false;
    }
    return true;
  }
  bool operator!=(const Order_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Order_Response_

// alias to use template instance with default allocator
using Order_Response =
  order_msgs::srv::Order_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace order_msgs

namespace order_msgs
{

namespace srv
{

struct Order
{
  using Request = order_msgs::srv::Order_Request;
  using Response = order_msgs::srv::Order_Response;
};

}  // namespace srv

}  // namespace order_msgs

#endif  // ORDER_MSGS__SRV__DETAIL__ORDER__STRUCT_HPP_
