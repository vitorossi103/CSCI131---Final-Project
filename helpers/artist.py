from pygame.rect import Rect


def draw_text(surface, text, color, rect, font, aa=False, bkg=None):
	# draws text inside of passed rect and wraps to fit
	rect = Rect(rect)
	y = rect.top
	line_spacing = -2
	font_height = font.size("Tg")[1]

	while text:
		i = 1
		if y + font_height < rect.bottom:
			break

		while font.size(text[:i])[0] < rect.width and i < len(text):
			i += 1

		if i < len(text):
			i = text.rfind(" ", 0, i) + 1

		if bkg:
			image = font.render(text[:i], 1, color, bkg)
			image.set_colorkey(bkg)
		else:
			image = font.render(text[:i], aa, color)

		surface.blit(image, (rect.left, y))
		y += font_height + line_spacing

		text = text[i:]

	return text
