def grip():
    set_digital_output(1,ON)
    set_digital_output(2,OFF)
    wait(1)

def ungrip():
    set_digital_output(1,OFF)
    set_digital_output(2,ON)
    wait(1)

pos1 = posx(598.72, 143.77, 73.68, 7.67, -180, 11.1)
pos2 = posx(495.33, 143.77, 73.68, 46.89, -180, 50.32)
pos3 = posx(497.89, 246.45, 73.68, 27.44, 180, 30.88)
pos4 = posx(599.4, 246.44, 73.68, 11.35, -180, 14.79)

goal1 = posx(599.52, -102.17, 73.68, 31.27, -179, 31.07)
goal2 = posx(497.52, -101.56, 73.68, 28.59, -178.81, 28.31)
goal3 = posx(601.79, -2.11, 73.68, 24.86, -178.42, 24.64)
goal4 = posx(499.44, -1.08, 73.6, 22.74, -178.32, 22.41)
home = posj(0,0,90,0,90,0)

direction = 1
row = 3
column = 3
stack = 1
thickness = 0
point_offset = [0, 0, 0] # Offset for calculated pose

# 높이가 약 55mm인 기둥이므로 좀더 높은 z값으로 올라가도록 설정
z_up = [0,0,60,0,0,0]
# 물건의 높이가 얼마인지 확인하기위해 내려갈때 사용할 z_down 값
z_down = [0,0,-40,0,0,0]

bases = []
goals = []

#이미 무언가를 집고 있는 상태라면 초기에 여는 과정 생략
if get_digital_input(1) == OFF:
    ungrip()

#물건을 집은 위치의 z좌표를 저장하기 위한 변수 생성
grip_z = 0

#물건을 집고 옮기는 과정을 거쳤는지 판단하기 위해 bool함수를 하나 추가함
move = False

# Total count
if direction < 2: # Normal Pallet
    total_count = row * column * stack
else: # Rhombus Pallet
    total_count = (row * column - int(row/2)) * stack
# Calculate Pallet Pose (Resulted in base coordinate)

for pallet_index in range(0, total_count): 
    Pallet_Pose = get_pattern_point(pos1, pos2, pos3, pos4, pallet_index, direction, row, column, stack, thickness, point_offset) 
    bases.append(Pallet_Pose)
    

for pallet_index in range(0, total_count): 
    Pallet_Pose = get_pattern_point(goal1, goal2, goal3, goal4, pallet_index, direction, row, column, stack, thickness, point_offset) 
    goals.append(Pallet_Pose)
    
    
#base에서 goal
if way == 0:
    for i in range(total_count):
        # timer를 추가하였음 후에 사용처 기술
        timer = 0
        #저장된 count로 i를 인위적으로 변경. 후에 count가 값을 넘어게가 되면 이 루프를 끝내는 break문을 삽입해놓음
        i = count
        #물건을 잡고 있지 않은 상태일때
        if get_digital_input(1) == OFF:
        # 우선 물건을 옮기지 않았으므로 move = false로 설정
            move = False
            #지정된 base좌표로 이동함 이때 base의 z좌표들은 가장 높은 기둥의 살짝 위로 모두 설정됨
            movel(bases[i],t=3)
            
            #그립한 상태로 비동기로 내려감
            grip()
            amovel( trans(bases[i],z_down,DR_BASE,DR_BASE),v=10,acc=100)
            
            # 이전에 추가한 타이머 변수를 이용해 계속 추가 이 값이 다될때 까지 인지되지 않으면 루프가 끝나게됨
            while timer <= 1000 :
                force = check_force_condition(DR_AXIS_Z,min = 8, ref = DR_TOOL)
                timer+=1
            #만약 힘이 감지된다면 동작을 멈추고 goal좌표로 이동하는과정        
                if force == True:
                    now = get_current_posx(ref = DR_BASE)[0]
                    stop(DR_QSTOP)
                    movel(trans(now,[0,0,10,0,0,0],DR_BASE,DR_BASE),t=3)
                    ungrip()
                    movel(trans(now,[0,0,-15,0,0,0],DR_BASE,DR_BASE),t=3)
                    grip()
                    grip_z = get_current_posx(ref=DR_BASE)[0][2]+5
                    
                    movel(trans(bases[i],z_up,DR_BASE,DR_BASE),t=3)
                    movel(trans(goals[i],z_up,DR_BASE,DR_BASE),t=5)
                    
                   
                    goals[i][2] = grip_z
                    movel(goals[i],t=3)
                    ungrip()
                    move = True
                    break
                    
                    
        else:             
        #이전의 위치가 따로 저장된게 없으므로 base위로 갔다가 다시 goal로 가는 행위 반복(수정 가능할지도)
             movel(trans(bases[i],z_up,DR_BASE,DR_BASE),t=3)
             movel(trans(goals[i],z_up,DR_BASE,DR_BASE),t=5)                
             amovel(trans(goals[i],[0,0,-100,0,0,0],DR_BASE,DR_BASE),v=5,acc=80)
             
             while True:
                 force = check_force_condition(DR_AXIS_Z,min = 5, ref = DR_TOOL)
                 if force == True:
                    ungrip()
                    move = True # 잡고 동작을 완료
                    break
            
        #잡을게 없을때
        if move == False:
            ungrip()
            movel( trans(bases[i],z_up,DR_BASE,DR_BASE),t=3)
    
        #모든 작업이 끝나고 카운트가 충분히 쌓이면 다음 루프(제작필요)        
        # move가 정상동작했다면 True로 변경되어 위의 조건문은 스킵 카운트를 증가시킨다.
        count+=1

        if count >=9:
            way= 1
            count = 0
            break

goals = []
bases = []           
            
for pallet_index in range(0, total_count): 
    Pallet_Pose = get_pattern_point(pos1, pos2, pos3, pos4, pallet_index, direction, row, column, stack, thickness, point_offset) 
    bases.append(Pallet_Pose)
    

for pallet_index in range(0, total_count): 
    Pallet_Pose = get_pattern_point(goal1, goal2, goal3, goal4, pallet_index, direction, row, column, stack, thickness, point_offset) 
    goals.append(Pallet_Pose)
    
'''
    trans로 값이 변경되게 되면 리스트 자체에 영향을 끼치게 된다.
'''    
if way == 1:
    for i in range(total_count-1, -1, -1):  # i를 8에서 0까지 반복
        timer = 0
        i = total_count-count-1
        
        # 물건을 잡고 있지 않은 상태일때
        if get_digital_input(1) == OFF:
            # 우선 물건을 옮기지 않았으므로 move = false로 설정
            move = False
            # goal 위치로 이동
            movel(goals[i], t=3)
            
            # 그립한 상태로 비동기로 내려감
            grip()
            amovel(trans(goals[i], z_down, DR_BASE, DR_BASE), v=10, acc=100)
    
            # 이전에 추가한 타이머 변수를 이용해 계속 추가 이 값이 다될때 까지 인지되지 않으면 루프를 끝나게됨
            while timer <= 1000:
                force = check_force_condition(DR_AXIS_Z, min=8, ref=DR_TOOL)
                timer += 1
            # 만약 힘이 감지된다면 동작을 멈추고 base좌표로 이동하는 과정
                if force == True:
                    now = get_current_posx(ref=DR_BASE)[0]
                    stop(DR_QSTOP)
                    movel(trans(now, [0, 0, 10, 0, 0, 0], DR_BASE, DR_BASE), t=3)
                    ungrip()
                    movel(trans(now, [0, 0, -15, 0, 0, 0], DR_BASE, DR_BASE), t=3)
                    grip()
                    grip_z = get_current_posx(ref=DR_BASE)[0][2] + 5
    
                    # base로 이동
                    movel(trans(goals[i], z_up, DR_BASE, DR_BASE), t=3)
                    movel(trans(bases[i], z_up, DR_BASE, DR_BASE), t=5)
    
                    bases[i][2] = grip_z
                    movel(bases[i], t=3)
                    ungrip()
                    move = True
                    break
    
        else:
            # 이전의 위치가 따로 저장된게 없으므로 goal위로 갔다가 다시 base로 가는 행위 반복
            movel(trans(goals[i], z_up, DR_BASE, DR_BASE), t=3)
            movel(trans(bases[i], z_up, DR_BASE, DR_BASE), t=5)
            amovel(trans(bases[i], [0, 0, -100, 0, 0, 0], DR_BASE, DR_BASE), v=5, acc=80)
    
            while True:
                force = check_force_condition(DR_AXIS_Z, min=5, ref=DR_TOOL)
                if force == True:
                    stop(DR_QSTOP)
                    ungrip()
                    move = True  
                    break
    
        # 잡을게 없을때
        if move == False:
            ungrip()
            movel(trans(goals[i], z_up, DR_BASE, DR_BASE), t=3)
            
        count += 1
        if count >= 9:
            break

# 모든 동작이 끝난다면 카운트 초기화 및 홈 포지션
if move == True:
    movel([0,0,-50,0,0,0],t=3,ref = DR_TOOL)
    move_home(DR_HOME_TARGET_USER)

way = 0
count = 0