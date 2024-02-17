import tkinter as tk
from dataclasses import dataclass, field
from tkinter.font import Font

import ttkbootstrap as tb
import ttkbootstrap.constants as c

from secondglass.timer import Timer

FONT_INIT_SIZE = 16
FONT_FAMILY = "Areal"
PADDING = 10


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


class MainFrame(tb.Frame):
    def __init__(self, master: tk.Misc | None = None) -> None:
        super().__init__(master)

        self.params = Params()

    def create_all(self) -> None:
        self.progressbar = tb.Progressbar(
            self,
            maximum=1.0,
            variable=self.params.progress,
            bootstyle=c.DEFAULT,
        )
        # the order IS important
        # InputFrame should go after Progressbar
        self.input_frame = InputFrame(self, self.params)
        self.input_frame.create_all()

    def pack_all(self) -> None:
        self.pack(
            expand=c.YES,
            fill=c.BOTH,
        )
        self.progressbar.place(
            anchor=c.CENTER,
            relheight=1.01,
            relwidth=1.01,
            relx=0.5,
            rely=0.5,
        )
        self.input_frame.pack_all()

    def animate_all(self) -> None:
        pass

    def animate_timer(self) -> None:
        pass

    # def update(self) -> None:
    #     self.timer.tick()
    #     self.update_progressbar()

    # def update_progressbar(self) -> None:
    #     self.progressbar_var.set(self.timer.progress)


class InputFrame(tb.Frame):
    def __init__(self, master: tk.Misc, params: Params) -> None:
        super().__init__(master)

        self.params = params

    def create_all(self) -> None:
        font_size = int(FONT_INIT_SIZE * self.params.size.get())
        font = Font(family=FONT_FAMILY, size=font_size)
        self.inner_container = tb.Frame(self)
        self.upper_placeholder = tb.Label(self.inner_container)
        self.entry = tb.Entry(
            self.inner_container,
            textvariable=self.params.text,
            justify=c.CENTER,
            font=font,
            cursor="xterm",
        )
        self.btn_container = tb.Frame(self.inner_container)

        def create_btn(text: str) -> tb.Button:
            return tb.Button(
                self.btn_container,
                text=text,
                bootstyle=(c.LINK),
                cursor="hand2",
            )

        self.btn_start = create_btn("start")
        self.btn_resume = create_btn("resume")
        self.btn_restart = create_btn("restart")

    def pack_all(self) -> None:
        padding = int(PADDING * self.params.size.get())
        self.pack(
            expand=c.YES,
            fill=c.BOTH,
            padx=padding,
            pady=padding,
        )
        self.inner_container.place(
            anchor=c.CENTER,
            relx=0.5,
            rely=0.5,
            relwidth=1.0,
        )
        self.upper_placeholder.pack(
            # padx=4,
        )  # margin
        self.entry.pack(
            fill=c.X,
            padx=4,
        )
        self.btn_container.pack(
            # expand=c.YES,
            # fill=c.BOTH,
            side=c.TOP,
        )
        self.btn_start.pack(side=c.LEFT)
        self.btn_resume.pack(side=c.LEFT)
        self.btn_restart.pack(side=c.LEFT)

    # def create_entry(self) -> tb.Entry:
    #     entry = tb.Entry(
    #         self.container,
    #         textvariable=self.entry_text,
    #         justify=c.CENTER,
    #         font=Font(size=16),
    #         # insertontime=0,
    #         cursor="xterm",
    #     )
    #     entry.pack(
    #         fill=c.X,
    #     )

    #     def focus_in(event: tk.Event) -> None:
    #         self.entry_text.set("111")
    #         entry.select_range(0, c.END)

    #     def focus_out(event: tk.Event) -> None:
    #         self.entry_text.set("222")

    #     entry.bind("<FocusIn>", focus_in)
    #     entry.bind("<FocusOut>", focus_out)

    #     return entry


if __name__ == "__main__":
    app = tb.Window(
        title="123",
        themename="simplex",
        minsize=(280, 120),
    )
    mf = MainFrame(app)
    mf.create_all()
    mf.pack_all()
    app.mainloop()