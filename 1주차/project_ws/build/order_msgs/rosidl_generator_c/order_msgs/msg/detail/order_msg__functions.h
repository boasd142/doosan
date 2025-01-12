// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from order_msgs:msg/OrderMsg.idl
// generated code does not contain a copyright notice

#ifndef ORDER_MSGS__MSG__DETAIL__ORDER_MSG__FUNCTIONS_H_
#define ORDER_MSGS__MSG__DETAIL__ORDER_MSG__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "order_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "order_msgs/msg/detail/order_msg__struct.h"

/// Initialize msg/OrderMsg message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * order_msgs__msg__OrderMsg
 * )) before or use
 * order_msgs__msg__OrderMsg__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_order_msgs
bool
order_msgs__msg__OrderMsg__init(order_msgs__msg__OrderMsg * msg);

/// Finalize msg/OrderMsg message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_order_msgs
void
order_msgs__msg__OrderMsg__fini(order_msgs__msg__OrderMsg * msg);

/// Create msg/OrderMsg message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * order_msgs__msg__OrderMsg__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_order_msgs
order_msgs__msg__OrderMsg *
order_msgs__msg__OrderMsg__create();

/// Destroy msg/OrderMsg message.
/**
 * It calls
 * order_msgs__msg__OrderMsg__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_order_msgs
void
order_msgs__msg__OrderMsg__destroy(order_msgs__msg__OrderMsg * msg);

/// Check for msg/OrderMsg message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_order_msgs
bool
order_msgs__msg__OrderMsg__are_equal(const order_msgs__msg__OrderMsg * lhs, const order_msgs__msg__OrderMsg * rhs);

/// Copy a msg/OrderMsg message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_order_msgs
bool
order_msgs__msg__OrderMsg__copy(
  const order_msgs__msg__OrderMsg * input,
  order_msgs__msg__OrderMsg * output);

/// Initialize array of msg/OrderMsg messages.
/**
 * It allocates the memory for the number of elements and calls
 * order_msgs__msg__OrderMsg__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_order_msgs
bool
order_msgs__msg__OrderMsg__Sequence__init(order_msgs__msg__OrderMsg__Sequence * array, size_t size);

/// Finalize array of msg/OrderMsg messages.
/**
 * It calls
 * order_msgs__msg__OrderMsg__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_order_msgs
void
order_msgs__msg__OrderMsg__Sequence__fini(order_msgs__msg__OrderMsg__Sequence * array);

/// Create array of msg/OrderMsg messages.
/**
 * It allocates the memory for the array and calls
 * order_msgs__msg__OrderMsg__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_order_msgs
order_msgs__msg__OrderMsg__Sequence *
order_msgs__msg__OrderMsg__Sequence__create(size_t size);

/// Destroy array of msg/OrderMsg messages.
/**
 * It calls
 * order_msgs__msg__OrderMsg__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_order_msgs
void
order_msgs__msg__OrderMsg__Sequence__destroy(order_msgs__msg__OrderMsg__Sequence * array);

/// Check for msg/OrderMsg message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_order_msgs
bool
order_msgs__msg__OrderMsg__Sequence__are_equal(const order_msgs__msg__OrderMsg__Sequence * lhs, const order_msgs__msg__OrderMsg__Sequence * rhs);

/// Copy an array of msg/OrderMsg messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_order_msgs
bool
order_msgs__msg__OrderMsg__Sequence__copy(
  const order_msgs__msg__OrderMsg__Sequence * input,
  order_msgs__msg__OrderMsg__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // ORDER_MSGS__MSG__DETAIL__ORDER_MSG__FUNCTIONS_H_
