class Fan:
    """Represents an electric fan with encapsulated attributes."""

    SLOW   = 1
    MEDIUM = 2
    FAST   = 3

    def __init__(self, speed=None, radius=5.0, color="blue", on=False):
        self.__speed  = speed if speed is not None else Fan.SLOW
        self.__radius = radius
        self.__color  = color
        self.__on     = on

    # ── Getters ──────────────────────────────────────────────
    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def get_on(self):                          
        return self.__on

    # ── Setters ──────────────────────────────────────────────
    def set_speed(self, speed):
        if speed not in (Fan.SLOW, Fan.MEDIUM, Fan.FAST):
            raise ValueError(f"Speed must be SLOW ({Fan.SLOW}), MEDIUM ({Fan.MEDIUM}), or FAST ({Fan.FAST}).")
        self.__speed = speed

    def set_radius(self, radius):
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.__radius = float(radius)

    def set_color(self, color):
        if not isinstance(color, str) or not color.strip():
            raise ValueError("Color must be a non-empty string.")
        self.__color = color

    def set_on(self, on):
        if not isinstance(on, bool):
            raise TypeError("'on' must be a boolean (True or False).")
        self.__on = on

    # ── Behaviours ───────────────────────────────────────────
    def toggle(self):
        self.__on = not self.__on
        return f"Fan turned {'on' if self.__on else 'off'}."

    def __str__(self):
        speed_name = {Fan.SLOW: "SLOW", Fan.MEDIUM: "MEDIUM", Fan.FAST: "FAST"}.get(self.__speed, "UNKNOWN")
        status = "on" if self.__on else "off"
        return (f"Fan [speed={speed_name}, radius={self.__radius}, "
                f"color={self.__color}, on={status}]")