// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from order_msgs:action/RobotAction.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__ACTION__DETAIL__ROBOT_ACTION__STRUCT_H_
#define ORDER_MSGS__ACTION__DETAIL__ROBOT_ACTION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/RobotAction in the package order_msgs.
typedef struct order_msgs__action__RobotAction_Goal
{
  int64_t table_num;
} order_msgs__action__RobotAction_Goal;

// Struct for a sequence of order_msgs__action__RobotAction_Goal.
typedef struct order_msgs__action__RobotAction_Goal__Sequence
{
  order_msgs__action__RobotAction_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} order_msgs__action__RobotAction_Goal__Sequence;


// Constants defined in the message

/// Struct defined in action/RobotAction in the package order_msgs.
typedef struct order_msgs__action__RobotAction_Result
{
  bool result;
} order_msgs__action__RobotAction_Result;

// Struct for a sequence of order_msgs__action__RobotAction_Result.
typedef struct order_msgs__action__RobotAction_Result__Sequence
{
  order_msgs__action__RobotAction_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} order_msgs__action__RobotAction_Result__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'delivery'
#include "rosidl_runtime_c/string.h"

/// Struct defined in action/RobotAction in the package order_msgs.
typedef struct order_msgs__action__RobotAction_Feedback
{
  rosidl_runtime_c__String__Sequence delivery;
} order_msgs__action__RobotAction_Feedback;

// Struct for a sequence of order_msgs__action__RobotAction_Feedback.
typedef struct order_msgs__action__RobotAction_Feedback__Sequence
{
  order_msgs__action__RobotAction_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} order_msgs__action__RobotAction_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "order_msgs/action/detail/robot_action__struct.h"

/// Struct defined in action/RobotAction in the package order_msgs.
typedef struct order_msgs__action__RobotAction_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  order_msgs__action__RobotAction_Goal goal;
} order_msgs__action__RobotAction_SendGoal_Request;

// Struct for a sequence of order_msgs__action__RobotAction_SendGoal_Request.
typedef struct order_msgs__action__RobotAction_SendGoal_Request__Sequence
{
  order_msgs__action__RobotAction_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} order_msgs__action__RobotAction_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/RobotAction in the package order_msgs.
typedef struct order_msgs__action__RobotAction_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} order_msgs__action__RobotAction_SendGoal_Response;

// Struct for a sequence of order_msgs__action__RobotAction_SendGoal_Response.
typedef struct order_msgs__action__RobotAction_SendGoal_Response__Sequence
{
  order_msgs__action__RobotAction_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} order_msgs__action__RobotAction_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/RobotAction in the package order_msgs.
typedef struct order_msgs__action__RobotAction_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} order_msgs__action__RobotAction_GetResult_Request;

// Struct for a sequence of order_msgs__action__RobotAction_GetResult_Request.
typedef struct order_msgs__action__RobotAction_GetResult_Request__Sequence
{
  order_msgs__action__RobotAction_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} order_msgs__action__RobotAction_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "order_msgs/action/detail/robot_action__struct.h"

/// Struct defined in action/RobotAction in the package order_msgs.
typedef struct order_msgs__action__RobotAction_GetResult_Response
{
  int8_t status;
  order_msgs__action__RobotAction_Result result;
} order_msgs__action__RobotAction_GetResult_Response;

// Struct for a sequence of order_msgs__action__RobotAction_GetResult_Response.
typedef struct order_msgs__action__RobotAction_GetResult_Response__Sequence
{
  order_msgs__action__RobotAction_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} order_msgs__action__RobotAction_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "order_msgs/action/detail/robot_action__struct.h"

/// Struct defined in action/RobotAction in the package order_msgs.
typedef struct order_msgs__action__RobotAction_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  order_msgs__action__RobotAction_Feedback feedback;
} order_msgs__action__RobotAction_FeedbackMessage;

// Struct for a sequence of order_msgs__action__RobotAction_FeedbackMessage.
typedef struct order_msgs__action__RobotAction_FeedbackMessage__Sequence
{
  order_msgs__action__RobotAction_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} order_msgs__action__RobotAction_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ORDER_MSGS__ACTION__DETAIL__ROBOT_ACTION__STRUCT_H_
