from . import openguilionCommon as _
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import pygame

# SURFACES
surfaceLost = pygame.Surface((_.w, _.h), pygame.SRCALPHA, 32)

# STATIC SCENE COMPOSITION
imgLost = _.fontHelvGiant.render("LOST", True, (0, 0, 0)).convert_alpha()
imgLost = pygame.transform.smoothscale(imgLost, (_.w - 100, _.h + 80))

def lost(animTime):
	_.screen.fill((0, 0, 0))
	surfaceLost.fill((0, 0, 0, 0))

	blinkTimeline = (animTime * 1000) % 750
	pygame.draw.rect(surfaceLost, (255, 0, 0), (20, 20, _.w - 40, _.h - 40))
	if blinkTimeline <= 375:
		imgLost.set_alpha(255)
	else:
		imgLost.set_alpha(max(0, 255 - round((blinkTimeline - 300) / 375 * 255)))
	surfaceLost.blit(imgLost, (40, -10))

	pil_string_image = pygame.image.tostring(surfaceLost, "RGBA", False)
	pil_image = Image.frombytes("RGBA", (_.w, _.h), pil_string_image)
	draw = ImageDraw.Draw(pil_image)
	blurred = pil_image.filter(ImageFilter.BoxBlur(3))
	py_text = pygame.image.fromstring(blurred.tobytes(), blurred.size, blurred.mode)
	_.screen.blit(py_text, (0, 0, 0, 0))
	_.screen.blit(surfaceLost, (0, 0))

	if animTime >= 5:
		return True
	return False