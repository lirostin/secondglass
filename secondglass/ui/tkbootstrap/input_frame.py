import tkinter as tk
from tkinter.font import Font

import ttkbootstrap as tb
import ttkbootstrap.constants as c

from .btn_frame import BtnFrame
from .frame import Frame
from .params import FONT_FAMILY, FONT_INIT_SIZE, PADDING, Params


class InputFrame(Frame):
    def __init__(self, master: tk.Misc, params: Params) -> None:
        super().__init__(master, params)

    def create_all(self) -> None:
        self.font = Font(family=FONT_FAMILY, size=FONT_INIT_SIZE)
        self.inner_container = tb.Frame(self)
        self.upper_placeholder = tb.Label(
            self.inner_container, bootstyle=c.SECONDARY
        )
        self.entry = tb.Entry(
            self.inner_container,
            textvariable=self.params.text_input,
            justify=c.CENTER,
            font=self.font,
            cursor="xterm",
        )
        self.btn_container = BtnFrame(self.inner_container, self.params)
        self.btn_container.create_all()
        self.upper_placeholder.configure(font=self.btn_container.font)

    def pack_all(self) -> None:
        self.pack(
            expand=c.YES,
            fill=c.BOTH,
            padx=PADDING,
            pady=PADDING,
        )
        self.inner_container.place(
            anchor=c.CENTER,
            relx=0.5,
            rely=0.5,
            relwidth=1.0,
        )
        self.upper_placeholder.pack(
            # pady=(0, PADDING),
        )
        self.entry.pack(
            fill=c.X,
            padx=4,
        )
        self.btn_container.pack_all()

    def update_all(self) -> None:
        self.btn_container.update_all()

    def set_callbacks(self) -> None:
        def on_size_change(name: str, ind: str | int, method: str) -> None:
            new_size = self.params.size.get()
            new_padding = int(PADDING * new_size)
            self.pack_configure(
                padx=new_padding,
                pady=new_padding,
            )

            new_font_size = int(FONT_INIT_SIZE * new_size)
            self.font.config(size=new_font_size)
            self.params.text_input.set(self.params.text_input.get())
            # - fixes the font alignment issue

        self.params.size.trace_add("write", on_size_change)
        self.btn_container.set_callbacks()

        def entry_focus_in(event: tk.Event) -> None:
            # print("entry_focus_in")
            self.entry.configure(textvariable=self.params.text_input)
            pass

        def entry_focus_out(event: tk.Event) -> None:
            # print("entry_focus_out")
            self.entry.configure(textvariable=self.params.text_output)
            pass

        self.entry.bind("<FocusIn>", entry_focus_in)
        self.entry.bind("<FocusOut>", entry_focus_out)

        def return_pressed(event: tk.Event) -> None:
            for btn in [
                self.btn_container.btn_start,
                self.btn_container.btn_restart,
            ]:
                if btn.winfo_ismapped():
                    btn.invoke()

        self.entry.bind("<Return>", return_pressed)
