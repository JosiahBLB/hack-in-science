from dataclasses import dataclass


@dataclass
class Frame:
    top: str = "-"
    left: str = "|"
    bottom: str = "-"
    right: str = "|"
    top_left: str = "+"
    top_right: str = "+"
    bottom_left: str = "+"
    bottom_right: str = "+"


fancy_frame = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
invisible_frame = Frame(" ", " ", " ", " ", " ", " ", " ", " ")


def frame_text(text: str, frame: Frame) -> str:
    text = text.split('\n')
    widths = list(map(lambda x: len(x), text))
    max_width = max(widths)
    top = "".join([frame.top_left, frame.top*max_width, frame.top_right])
    bottom = "".join([frame.bottom_left, frame.bottom*max_width, frame.bottom_right])
    for index, line in enumerate(text):
        text[index] = "".join([frame.left, line.ljust(max_width, " "), frame.right])
    text.insert(0, top)
    text.append(bottom)
    text = '\n'.join(text)
    return(print(text))
    
            
christmas_tree = '      *\n     ***\n    *****\n   *******\n    *****\n   *******\n  *********\n ***********\n*************\n     |||\n     |||'
custom_message = 'Happy new year!\nFrom Josiah Brough'

frame_text(christmas_tree, fancy_frame)
frame_text(custom_message, fancy_frame)

frame_text("hello Rae!", fancy_frame)