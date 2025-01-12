// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from order_msgs:srv/Order.idl
// generated code does not contain a copyright notice
#include "order_msgs/srv/detail/order__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `table_num`
// Member `item`
#include "rosidl_runtime_c/string_functions.h"

bool
order_msgs__srv__Order_Request__init(order_msgs__srv__Order_Request * msg)
{
  if (!msg) {
    return false;
  }
  // table_num
  if (!rosidl_runtime_c__String__init(&msg->table_num)) {
    order_msgs__srv__Order_Request__fini(msg);
    return false;
  }
  // item
  if (!rosidl_runtime_c__String__init(&msg->item)) {
    order_msgs__srv__Order_Request__fini(msg);
    return false;
  }
  // quantity
  // price
  return true;
}

void
order_msgs__srv__Order_Request__fini(order_msgs__srv__Order_Request * msg)
{
  if (!msg) {
    return;
  }
  // table_num
  rosidl_runtime_c__String__fini(&msg->table_num);
  // item
  rosidl_runtime_c__String__fini(&msg->item);
  // quantity
  // price
}

bool
order_msgs__srv__Order_Request__are_equal(const order_msgs__srv__Order_Request * lhs, const order_msgs__srv__Order_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // table_num
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->table_num), &(rhs->table_num)))
  {
    return false;
  }
  // item
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->item), &(rhs->item)))
  {
    return false;
  }
  // quantity
  if (lhs->quantity != rhs->quantity) {
    return false;
  }
  // price
  if (lhs->price != rhs->price) {
    return false;
  }
  return true;
}

bool
order_msgs__srv__Order_Request__copy(
  const order_msgs__srv__Order_Request * input,
  order_msgs__srv__Order_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // table_num
  if (!rosidl_runtime_c__String__copy(
      &(input->table_num), &(output->table_num)))
  {
    return false;
  }
  // item
  if (!rosidl_runtime_c__String__copy(
      &(input->item), &(output->item)))
  {
    return false;
  }
  // quantity
  output->quantity = input->quantity;
  // price
  output->price = input->price;
  return true;
}

order_msgs__srv__Order_Request *
order_msgs__srv__Order_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  order_msgs__srv__Order_Request * msg = (order_msgs__srv__Order_Request *)allocator.allocate(sizeof(order_msgs__srv__Order_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(order_msgs__srv__Order_Request));
  bool success = order_msgs__srv__Order_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
order_msgs__srv__Order_Request__destroy(order_msgs__srv__Order_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    order_msgs__srv__Order_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
order_msgs__srv__Order_Request__Sequence__init(order_msgs__srv__Order_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  order_msgs__srv__Order_Request * data = NULL;

  if (size) {
    data = (order_msgs__srv__Order_Request *)allocator.zero_allocate(size, sizeof(order_msgs__srv__Order_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = order_msgs__srv__Order_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        order_msgs__srv__Order_Request__fini(&data[i - 1]);
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
order_msgs__srv__Order_Request__Sequence__fini(order_msgs__srv__Order_Request__Sequence * array)
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
      order_msgs__srv__Order_Request__fini(&array->data[i]);
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

order_msgs__srv__Order_Request__Sequence *
order_msgs__srv__Order_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  order_msgs__srv__Order_Request__Sequence * array = (order_msgs__srv__Order_Request__Sequence *)allocator.allocate(sizeof(order_msgs__srv__Order_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = order_msgs__srv__Order_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
order_msgs__srv__Order_Request__Sequence__destroy(order_msgs__srv__Order_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    order_msgs__srv__Order_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
order_msgs__srv__Order_Request__Sequence__are_equal(const order_msgs__srv__Order_Request__Sequence * lhs, const order_msgs__srv__Order_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!order_msgs__srv__Order_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
order_msgs__srv__Order_Request__Sequence__copy(
  const order_msgs__srv__Order_Request__Sequence * input,
  order_msgs__srv__Order_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(order_msgs__srv__Order_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    order_msgs__srv__Order_Request * data =
      (order_msgs__srv__Order_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!order_msgs__srv__Order_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          order_msgs__srv__Order_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!order_msgs__srv__Order_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `message`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

bool
order_msgs__srv__Order_Response__init(order_msgs__srv__Order_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  // message
  if (!rosidl_runtime_c__String__init(&msg->message)) {
    order_msgs__srv__Order_Response__fini(msg);
    return false;
  }
  return true;
}

void
order_msgs__srv__Order_Response__fini(order_msgs__srv__Order_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
  // message
  rosidl_runtime_c__String__fini(&msg->message);
}

bool
order_msgs__srv__Order_Response__are_equal(const order_msgs__srv__Order_Response * lhs, const order_msgs__srv__Order_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  // message
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->message), &(rhs->message)))
  {
    return false;
  }
  return true;
}

bool
order_msgs__srv__Order_Response__copy(
  const order_msgs__srv__Order_Response * input,
  order_msgs__srv__Order_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  // message
  if (!rosidl_runtime_c__String__copy(
      &(input->message), &(output->message)))
  {
    return false;
  }
  return true;
}

order_msgs__srv__Order_Response *
order_msgs__srv__Order_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  order_msgs__srv__Order_Response * msg = (order_msgs__srv__Order_Response *)allocator.allocate(sizeof(order_msgs__srv__Order_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(order_msgs__srv__Order_Response));
  bool success = order_msgs__srv__Order_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
order_msgs__srv__Order_Response__destroy(order_msgs__srv__Order_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    order_msgs__srv__Order_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
order_msgs__srv__Order_Response__Sequence__init(order_msgs__srv__Order_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  order_msgs__srv__Order_Response * data = NULL;

  if (size) {
    data = (order_msgs__srv__Order_Response *)allocator.zero_allocate(size, sizeof(order_msgs__srv__Order_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = order_msgs__srv__Order_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        order_msgs__srv__Order_Response__fini(&data[i - 1]);
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
order_msgs__srv__Order_Response__Sequence__fini(order_msgs__srv__Order_Response__Sequence * array)
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
      order_msgs__srv__Order_Response__fini(&array->data[i]);
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

order_msgs__srv__Order_Response__Sequence *
order_msgs__srv__Order_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  order_msgs__srv__Order_Response__Sequence * array = (order_msgs__srv__Order_Response__Sequence *)allocator.allocate(sizeof(order_msgs__srv__Order_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = order_msgs__srv__Order_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
order_msgs__srv__Order_Response__Sequence__destroy(order_msgs__srv__Order_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    order_msgs__srv__Order_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
order_msgs__srv__Order_Response__Sequence__are_equal(const order_msgs__srv__Order_Response__Sequence * lhs, const order_msgs__srv__Order_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!order_msgs__srv__Order_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
order_msgs__srv__Order_Response__Sequence__copy(
  const order_msgs__srv__Order_Response__Sequence * input,
  order_msgs__srv__Order_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(order_msgs__srv__Order_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    order_msgs__srv__Order_Response * data =
      (order_msgs__srv__Order_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!order_msgs__srv__Order_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          order_msgs__srv__Order_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!order_msgs__srv__Order_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
