import unittest
import helper
from random import choice

env_data = helper.fetch_maze()
position_empty = 0
position_robot = 1
position_barrier = 2
position_destination = 3

#################################################################
print("\n任务1: 正确获取模拟环境的长和宽与模拟环境中第3行第6列元素")
rows = len(env_data)
columns = len(env_data[0])
row_3_col_6 = env_data[2][5]
print("迷宫共有", rows, "行", columns, "列，第三行第六列的元素是", row_3_col_6)

#################################################################
print("\n任务2: 正确计算模拟环境中，第一行和第三列的障碍物个数。")
number_of_barriers_row1 = len([point for point in env_data[0] if point == position_barrier])
number_of_barriers_col3 = 0
for row_index in range(len(env_data)):
    number_of_barriers_col3 += 1 if env_data[row_index][2] == position_barrier else 0

#################################################################
# 任务3
loc_map = {}
for row_index, row in enumerate(env_data):
    for col_index, point in enumerate(row):
        if point == position_robot:
            loc_map["start"] = row_index, col_index
        elif point == position_destination:
            loc_map["destination"] = row_index, col_index


#################################################################
# 任务4： is_move_valid_special
def is_move_valid_special(loc, act):
    """
    Judge wether the robot can take action act
    at location loc.

    Keyword arguments:
    loc -- tuple, robots current location
    act -- string, robots meant action
    """
    return is_move_valid(env_data, loc, act)


#################################################################
# 任务5： is_move_valid
def is_move_valid(env, loc, act):
    """
    Judge wether the robot can take action act
    at location loc.

    Keyword arguments:
    env -- list, the environment data
    loc -- tuple, robots current location
    act -- string, robots meant action
    """
    rows_ = len(env)
    columns_ = len(env[0])
    if act == 'u':
        return loc[0] > 0 and env[loc[0] - 1][loc[1]] != position_barrier
    if act == 'd':
        return loc[0] < rows_ - 1 and env[loc[0] + 1][loc[1]] != position_barrier
    if act == 'l':
        return loc[1] > 0 and env[loc[0]][loc[1] - 1] != position_barrier
    if act == 'r':
        return loc[1] < columns_ - 1 and env[loc[0]][loc[1] + 1] != position_barrier


#################################################################
# 任务7： valid_actions
def valid_actions(env, loc):
    """
    Find all possible actions the robot can take
    at location loc.

    Keyword arguments:
    env -- list, the environment data
    loc -- tuple, robots current location
    """
    return [action for action in ['u', 'd', "l", "r"] if is_move_valid(env, loc, action)]


#################################################################
# 任务8：编写一个名为 move_robot 的函数，它有两个输入，分别为机器人当前所在的位置 loc 和即将执行的动作 act。接着会返回机器人执行动作之后的新位置 new_loc。
def move_robot(loc, act):
    """
    Move robot.

    Keyword arguments:
    loc -- tuple, robots current location
    act -- string, robots meant action
    """
    if valid_actions(env_data, loc).__contains__(act):
        if act == 'u':
            return loc[0] - 1, loc[1]
        elif act == 'd':
            return loc[0] + 1, loc[1]
        elif act == 'l':
            return loc[0], loc[1] - 1
        elif act == 'r':
            return loc[0], loc[1] + 1


class RobotControllerTestCase(unittest.TestCase):
    """Test for Robot Controller project"""

    def test_cal_barriers(self):
        self.assertEqual(number_of_barriers_row1, 7)
        self.assertEqual(number_of_barriers_col3, 3)

    def test_cal_loc_map(self):
        self.assertEqual(loc_map["start"], (0, 8))
        self.assertEqual(loc_map["destination"], (0, 0))

    def test_is_move_valid(self):
        self.assertEqual(is_move_valid(env_data, (0, 0), 'u'), False)
        self.assertEqual(is_move_valid(env_data, (0, 0), 'l'), False)

        self.assertEqual(is_move_valid(env_data, (4, 0), 'd'), False)
        self.assertEqual(is_move_valid(env_data, (0, 8), 'r'), False)

        self.assertEqual(is_move_valid(env_data, (0, 0), 'r'), False)
        self.assertEqual(is_move_valid(env_data, (1, 0), 'd'), False)

        self.assertEqual(is_move_valid(env_data, (1, 7), 'd'), True)
        self.assertEqual(is_move_valid(env_data, (3, 5), 'r'), True)

        self.assertEqual(is_move_valid(env_data, (1, 0), 'u'), True)

    def test_is_move_valid_special(self):
        self.assertEqual(is_move_valid_special((0, 0), 'u'), False)
        self.assertEqual(is_move_valid_special((0, 0), 'l'), False)

        self.assertEqual(is_move_valid_special((4, 0), 'd'), False)
        self.assertEqual(is_move_valid_special((0, 8), 'r'), False)

        self.assertEqual(is_move_valid_special((0, 0), 'r'), False)
        self.assertEqual(is_move_valid_special((1, 0), 'd'), False)

        self.assertEqual(is_move_valid_special((1, 7), 'd'), True)
        self.assertEqual(is_move_valid_special((3, 5), 'r'), True)

        self.assertEqual(is_move_valid_special((1, 0), 'u'), True)

    def test_valid_actions(self):
        result_list = valid_actions(env_data, (0, 8))
        self.assertEqual(set(result_list), set(['d']))

        result_list = valid_actions(env_data, (1, 0))
        self.assertTrue(set(result_list), set(['u', 'r']))

    def test_move_robot(self):
        self.assertEqual(move_robot((1, 0), 'u'), (0, 0))
        self.assertEqual(move_robot((0, 8), 'd'), (1, 8))
        self.assertEqual(move_robot((3, 3), 'l'), (3, 2))
        self.assertEqual(move_robot((1, 0), 'r'), (1, 1))

    @staticmethod
    def test_find_destination():
        find_destination()


def find_destination():
    # 利用上方定义的 valid_actions 函数，找出当前位置下，机器人可行的动作；
    # 利用 random 库中的 choice 函数，从机器人可行的动作中，随机挑选出一个动作；
    # 接着根据这个动作，利用上方定义的 move_robot 函数，来移动机器人，并更新机器人的位置；
    # 当机器人走到终点时，输出“在第n个回合找到宝藏！”。
    start_loc = loc_map['start']
    env_data_ = env_data
    for count_acts in range(300):
        new_loc = random_choose_actions(env_data_, start_loc)
        if new_loc == loc_map['destination']:
            print("在第{}个回合找到宝藏！".format(count_acts + 1))
            return

        env_data_[new_loc[0]][new_loc[1]] = position_robot
        env_data_[start_loc[0]][start_loc[1]] = position_empty
        start_loc = new_loc
        helper.fetch_maze()


def random_choose_actions(env_, robot_current_loc):
    """
    Random choose the action

    Keyword arguments:
    env -- list, the environment data
    robot_current_loc -- tuple, robots current location
    Return:
        The new location
    """
    random_act = choice(valid_actions(env_, robot_current_loc))
    new_loc = move_robot(robot_current_loc, random_act)
    return new_loc


if __name__ == '__main__':
    unittest.main()
