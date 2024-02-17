from dataclasses import dataclass, field

import ttkbootstrap as tb

from secondglass.timer import Timer

WINDOW_MIN_SIZE = (280, 120)
WINDOW_INIT_SIZE = (400, 180)
FONT_INIT_SIZE = 16
FONT_FAMILY = "Areal"
PADDING = 10
RENDER_DELAY_MS = 50  # 0.05 sec


@dataclass
class Params:
    timer: Timer = field(default_factory=Timer)
    progress: tb.DoubleVar = field(
        default_factory=lambda: tb.DoubleVar(value=0.6)
    )
    text: tb.StringVar = field(
        default_factory=lambda: tb.StringVar(value="text")
    )
    size: tb.DoubleVar = field(default_factory=lambda: tb.DoubleVar(value=1.0))

    def update_size(self, current_size: tuple[int, int]) -> None:
        old_size = self.size.get()
        new_size = current_size[0] / WINDOW_INIT_SIZE[0]
        if old_size != new_size:
            self.size.set(new_size)
