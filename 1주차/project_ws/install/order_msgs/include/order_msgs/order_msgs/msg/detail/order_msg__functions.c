// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from order_msgs:msg/OrderMsg.idl
// generated code does not contain a copyright notice
#include "order_msgs/msg/detail/order_msg__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
order_msgs__msg__OrderMsg__init(order_msgs__msg__OrderMsg * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
order_msgs__msg__OrderMsg__fini(order_msgs__msg__OrderMsg * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
order_msgs__msg__OrderMsg__are_equal(const order_msgs__msg__OrderMsg * lhs, const order_msgs__msg__OrderMsg * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // structure_needs_at_least_one_member
  if (lhs->structure_needs_at_least_one_member != rhs->structure_needs_at_least_one_member) {
    return false;
  }
  return true;
}

bool
order_msgs__msg__OrderMsg__copy(
  const order_msgs__msg__OrderMsg * input,
  order_msgs__msg__OrderMsg * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

order_msgs__msg__OrderMsg *
order_msgs__msg__OrderMsg__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  order_msgs__msg__OrderMsg * msg = (order_msgs__msg__OrderMsg *)allocator.allocate(sizeof(order_msgs__msg__OrderMsg), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(order_msgs__msg__OrderMsg));
  bool success = order_msgs__msg__OrderMsg__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
order_msgs__msg__OrderMsg__destroy(order_msgs__msg__OrderMsg * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    order_msgs__msg__OrderMsg__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
order_msgs__msg__OrderMsg__Sequence__init(order_msgs__msg__OrderMsg__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  order_msgs__msg__OrderMsg * data = NULL;

  if (size) {
    data = (order_msgs__msg__OrderMsg *)allocator.zero_allocate(size, sizeof(order_msgs__msg__OrderMsg), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = order_msgs__msg__OrderMsg__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        order_msgs__msg__OrderMsg__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
order_msgs__msg__OrderMsg__Sequence__fini(order_msgs__msg__OrderMsg__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      order_msgs__msg__OrderMsg__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

order_msgs__msg__OrderMsg__Sequence *
order_msgs__msg__OrderMsg__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  order_msgs__msg__OrderMsg__Sequence * array = (order_msgs__msg__OrderMsg__Sequence *)allocator.allocate(sizeof(order_msgs__msg__OrderMsg__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = order_msgs__msg__OrderMsg__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
order_msgs__msg__OrderMsg__Sequence__destroy(order_msgs__msg__OrderMsg__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    order_msgs__msg__OrderMsg__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
order_msgs__msg__OrderMsg__Sequence__are_equal(const order_msgs__msg__OrderMsg__Sequence * lhs, const order_msgs__msg__OrderMsg__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!order_msgs__msg__OrderMsg__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
order_msgs__msg__OrderMsg__Sequence__copy(
  const order_msgs__msg__OrderMsg__Sequence * input,
  order_msgs__msg__OrderMsg__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(order_msgs__msg__OrderMsg);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    order_msgs__msg__OrderMsg * data =
      (order_msgs__msg__OrderMsg *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!order_msgs__msg__OrderMsg__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          order_msgs__msg__OrderMsg__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!order_msgs__msg__OrderMsg__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
