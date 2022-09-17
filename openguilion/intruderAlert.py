from . import openguilionCommon as _
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import pygame
import math
import random

# SURFACES
surfaceIntruderAlert = pygame.Surface((_.w, _.h), pygame.SRCALPHA, 32)
surfaceIntruderAlertBG = pygame.Surface((_.w, _.h), pygame.SRCALPHA, 32)
surfaceIntruderAlertOver = pygame.Surface((_.w, _.h), pygame.SRCALPHA, 32)

# STATIC SCENE COMPOSITION
imgUnidentInt = _.fontHelv.render("UNIDENTIFIED INTRUDER", True, (228, 114, 0)).convert_alpha()
imgUnidentInt = pygame.transform.smoothscale(imgUnidentInt, (round(imgUnidentInt.get_size()[0] * 0.6), round(imgUnidentInt.get_size()[1] * 1)))
imgUnidentInt = pygame.transform.rotate(imgUnidentInt, 270)
imgSubcomp    = _.fontHelv.render("SUBCOMPUTER #1", True, (228, 114, 0)).convert_alpha()
imgSubcomp    = pygame.transform.smoothscale(imgSubcomp, (round(imgSubcomp.get_size()[0] * 0.6), round(imgSubcomp.get_size()[1] * 0.65)))
imgIntAlert   = _.fontHelv.render("INTRUDER ALERT", True, (228, 114, 0)).convert_alpha()
imgIntAlert   = pygame.transform.smoothscale(imgIntAlert, (round(imgIntAlert.get_size()[0] * 0.85), round(imgIntAlert.get_size()[1] * 1.6)))
imgPartition  = _.fontHelv.render("PARTITION", True, (228, 114, 0)).convert_alpha()
imgPartition  = pygame.transform.smoothscale(imgPartition, (round(imgPartition.get_size()[0] * 0.3), round(imgPartition.get_size()[1] * 0.5)))
imgInt1       = _.fontHelv.render("#1", True, (228, 114, 0)).convert_alpha()
imgInt1       = pygame.transform.smoothscale(imgInt1, (round(imgInt1.get_size()[0] * 0.5), round(imgInt1.get_size()[1] * 0.5)))
imgInt2       = _.fontHelv.render("#2", True, (228, 114, 0)).convert_alpha()
imgInt2       = pygame.transform.smoothscale(imgInt2, (round(imgInt2.get_size()[0] * 0.5), round(imgInt2.get_size()[1] * 0.5)))
imgInt3       = _.fontHelv.render("#3", True, (228, 114, 0)).convert_alpha()
imgInt3       = pygame.transform.smoothscale(imgInt3, (round(imgInt3.get_size()[0] * 0.5), round(imgInt3.get_size()[1] * 0.5)))
imgInt4       = _.fontHelv.render("#4", True, (228, 114, 0)).convert_alpha()
imgInt4       = pygame.transform.smoothscale(imgInt4, (round(imgInt4.get_size()[0] * 0.5), round(imgInt4.get_size()[1] * 0.5)))
imgInt5       = _.fontHelv.render("#5", True, (228, 114, 0)).convert_alpha()
imgInt5       = pygame.transform.smoothscale(imgInt5, (round(imgInt5.get_size()[0] * 0.5), round(imgInt5.get_size()[1] * 0.5)))
pygame.draw.rect(surfaceIntruderAlertBG, (186, 1, 13), (0, 0, 235, 512))
tempColor = pygame.Color((0, 0, 0))
for i in range(235):
	tempColor.hsva = (172.74 + 127.26 * (i / 235), 100, 100, 50)
	pygame.draw.line(surfaceIntruderAlertBG, tempColor, (235 + i, 0), (235 + i, 511))
for i in range(554):
	tempColor.hsva = (300 - 300 * (i / 554), 100, 100, 50)
	pygame.draw.line(surfaceIntruderAlertBG, tempColor, (470 + i, 0), (470 + i, 511))
pygame.draw.rect(surfaceIntruderAlertBG, (0, 0, 0), (235 + 128, 0, 30, 512))
pygame.draw.rect(surfaceIntruderAlertBG, (0, 0, 0), (235 + 316, 0, 14, 512))
pygame.draw.rect(surfaceIntruderAlertBG, (0, 0, 0), (235 + 406, 0, 20, 512))
pygame.draw.rect(surfaceIntruderAlertBG, (0, 0, 0), (235 + 473, 0, 20, 512))
pygame.draw.rect(surfaceIntruderAlertBG, (0, 0, 0), (235 + 631, 0, 20, 512))
surfaceIntruderAlertBG.blit(imgUnidentInt, (142, 86))
surfaceIntruderAlertBG.blit(imgPartition, (265, 22))
surfaceIntruderAlertBG.blit(imgPartition, (435, 22))
surfaceIntruderAlertBG.blit(imgPartition, (600, 22))
surfaceIntruderAlertBG.blit(imgPartition, (762, 22))
surfaceIntruderAlertBG.blit(imgPartition, (913, 22))
surfaceIntruderAlertBG.blit(imgInt1, (292, 50))
surfaceIntruderAlertBG.blit(imgInt2, (461, 50))
surfaceIntruderAlertBG.blit(imgInt3, (626, 50))
surfaceIntruderAlertBG.blit(imgInt4, (787, 50))
surfaceIntruderAlertBG.blit(imgInt5, (939, 50))
surfaceIntruderAlertBG.blit(imgSubcomp, (496, 344))
surfaceIntruderAlertBG.blit(imgIntAlert, (499, 384))
pygame.draw.rect(surfaceIntruderAlertBG, (228, 114, 0), (144, 74, 61, 396), 3, border_radius = 6)
pygame.draw.rect(surfaceIntruderAlertBG, (228, 114, 0), (261, 20, 86, 60), 2, border_radius = 4)
pygame.draw.rect(surfaceIntruderAlertBG, (228, 114, 0), (431, 20, 86, 60), 2, border_radius = 4)
pygame.draw.rect(surfaceIntruderAlertBG, (228, 114, 0), (596, 20, 86, 60), 2, border_radius = 4)
pygame.draw.rect(surfaceIntruderAlertBG, (228, 114, 0), (758, 20, 86, 60), 2, border_radius = 4)
pygame.draw.rect(surfaceIntruderAlertBG, (228, 114, 0), (909, 20, 86, 60), 2, border_radius = 4)
pygame.draw.rect(surfaceIntruderAlertBG, (228, 114, 0), (489, 379, 391, 99), 5, border_radius = 8)

def intruderAlert(animTime):
	_.screen.fill((0, 0, 0))
	surfaceIntruderAlert.fill((0, 0, 0, 0))
	surfaceIntruderAlertOver.fill((0, 0, 0, 0))

	surfaceIntruderAlert.blit(surfaceIntruderAlertBG, (0, 0))
	factor = animTime / 6
	if factor < 0.5:
		barsMultiplier = 16 * factor * factor * factor * factor * factor
	else:
		barsMultiplier = 1 - math.pow(-2 * factor + 2, 5) / 2
	
	offset = random.randint(-30, 30)
	pygame.draw.rect(surfaceIntruderAlertOver, (255, 64, 64), (230, 256 - (120 + offset + 150 * barsMultiplier) / 2, 133, 120 + offset + 150 * barsMultiplier))
	pygame.draw.rect(surfaceIntruderAlertOver, (255, 64, 64), (362, 256 - (60 + offset + 150 * barsMultiplier) / 2, 22, 60 + offset + 150 * barsMultiplier))
	pygame.draw.rect(surfaceIntruderAlertOver, (255, 64, 64), (384, 256 - (72 + offset + 150 * barsMultiplier) / 2, 9, 72 + offset + 150 * barsMultiplier))
	pygame.draw.rect(surfaceIntruderAlertOver, (255, 64, 64), (393, 256 - (-18 + offset + 150 * barsMultiplier) / 2, 121, -18 + offset + 150 * barsMultiplier))
	pygame.draw.rect(surfaceIntruderAlertOver, (255, 64, 64), (514, 256 - (18 + offset + 150 * barsMultiplier) / 2, 30, 18 + offset + 150 * barsMultiplier))
	pygame.draw.rect(surfaceIntruderAlertOver, (255, 64, 64), (544, 256 - (30 + offset + 150 * barsMultiplier) / 2, 7, 30 + offset + 150 * barsMultiplier))
	pygame.draw.rect(surfaceIntruderAlertOver, (255, 64, 64), (551, 256 - (-48 + offset + 150 * barsMultiplier) / 2, 87, -48 + offset + 150 * barsMultiplier))
	pygame.draw.rect(surfaceIntruderAlertOver, (255, 64, 64), (638, 256 - (-30 + offset + 150 * barsMultiplier) / 2, 6, -30 + offset + 150 * barsMultiplier))
	pygame.draw.rect(surfaceIntruderAlertOver, (255, 64, 64), (644, 256 - (-12 + offset + 150 * barsMultiplier) / 2, 17, -12 + offset + 150 * barsMultiplier))
	pygame.draw.rect(surfaceIntruderAlertOver, (255, 64, 64), (661, 256 - (-90 + offset + 150 * barsMultiplier) / 2, 51, -90 + offset + 150 * barsMultiplier))
	pygame.draw.rect(surfaceIntruderAlertOver, (255, 64, 64), (712, 256 - (-60 + offset + 150 * barsMultiplier) / 2, 15, -60 + offset + 150 * barsMultiplier))
	pygame.draw.rect(surfaceIntruderAlertOver, (255, 64, 64), (727, 256 - (-90 + offset + 150 * barsMultiplier) / 2, 39, -90 + offset + 150 * barsMultiplier))
	pygame.draw.rect(surfaceIntruderAlertOver, (255, 64, 64), (766, 256 - (-96 + offset + 150 * barsMultiplier) / 2, 102, -96 + offset + 150 * barsMultiplier))
	pygame.draw.rect(surfaceIntruderAlertOver, (255, 64, 64), (868, 256 - (-78 + offset + 150 * barsMultiplier) / 2, 17, -78 + offset + 150 * barsMultiplier))
	pygame.draw.rect(surfaceIntruderAlertOver, (255, 64, 64), (885, 256 - (-114 + offset + 150 * barsMultiplier) / 2, 50, -114 + offset + 150 * barsMultiplier))
	surfaceIntruderAlertOver.set_alpha(64)
	pil_string_image = pygame.image.tostring(surfaceIntruderAlertOver, "RGBA", False)
	pil_image = Image.frombytes("RGBA", (_.w, _.h), pil_string_image)
	draw = ImageDraw.Draw(pil_image)
	blurred = pil_image.filter(ImageFilter.BoxBlur(10))
	blurred = pygame.image.fromstring(blurred.tobytes(), blurred.size, blurred.mode)
	blurred.set_alpha(192)
	surfaceIntruderAlert.blit(blurred, (0, 0, 0, 0))
	surfaceIntruderAlert.blit(surfaceIntruderAlertOver, (0, 0))

	_.screen.blit(surfaceIntruderAlert, (0, 0))

	if animTime >= 6:
		return True
	return False