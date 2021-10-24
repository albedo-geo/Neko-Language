from tkinter import font
import PySimpleGUI as sg
from neko import *

sg.theme('SystemDefault')

sg.set_options(font=('Microsoft Yahei UI', 10))
outbox = sg.Output()
layout = [
    [sg.Text('输入'), sg.Input()],
    [sg.Text('输出'), outbox],
    [
        sg.Checkbox('解码', tooltip='编码还是解码？'),
        sg.Button('转换'),
        sg.Button('关闭'),
    ],
]

# Create the Window
window = sg.Window('喵星文转换器', layout)
while True:
    event, values = window.read()
    if event == '转换':
        input = values[0].strip()
        if values[1]:
            text = neko_decode(input)
        else:
            text = neko_encode(input)
        outbox.update(value=text)
    elif event == sg.WIN_CLOSED or '关闭':
        break

window.close()
