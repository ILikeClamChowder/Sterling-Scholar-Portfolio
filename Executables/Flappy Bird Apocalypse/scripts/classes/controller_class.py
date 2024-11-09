import pygame as pg


class Controller():
    def __init__(self,count = 0):
        self.dead_zone = 0.03
        try:
            self.controller = pg.joystick.Joystick(count)
            self.controller.init()
            try:
                cont_id = self.controller.get_instance_id()
            except AttributeError:
                cont_id = self.controller.get_id()
        except IOError:
            print("no controller connected")
            quit()

    def get_dpad(self):
        dPad_dict = {}
        dpad = self.controller.get_hat(0)
        x = dpad[0]
        y = dpad[1] * -1
        dPad_dict = {"D_X": x, "D_Y": y}
        return dPad_dict

    def get_buttons(self):
        buttons_dict = {}
        a_button = self.controller.get_button(0)
        b_button = self.controller.get_button(1)
        x_button = self.controller.get_button(2)
        y_button = self.controller.get_button(3)
        lb_button = self.controller.get_button(4)
        rb_button = self.controller.get_button(5)
        back_button = self.controller.get_button(6)
        start_button = self.controller.get_button(7)
        lj_button = self.controller.get_button(8)
        rj_button = self.controller.get_button(9)
        xbox_button = self.controller.get_button(10)
        buttons_dict = {"A":a_button,"B":b_button,"X":x_button,"Y":y_button,
                        "LB":lb_button,"RB":rb_button,"START":start_button,"BACK":back_button,
                        "LJ":lj_button,"RJ":rj_button}


        return buttons_dict

    def get_axes(self):
        axis_dict = {}
        left_y = self.controller.get_axis(1)
        left_x = self.controller.get_axis(0)
        right_y = self.controller.get_axis(3)
        right_x = self.controller.get_axis(2)
        left_trig = self.controller.get_axis(4)
        right_trig = self.controller.get_axis(5)

        # clean up drift
        if left_x < self.dead_zone and left_x > -self.dead_zone:
            left_x = 0
        if left_y < self.dead_zone and left_y > -self.dead_zone:
            left_y = 0
        if right_x < self.dead_zone and right_x > -self.dead_zone:
            right_x = 0
        if right_y < self.dead_zone and right_y > -self.dead_zone:
            right_y = 0
        # set up key value pairs
        axis_dict = {"LJOY_Y": left_y, "LJOY_X": left_x, "RJOY_Y": right_y, "RJOY_X": right_x, "LTRIG": left_trig,
                     "RTRIG": right_trig}

        return axis_dict