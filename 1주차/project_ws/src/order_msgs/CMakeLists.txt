cmake_minimum_required(VERSION 3.8)
project(order_msgs)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)

# 액션 및 서비스 정의 및 생성
rosidl_generate_interfaces(${PROJECT_NAME}
  "action/RobotAction.action"
  "srv/Order.srv"  # 서비스 파일 추가
  DEPENDENCIES builtin_interfaces std_msgs  # 필요한 의존성 추가
)

# 테스트 관련 설정
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
