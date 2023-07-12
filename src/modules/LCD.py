from drivers import RPi_I2C_driver


class LCD:
    driver = RPi_I2C_driver.lcd()

    def clear(self):
        self.driver.lcd_clear()

    def draw_string(self, value, row):
        self.driver.lcd_display_string(value, row)
