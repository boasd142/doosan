// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from order_msgs:action/RobotAction.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__ACTION__DETAIL__ROBOT_ACTION__STRUCT_HPP_
#define ORDER_MSGS__ACTION__DETAIL__ROBOT_ACTION__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__order_msgs__action__RobotAction_Goal __attribute__((deprecated))
#else
# define DEPRECATED__order_msgs__action__RobotAction_Goal __declspec(deprecated)
#endif

namespace order_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotAction_Goal_
{
  using Type = RobotAction_Goal_<ContainerAllocator>;

  explicit RobotAction_Goal_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->table_num = 0ll;
    }
  }

  explicit RobotAction_Goal_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->table_num = 0ll;
    }
  }

  // field types and members
  using _table_num_type =
    int64_t;
  _table_num_type table_num;

  // setters for named parameter idiom
  Type & set__table_num(
    const int64_t & _arg)
  {
    this->table_num = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    order_msgs::action::RobotAction_Goal_<ContainerAllocator> *;
  using ConstRawPtr =
    const order_msgs::action::RobotAction_Goal_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_Goal_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_Goal_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_Goal_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_Goal_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_Goal_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_Goal_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_Goal_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_Goal_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__order_msgs__action__RobotAction_Goal
    std::shared_ptr<order_msgs::action::RobotAction_Goal_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__order_msgs__action__RobotAction_Goal
    std::shared_ptr<order_msgs::action::RobotAction_Goal_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotAction_Goal_ & other) const
  {
    if (this->table_num != other.table_num) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotAction_Goal_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotAction_Goal_

// alias to use template instance with default allocator
using RobotAction_Goal =
  order_msgs::action::RobotAction_Goal_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace order_msgs


#ifndef _WIN32
# define DEPRECATED__order_msgs__action__RobotAction_Result __attribute__((deprecated))
#else
# define DEPRECATED__order_msgs__action__RobotAction_Result __declspec(deprecated)
#endif

namespace order_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotAction_Result_
{
  using Type = RobotAction_Result_<ContainerAllocator>;

  explicit RobotAction_Result_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->result = false;
    }
  }

  explicit RobotAction_Result_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->result = false;
    }
  }

  // field types and members
  using _result_type =
    bool;
  _result_type result;

  // setters for named parameter idiom
  Type & set__result(
    const bool & _arg)
  {
    this->result = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    order_msgs::action::RobotAction_Result_<ContainerAllocator> *;
  using ConstRawPtr =
    const order_msgs::action::RobotAction_Result_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_Result_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_Result_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_Result_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_Result_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_Result_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_Result_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_Result_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_Result_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__order_msgs__action__RobotAction_Result
    std::shared_ptr<order_msgs::action::RobotAction_Result_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__order_msgs__action__RobotAction_Result
    std::shared_ptr<order_msgs::action::RobotAction_Result_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotAction_Result_ & other) const
  {
    if (this->result != other.result) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotAction_Result_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotAction_Result_

// alias to use template instance with default allocator
using RobotAction_Result =
  order_msgs::action::RobotAction_Result_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace order_msgs


#ifndef _WIN32
# define DEPRECATED__order_msgs__action__RobotAction_Feedback __attribute__((deprecated))
#else
# define DEPRECATED__order_msgs__action__RobotAction_Feedback __declspec(deprecated)
#endif

namespace order_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotAction_Feedback_
{
  using Type = RobotAction_Feedback_<ContainerAllocator>;

  explicit RobotAction_Feedback_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit RobotAction_Feedback_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _delivery_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _delivery_type delivery;

  // setters for named parameter idiom
  Type & set__delivery(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->delivery = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    order_msgs::action::RobotAction_Feedback_<ContainerAllocator> *;
  using ConstRawPtr =
    const order_msgs::action::RobotAction_Feedback_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_Feedback_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_Feedback_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_Feedback_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_Feedback_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_Feedback_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_Feedback_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_Feedback_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_Feedback_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__order_msgs__action__RobotAction_Feedback
    std::shared_ptr<order_msgs::action::RobotAction_Feedback_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__order_msgs__action__RobotAction_Feedback
    std::shared_ptr<order_msgs::action::RobotAction_Feedback_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotAction_Feedback_ & other) const
  {
    if (this->delivery != other.delivery) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotAction_Feedback_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotAction_Feedback_

// alias to use template instance with default allocator
using RobotAction_Feedback =
  order_msgs::action::RobotAction_Feedback_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace order_msgs


// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"
// Member 'goal'
#include "order_msgs/action/detail/robot_action__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__order_msgs__action__RobotAction_SendGoal_Request __attribute__((deprecated))
#else
# define DEPRECATED__order_msgs__action__RobotAction_SendGoal_Request __declspec(deprecated)
#endif

namespace order_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotAction_SendGoal_Request_
{
  using Type = RobotAction_SendGoal_Request_<ContainerAllocator>;

  explicit RobotAction_SendGoal_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    goal(_init)
  {
    (void)_init;
  }

  explicit RobotAction_SendGoal_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    goal(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _goal_type =
    order_msgs::action::RobotAction_Goal_<ContainerAllocator>;
  _goal_type goal;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__goal(
    const order_msgs::action::RobotAction_Goal_<ContainerAllocator> & _arg)
  {
    this->goal = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    order_msgs::action::RobotAction_SendGoal_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const order_msgs::action::RobotAction_SendGoal_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_SendGoal_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_SendGoal_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_SendGoal_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_SendGoal_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_SendGoal_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_SendGoal_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_SendGoal_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_SendGoal_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__order_msgs__action__RobotAction_SendGoal_Request
    std::shared_ptr<order_msgs::action::RobotAction_SendGoal_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__order_msgs__action__RobotAction_SendGoal_Request
    std::shared_ptr<order_msgs::action::RobotAction_SendGoal_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotAction_SendGoal_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->goal != other.goal) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotAction_SendGoal_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotAction_SendGoal_Request_

// alias to use template instance with default allocator
using RobotAction_SendGoal_Request =
  order_msgs::action::RobotAction_SendGoal_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace order_msgs


// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__order_msgs__action__RobotAction_SendGoal_Response __attribute__((deprecated))
#else
# define DEPRECATED__order_msgs__action__RobotAction_SendGoal_Response __declspec(deprecated)
#endif

namespace order_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotAction_SendGoal_Response_
{
  using Type = RobotAction_SendGoal_Response_<ContainerAllocator>;

  explicit RobotAction_SendGoal_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  explicit RobotAction_SendGoal_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  // field types and members
  using _accepted_type =
    bool;
  _accepted_type accepted;
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;

  // setters for named parameter idiom
  Type & set__accepted(
    const bool & _arg)
  {
    this->accepted = _arg;
    return *this;
  }
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    order_msgs::action::RobotAction_SendGoal_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const order_msgs::action::RobotAction_SendGoal_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_SendGoal_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_SendGoal_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_SendGoal_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_SendGoal_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_SendGoal_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_SendGoal_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_SendGoal_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_SendGoal_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__order_msgs__action__RobotAction_SendGoal_Response
    std::shared_ptr<order_msgs::action::RobotAction_SendGoal_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__order_msgs__action__RobotAction_SendGoal_Response
    std::shared_ptr<order_msgs::action::RobotAction_SendGoal_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotAction_SendGoal_Response_ & other) const
  {
    if (this->accepted != other.accepted) {
      return false;
    }
    if (this->stamp != other.stamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotAction_SendGoal_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotAction_SendGoal_Response_

// alias to use template instance with default allocator
using RobotAction_SendGoal_Response =
  order_msgs::action::RobotAction_SendGoal_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace order_msgs

namespace order_msgs
{

namespace action
{

struct RobotAction_SendGoal
{
  using Request = order_msgs::action::RobotAction_SendGoal_Request;
  using Response = order_msgs::action::RobotAction_SendGoal_Response;
};

}  // namespace action

}  // namespace order_msgs


// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__order_msgs__action__RobotAction_GetResult_Request __attribute__((deprecated))
#else
# define DEPRECATED__order_msgs__action__RobotAction_GetResult_Request __declspec(deprecated)
#endif

namespace order_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotAction_GetResult_Request_
{
  using Type = RobotAction_GetResult_Request_<ContainerAllocator>;

  explicit RobotAction_GetResult_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init)
  {
    (void)_init;
  }

  explicit RobotAction_GetResult_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    order_msgs::action::RobotAction_GetResult_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const order_msgs::action::RobotAction_GetResult_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_GetResult_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_GetResult_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_GetResult_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_GetResult_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_GetResult_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_GetResult_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_GetResult_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_GetResult_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__order_msgs__action__RobotAction_GetResult_Request
    std::shared_ptr<order_msgs::action::RobotAction_GetResult_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__order_msgs__action__RobotAction_GetResult_Request
    std::shared_ptr<order_msgs::action::RobotAction_GetResult_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotAction_GetResult_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotAction_GetResult_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotAction_GetResult_Request_

// alias to use template instance with default allocator
using RobotAction_GetResult_Request =
  order_msgs::action::RobotAction_GetResult_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace order_msgs


// Include directives for member types
// Member 'result'
// already included above
// #include "order_msgs/action/detail/robot_action__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__order_msgs__action__RobotAction_GetResult_Response __attribute__((deprecated))
#else
# define DEPRECATED__order_msgs__action__RobotAction_GetResult_Response __declspec(deprecated)
#endif

namespace order_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotAction_GetResult_Response_
{
  using Type = RobotAction_GetResult_Response_<ContainerAllocator>;

  explicit RobotAction_GetResult_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : result(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  explicit RobotAction_GetResult_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : result(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  // field types and members
  using _status_type =
    int8_t;
  _status_type status;
  using _result_type =
    order_msgs::action::RobotAction_Result_<ContainerAllocator>;
  _result_type result;

  // setters for named parameter idiom
  Type & set__status(
    const int8_t & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__result(
    const order_msgs::action::RobotAction_Result_<ContainerAllocator> & _arg)
  {
    this->result = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    order_msgs::action::RobotAction_GetResult_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const order_msgs::action::RobotAction_GetResult_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_GetResult_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_GetResult_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_GetResult_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_GetResult_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_GetResult_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_GetResult_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_GetResult_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_GetResult_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__order_msgs__action__RobotAction_GetResult_Response
    std::shared_ptr<order_msgs::action::RobotAction_GetResult_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__order_msgs__action__RobotAction_GetResult_Response
    std::shared_ptr<order_msgs::action::RobotAction_GetResult_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotAction_GetResult_Response_ & other) const
  {
    if (this->status != other.status) {
      return false;
    }
    if (this->result != other.result) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotAction_GetResult_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotAction_GetResult_Response_

// alias to use template instance with default allocator
using RobotAction_GetResult_Response =
  order_msgs::action::RobotAction_GetResult_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace order_msgs

namespace order_msgs
{

namespace action
{

struct RobotAction_GetResult
{
  using Request = order_msgs::action::RobotAction_GetResult_Request;
  using Response = order_msgs::action::RobotAction_GetResult_Response;
};

}  // namespace action

}  // namespace order_msgs


// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"
// Member 'feedback'
// already included above
// #include "order_msgs/action/detail/robot_action__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__order_msgs__action__RobotAction_FeedbackMessage __attribute__((deprecated))
#else
# define DEPRECATED__order_msgs__action__RobotAction_FeedbackMessage __declspec(deprecated)
#endif

namespace order_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct RobotAction_FeedbackMessage_
{
  using Type = RobotAction_FeedbackMessage_<ContainerAllocator>;

  explicit RobotAction_FeedbackMessage_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    feedback(_init)
  {
    (void)_init;
  }

  explicit RobotAction_FeedbackMessage_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    feedback(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _feedback_type =
    order_msgs::action::RobotAction_Feedback_<ContainerAllocator>;
  _feedback_type feedback;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__feedback(
    const order_msgs::action::RobotAction_Feedback_<ContainerAllocator> & _arg)
  {
    this->feedback = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    order_msgs::action::RobotAction_FeedbackMessage_<ContainerAllocator> *;
  using ConstRawPtr =
    const order_msgs::action::RobotAction_FeedbackMessage_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_FeedbackMessage_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<order_msgs::action::RobotAction_FeedbackMessage_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_FeedbackMessage_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_FeedbackMessage_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      order_msgs::action::RobotAction_FeedbackMessage_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<order_msgs::action::RobotAction_FeedbackMessage_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_FeedbackMessage_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<order_msgs::action::RobotAction_FeedbackMessage_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__order_msgs__action__RobotAction_FeedbackMessage
    std::shared_ptr<order_msgs::action::RobotAction_FeedbackMessage_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__order_msgs__action__RobotAction_FeedbackMessage
    std::shared_ptr<order_msgs::action::RobotAction_FeedbackMessage_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotAction_FeedbackMessage_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->feedback != other.feedback) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotAction_FeedbackMessage_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotAction_FeedbackMessage_

// alias to use template instance with default allocator
using RobotAction_FeedbackMessage =
  order_msgs::action::RobotAction_FeedbackMessage_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace order_msgs

#include "action_msgs/srv/cancel_goal.hpp"
#include "action_msgs/msg/goal_info.hpp"
#include "action_msgs/msg/goal_status_array.hpp"

namespace order_msgs
{

namespace action
{

struct RobotAction
{
  /// The goal message defined in the action definition.
  using Goal = order_msgs::action::RobotAction_Goal;
  /// The result message defined in the action definition.
  using Result = order_msgs::action::RobotAction_Result;
  /// The feedback message defined in the action definition.
  using Feedback = order_msgs::action::RobotAction_Feedback;

  struct Impl
  {
    /// The send_goal service using a wrapped version of the goal message as a request.
    using SendGoalService = order_msgs::action::RobotAction_SendGoal;
    /// The get_result service using a wrapped version of the result message as a response.
    using GetResultService = order_msgs::action::RobotAction_GetResult;
    /// The feedback message with generic fields which wraps the feedback message.
    using FeedbackMessage = order_msgs::action::RobotAction_FeedbackMessage;

    /// The generic service to cancel a goal.
    using CancelGoalService = action_msgs::srv::CancelGoal;
    /// The generic message for the status of a goal.
    using GoalStatusMessage = action_msgs::msg::GoalStatusArray;
  };
};

typedef struct RobotAction RobotAction;

}  // namespace action

}  // namespace order_msgs

#endif  // ORDER_MSGS__ACTION__DETAIL__ROBOT_ACTION__STRUCT_HPP_
