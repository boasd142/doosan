// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from type:srv/StartTime.idl
// generated code does not contain a copyright notice
#include "type/srv/detail/start_time__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `job_list`
#include "rosidl_runtime_c/string_functions.h"

bool
type__srv__StartTime_Request__init(type__srv__StartTime_Request * msg)
{
  if (!msg) {
    return false;
  }
  // start_value
  // job_list
  if (!rosidl_runtime_c__String__init(&msg->job_list)) {
    type__srv__StartTime_Request__fini(msg);
    return false;
  }
  // constatus
  // datastatus
  return true;
}

void
type__srv__StartTime_Request__fini(type__srv__StartTime_Request * msg)
{
  if (!msg) {
    return;
  }
  // start_value
  // job_list
  rosidl_runtime_c__String__fini(&msg->job_list);
  // constatus
  // datastatus
}

bool
type__srv__StartTime_Request__are_equal(const type__srv__StartTime_Request * lhs, const type__srv__StartTime_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // start_value
  if (lhs->start_value != rhs->start_value) {
    return false;
  }
  // job_list
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->job_list), &(rhs->job_list)))
  {
    return false;
  }
  // constatus
  if (lhs->constatus != rhs->constatus) {
    return false;
  }
  // datastatus
  if (lhs->datastatus != rhs->datastatus) {
    return false;
  }
  return true;
}

bool
type__srv__StartTime_Request__copy(
  const type__srv__StartTime_Request * input,
  type__srv__StartTime_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // start_value
  output->start_value = input->start_value;
  // job_list
  if (!rosidl_runtime_c__String__copy(
      &(input->job_list), &(output->job_list)))
  {
    return false;
  }
  // constatus
  output->constatus = input->constatus;
  // datastatus
  output->datastatus = input->datastatus;
  return true;
}

type__srv__StartTime_Request *
type__srv__StartTime_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  type__srv__StartTime_Request * msg = (type__srv__StartTime_Request *)allocator.allocate(sizeof(type__srv__StartTime_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(type__srv__StartTime_Request));
  bool success = type__srv__StartTime_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
type__srv__StartTime_Request__destroy(type__srv__StartTime_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    type__srv__StartTime_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
type__srv__StartTime_Request__Sequence__init(type__srv__StartTime_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  type__srv__StartTime_Request * data = NULL;

  if (size) {
    data = (type__srv__StartTime_Request *)allocator.zero_allocate(size, sizeof(type__srv__StartTime_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = type__srv__StartTime_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        type__srv__StartTime_Request__fini(&data[i - 1]);
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
type__srv__StartTime_Request__Sequence__fini(type__srv__StartTime_Request__Sequence * array)
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
      type__srv__StartTime_Request__fini(&array->data[i]);
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

type__srv__StartTime_Request__Sequence *
type__srv__StartTime_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  type__srv__StartTime_Request__Sequence * array = (type__srv__StartTime_Request__Sequence *)allocator.allocate(sizeof(type__srv__StartTime_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = type__srv__StartTime_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
type__srv__StartTime_Request__Sequence__destroy(type__srv__StartTime_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    type__srv__StartTime_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
type__srv__StartTime_Request__Sequence__are_equal(const type__srv__StartTime_Request__Sequence * lhs, const type__srv__StartTime_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!type__srv__StartTime_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
type__srv__StartTime_Request__Sequence__copy(
  const type__srv__StartTime_Request__Sequence * input,
  type__srv__StartTime_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(type__srv__StartTime_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    type__srv__StartTime_Request * data =
      (type__srv__StartTime_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!type__srv__StartTime_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          type__srv__StartTime_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!type__srv__StartTime_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `status`
// Member `conv`
// Member `data`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

bool
type__srv__StartTime_Response__init(type__srv__StartTime_Response * msg)
{
  if (!msg) {
    return false;
  }
  // result_value
  // status
  if (!rosidl_runtime_c__String__init(&msg->status)) {
    type__srv__StartTime_Response__fini(msg);
    return false;
  }
  // conv
  if (!rosidl_runtime_c__String__init(&msg->conv)) {
    type__srv__StartTime_Response__fini(msg);
    return false;
  }
  // data
  if (!rosidl_runtime_c__String__init(&msg->data)) {
    type__srv__StartTime_Response__fini(msg);
    return false;
  }
  return true;
}

void
type__srv__StartTime_Response__fini(type__srv__StartTime_Response * msg)
{
  if (!msg) {
    return;
  }
  // result_value
  // status
  rosidl_runtime_c__String__fini(&msg->status);
  // conv
  rosidl_runtime_c__String__fini(&msg->conv);
  // data
  rosidl_runtime_c__String__fini(&msg->data);
}

bool
type__srv__StartTime_Response__are_equal(const type__srv__StartTime_Response * lhs, const type__srv__StartTime_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // result_value
  if (lhs->result_value != rhs->result_value) {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->status), &(rhs->status)))
  {
    return false;
  }
  // conv
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->conv), &(rhs->conv)))
  {
    return false;
  }
  // data
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->data), &(rhs->data)))
  {
    return false;
  }
  return true;
}

bool
type__srv__StartTime_Response__copy(
  const type__srv__StartTime_Response * input,
  type__srv__StartTime_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // result_value
  output->result_value = input->result_value;
  // status
  if (!rosidl_runtime_c__String__copy(
      &(input->status), &(output->status)))
  {
    return false;
  }
  // conv
  if (!rosidl_runtime_c__String__copy(
      &(input->conv), &(output->conv)))
  {
    return false;
  }
  // data
  if (!rosidl_runtime_c__String__copy(
      &(input->data), &(output->data)))
  {
    return false;
  }
  return true;
}

type__srv__StartTime_Response *
type__srv__StartTime_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  type__srv__StartTime_Response * msg = (type__srv__StartTime_Response *)allocator.allocate(sizeof(type__srv__StartTime_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(type__srv__StartTime_Response));
  bool success = type__srv__StartTime_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
type__srv__StartTime_Response__destroy(type__srv__StartTime_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    type__srv__StartTime_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
type__srv__StartTime_Response__Sequence__init(type__srv__StartTime_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  type__srv__StartTime_Response * data = NULL;

  if (size) {
    data = (type__srv__StartTime_Response *)allocator.zero_allocate(size, sizeof(type__srv__StartTime_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = type__srv__StartTime_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        type__srv__StartTime_Response__fini(&data[i - 1]);
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
type__srv__StartTime_Response__Sequence__fini(type__srv__StartTime_Response__Sequence * array)
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
      type__srv__StartTime_Response__fini(&array->data[i]);
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

type__srv__StartTime_Response__Sequence *
type__srv__StartTime_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  type__srv__StartTime_Response__Sequence * array = (type__srv__StartTime_Response__Sequence *)allocator.allocate(sizeof(type__srv__StartTime_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = type__srv__StartTime_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
type__srv__StartTime_Response__Sequence__destroy(type__srv__StartTime_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    type__srv__StartTime_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
type__srv__StartTime_Response__Sequence__are_equal(const type__srv__StartTime_Response__Sequence * lhs, const type__srv__StartTime_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!type__srv__StartTime_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
type__srv__StartTime_Response__Sequence__copy(
  const type__srv__StartTime_Response__Sequence * input,
  type__srv__StartTime_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(type__srv__StartTime_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    type__srv__StartTime_Response * data =
      (type__srv__StartTime_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!type__srv__StartTime_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          type__srv__StartTime_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!type__srv__StartTime_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
