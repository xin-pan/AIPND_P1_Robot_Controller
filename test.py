import unittest
import helper

env_data = helper.fetch_maze()

print("\n任务1: 正确获取模拟环境的长和宽与模拟环境中第3行第6列元素")
rows = len(env_data)
columns = len(env_data[0])
row_3_col_6 = env_data[2][5]
print("迷宫共有", rows, "行", columns, "列，第三行第六列的元素是", row_3_col_6)

print("\n任务2: 正确计算模拟环境中，第一行和第三列的障碍物个数。")
number_of_barriers_row1 = len([point for point in env_data[0] if point == 2])
number_of_barriers_col3 = 0
for row_index in range(len(env_data)):
    number_of_barriers_col3 += 1 if env_data[row_index][2] == 2 else 0


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
        self.assertEqual(valid_actions(env_data, (0, 8)), ['d'])

        result_list = valid_actions(env_data, (1, 0))
        self.assertTrue(['u', 'r'] == result_list or ['r', 'u'] == result_list)

    def test_move_robot(self):
        self.assertEqual(move_robot((1, 0), 'u'), (0, 0))
        self.assertEqual(move_robot((0, 8), 'd'), (1, 8))
        self.assertEqual(move_robot((3, 3), 'l'), (3, 2))
        self.assertEqual(move_robot((1, 0), 'r'), (1, 1))


if __name__ == '__main__':
    unittest.main()
