#双色球
import base_lottery_class
import random
class two_color_ball_class(base_lottery_class.base_lotter_class):
    def __init__(self) -> None:
        super().__init__()
        self.def_red_ball_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
        self.def_blue_ball_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.red_number = 6
        self.blue_number = 1
        self.isTheSame = False
        self.lotter_type = 'two_color_ball'
        self.lottery_id = 'ssq'
        self.lottery_str = '双色球'
        self.lottery_img = 'http://ftp.zhuliyou.top/%E5%8F%8C%E8%89%B2%E7%90%83%E4%B8%AD%E5%A5%96%E8%A7%84%E5%88%99.png'
        self.open_base_url = self.open_base_url.format(self.lottery_id)
