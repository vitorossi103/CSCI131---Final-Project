from main.constants import SCREEN


# just to note, this is not mine. Found this online

def render_text(string, font, rect, text_color, justification=0):
    # Returns a surface containing the passed text string, reformatted
    # to fit within the given rect, word-wrapping as necessary. The text
    # will be anti-aliased.

    final_lines = []

    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.

    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    print("text is too long for passed in rect")
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_line)

    # Let's try to write the text out on the surface.
    accumulated_height = 0
    for line in final_lines:
        if accumulated_height + font.size(line)[1] >= rect.height:
            print("Once word-wrapped, the text string was too tall to fit in the rect.")
        if line != "":
            temp_surface = font.render(line, 1, text_color)
            if justification == 0:
                SCREEN.blit(temp_surface, (rect.x, rect.y + accumulated_height))
            elif justification == 1:
                SCREEN.blit(temp_surface, ((rect.width - temp_surface.get_width()) / 2, rect.y + accumulated_height))
            elif justification == 2:
                SCREEN.blit(temp_surface, (rect.width - temp_surface.get_width(), rect.y + accumulated_height))
            else:
                print("Invalid justification argument: " + str(justification))
        accumulated_height += font.size(line)[1]
