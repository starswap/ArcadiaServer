from ast import main
import math

def get_bearing(start_location, end_location):
    user_x = start_location[0]
    user_y = start_location[1]
    arcade_x = end_location[0]
    arcade_y = end_location[1]
    A = math.cos(arcade_x)*math.sin(user_y - arcade_y)
    B = math.cos(user_x)*math.sin(arcade_x) - math.sin(user_x)*math.cos(arcade_x)*math.cos(user_y -arcade_y)
    answer_radian = math.atan2(A , B)
    answer = math.degrees(answer_radian)
    answer = round(answer)
    return answer

    
if __name__ == '__main__':
    print(get_bearing((53.4808, 2.2426), (51.5072, 0.1276)))