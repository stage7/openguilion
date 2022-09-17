from . import openguilionCommon as _
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import pygame

# SURFACES
surfaceStateEmergency = pygame.Surface((_.w, _.h), pygame.SRCALPHA, 32)
surfaceStateEmergencyBG = pygame.Surface((_.w, _.h), pygame.SRCALPHA, 32)
surfaceStateEmergencyBGRects = pygame.Surface((_.w, _.h), pygame.SRCALPHA, 32)
surfaceStateEmergencyOver = pygame.Surface((_.w, _.h), pygame.SRCALPHA, 32)

# STATIC SCENE COMPOSITION
imgStateEm   = _.fontMatisse.render("非常事態", True, _.cRed).convert_alpha()
imgStateEm   = pygame.transform.smoothscale(imgStateEm, (round(imgStateEm.get_size()[0] * 2), round(imgStateEm.get_size()[1] * 1.5)))
imgEmergency = _.fontSinkin.render("EMERGENCY", True, _.cOrange).convert_alpha()
imgEmergency = pygame.transform.smoothscale(imgEmergency, (round(imgEmergency.get_size()[0] * 0.55), round(imgEmergency.get_size()[1] * 0.7)))

pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((43, 0), (113, 0), (0, 113), (0, 43)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((26, 159), (185, 0), (255, 0), (96, 159)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((168, 159), (327, 0), (397, 0), (238, 159)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((310, 159), (469, 0), (554, 0), (713, 159), (643, 159), (512, 28), (511, 28), (380, 159)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((452, 159), (511, 100), (512, 100), (571, 159)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((626, 0), (696, 0), (855, 159), (785, 159)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((768, 0), (838, 0), (997, 159), (927, 159)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((910, 0), (980, 0), (1023, 43), (1023, 113)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((0, 352), (40, 352), (0, 392)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((0, 464), (112, 352), (182, 352), (23, 511), (0, 511)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((254, 352), (324, 352), (165, 511), (95,511)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((396, 352), (466, 352), (307, 511), (237, 511)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((379, 511), (511, 379), (512, 379), (644, 511), (574, 511), (512, 449), (511, 449), (449, 511)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((557, 352), (627, 352), (786, 511), (716, 511)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((699, 352), (769, 352), (928, 511), (858, 511)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((841, 352), (911, 352), (1023, 464), (1023, 511), (1000, 511)))
pygame.draw.polygon(surfaceStateEmergencyBG, _.cRed, ((983, 352), (1023, 352), (1023, 392)))
pygame.draw.rect(surfaceStateEmergencyBG, _.cBlack, (512 - imgStateEm.get_size()[0] / 2 - 40, 35, imgStateEm.get_size()[0] + 80, imgStateEm.get_size()[1] + 20))
pygame.draw.rect(surfaceStateEmergencyBG, _.cBlack, (512 - imgStateEm.get_size()[0] / 2 - 40, _.h - 55 - imgStateEm.get_size()[1], imgStateEm.get_size()[0] + 80, imgStateEm.get_size()[1] + 20))

surfaceStateEmergencyBG.blit(imgStateEm, (512 - imgStateEm.get_size()[0] / 2, 45))
surfaceStateEmergencyBG.blit(imgStateEm, (512 - imgStateEm.get_size()[0] / 2, _.h - 45 - imgStateEm.get_size()[1]))


pygame.draw.rect(surfaceStateEmergencyBGRects, _.cOrange, (512 - imgStateEm.get_size()[0] / 2 - 35, 40, 20, imgStateEm.get_size()[1] + 10))
pygame.draw.rect(surfaceStateEmergencyBGRects, _.cOrange, (512 + imgStateEm.get_size()[0] / 2 + 15, 40, 20, imgStateEm.get_size()[1] + 10))
pygame.draw.rect(surfaceStateEmergencyBGRects, _.cOrange, (512 - imgStateEm.get_size()[0] / 2 - 35, _.h - 50 - imgStateEm.get_size()[1], 20, imgStateEm.get_size()[1] + 10))
pygame.draw.rect(surfaceStateEmergencyBGRects, _.cOrange, (512 + imgStateEm.get_size()[0] / 2 + 15, _.h - 50 - imgStateEm.get_size()[1], 20, imgStateEm.get_size()[1] + 10))

def stateEmergency(animTime):
	_.screen.fill(_.cBlack)
	surfaceStateEmergency.fill((0, 0, 0, 0))

	offsetEmergency = (-animTime * 500) % (imgEmergency.get_size()[0] + 350) - _.w
	while offsetEmergency < _.w:
		surfaceStateEmergency.blit(imgEmergency, (offsetEmergency, 180))
		offsetEmergency += (imgEmergency.get_size()[0] + 350)
	pygame.draw.rect(surfaceStateEmergency, _.cRed, (0, 321, _.w, 10))

	blinkTimeline = (animTime * 1000) % 500
	if blinkTimeline <= 250:
		surfaceStateEmergencyBG.set_alpha(255)
		surfaceStateEmergencyBGRects.set_alpha(255 - max(0, 255 - round((blinkTimeline - 200) / 250 * 255)))
	else:
		surfaceStateEmergencyBG.set_alpha(max(0, 255 - round((blinkTimeline - 200) / 250 * 255)))
		surfaceStateEmergencyBGRects.set_alpha(255)

	pil_string_image = pygame.image.tostring(surfaceStateEmergency, "RGBA", False)
	pil_image = Image.frombytes("RGBA", (_.w, _.h), pil_string_image)
	draw = ImageDraw.Draw(pil_image)
	blurred = pil_image.filter(ImageFilter.BoxBlur(6))
	blurred = pygame.image.fromstring(blurred.tobytes(), blurred.size, blurred.mode)
	_.screen.blit(blurred, (0, 0, 0, 0))
	surfaceStateEmergency.blit(surfaceStateEmergencyBG, (0, 0))
	surfaceStateEmergency.blit(surfaceStateEmergencyBGRects, (0, 0))
	surfaceStateEmergency.blit(surfaceStateEmergencyOver, (0, 0))

	_.screen.blit(surfaceStateEmergency, (0, 0))

	if animTime >= 5:
		return True
	return False