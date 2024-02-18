import tkinter as tk
from typing import Callable

import ttkbootstrap as tb
import ttkbootstrap.constants as c

from secondglass.timer import Status, Timer  # noqa: F401

from .frame import Frame
from .params import FONT_FAMILY, FONT_INIT_SIZE, PADDING, Params  # noqa: F401


class BtnFrame(Frame):
    def __init__(self, master: tk.Misc, params: Params) -> None:
        super().__init__(master, params)

    def create_all(self) -> None:
        def create_btn(text: str) -> tb.Button:
            return tb.Button(
                self,
                text=text,
                bootstyle=(c.LINK),
                cursor="hand2",
            )

        self.btn_start = create_btn("start")
        self.btn_pause = create_btn("pause")
        self.btn_resume = create_btn("resume")
        self.btn_restart = create_btn("restart")
        self.btn_stop = create_btn("stop")

        self.btns_order = [
            self.btn_start,
            self.btn_pause,
            self.btn_resume,
            self.btn_restart,
            self.btn_stop,
        ]

        self.btns_visibility = {
            Status.IDLE: (self.btn_start,),
            Status.TICKING: (self.btn_pause, self.btn_restart, self.btn_stop),
            Status.PAUSED: (self.btn_resume, self.btn_restart, self.btn_stop),
            Status.RANG: (self.btn_restart, self.btn_stop),
        }

    def pack_all(self) -> None:
        self.pack(side=c.TOP)
        self._update_btns_visibility()

    def _update_btns_visibility(self) -> None:
        visible_bnts = self.btns_visibility[self.params.timer.status]
        for btn in self.btns_order:
            btn.pack_forget()
        for btn in visible_bnts:
            btn.pack(side=c.LEFT)

    def set_callbacks(self) -> None:
        def bind_btn_handler(
            btn: tb.Button,
            change_status: Callable,
            text_var: tb.StringVar | None = None,
        ) -> None:

            def handler() -> None:
                if text_var:
                    change_status(text_var.get())
                else:
                    change_status()
                self._update_btns_visibility()

            btn.config(command=handler)

        bind_btn_handler(
            self.btn_start, self.params.timer.start, self.params.text
        )
        bind_btn_handler(self.btn_pause, self.params.timer.pause)
        bind_btn_handler(self.btn_resume, self.params.timer.resume)
        bind_btn_handler(self.btn_restart, self.params.timer.restart)
        bind_btn_handler(self.btn_stop, self.params.timer.stop)