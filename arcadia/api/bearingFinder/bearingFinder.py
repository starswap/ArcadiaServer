
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
    if 22.5> answer > 0:
        letter_answer = 'N'
    elif 67.5> answer > 22.5:
        letter_answer = 'NE'
    elif 112.5> answer > 67.5:
        letter_answer = 'E'
    elif 157.5> answer > 112.5:
        letter_answer = 'SE'
    elif 202.5> answer > 157.5:
        letter_answer = 'S'
    elif 247.5> answer > 202.5:
        letter_answer = 'SW'
    elif 292.5> answer > 247.5:
        letter_answer = 'W'
    elif 337.5> answer > 292.5:
        letter_answer = 'NW'
    elif answer > 337.5:
        letter_answer = 'N'
    return letter_answer

    
if __name__ == '__main__':
    print(get_bearing((53.4808, 2.2426), (51.5072, 0.1276)))