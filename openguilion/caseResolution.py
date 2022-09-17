from . import openguilionCommon as _
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import pygame
import random

# SURFACES
surfaceCaseResolution = pygame.Surface((_.w, _.h), pygame.SRCALPHA, 32)
surfaceCaseResolutionBG = pygame.Surface((_.w, _.h), pygame.SRCALPHA, 32)
surfaceCaseMelchior = pygame.Surface((_.w, 566), pygame.SRCALPHA, 32)
surfaceCaseCasper = pygame.Surface((_.w, 566), pygame.SRCALPHA, 32)
surfaceCaseMelchiorText = pygame.Surface((180, 180), pygame.SRCALPHA, 32)
surfaceCaseCasperText = pygame.Surface((180, 180), pygame.SRCALPHA, 32)

# STATIC SCENE COMPOSITION
imgCaseJap   = _.fontMatisse.render("提訴", True, (228, 114, 0)).convert_alpha()
imgCaseJap   = pygame.transform.smoothscale(imgCaseJap, (round(imgCaseJap.get_size()[0] * 2), round(imgCaseJap.get_size()[1] * 1.5)))
imgResoJap   = _.fontMatisse.render("決議", True, (228, 114, 0)).convert_alpha()
imgResoJap   = pygame.transform.smoothscale(imgResoJap, (round(imgResoJap.get_size()[0] * 2), round(imgResoJap.get_size()[1] * 1.5)))
imgDelibJap  = _.fontMatisse.render("審議中", True, (212, 19, 13)).convert_alpha()
imgDelibJap  = pygame.transform.smoothscale(imgDelibJap, (round(imgDelibJap.get_size()[0] * 0.85), round(imgDelibJap.get_size()[1] * 1)))
imgMagi      = _.fontMatisse.render("MAGI", True, (228, 114, 0)).convert_alpha()
imgMagi      = pygame.transform.smoothscale(imgMagi, (round(imgMagi.get_size()[0] * 0.65), round(imgMagi.get_size()[1] * 0.55)))
imgMelchior  = _.fontHelv.render("MELCHIOR", True, (0, 0, 0)).convert_alpha()
imgMelchior  = pygame.transform.smoothscale(imgMelchior, (round(imgMelchior.get_size()[0] * 0.5), round(imgMelchior.get_size()[1] * 0.5)))
imgCasper    = _.fontHelv.render("CASPER", True, (0, 0, 0)).convert_alpha()
imgCasper    = pygame.transform.smoothscale(imgCasper, (round(imgCasper.get_size()[0] * 0.5), round(imgCasper.get_size()[1] * 0.5)))
imgBalthasar = _.fontHelv.render("BALTHASAR", True, (0, 0, 0)).convert_alpha()
imgBalthasar = pygame.transform.smoothscale(imgBalthasar, (round(imgBalthasar.get_size()[0] * 0.5), round(imgBalthasar.get_size()[1] * 0.5)))
imgCase1     = _.fontHelv.render("1", True, (0, 0, 0)).convert_alpha()
imgCase1     = pygame.transform.smoothscale(imgCase1, (round(imgCase1.get_size()[0] * 2), round(imgCase1.get_size()[1] * 1.4)))
imgCase2     = _.fontHelv.render("2", True, (0, 0, 0)).convert_alpha()
imgCase2     = pygame.transform.smoothscale(imgCase2, (round(imgCase2.get_size()[0] * 2), round(imgCase2.get_size()[1] * 1.4)))
imgCase3     = _.fontHelv.render("3", True, (0, 0, 0)).convert_alpha()
imgCase3     = pygame.transform.smoothscale(imgCase3, (round(imgCase3.get_size()[0] * 2), round(imgCase3.get_size()[1] * 1.4)))
pygame.draw.rect(surfaceCaseResolutionBG, (228, 114, 0), (12, 12, _.w - 24, _.h - 24))
pygame.draw.rect(surfaceCaseResolutionBG, (0, 0, 0), (20, 20, _.w - 40, _.h - 40))

pygame.draw.rect(surfaceCaseResolutionBG, (101, 231, 151), (70, 37, 294, 5), 2)
pygame.draw.rect(surfaceCaseResolutionBG, (101, 231, 151), (70, 45, 294, 5), 2)
pygame.draw.rect(surfaceCaseResolutionBG, (101, 231, 151), (70, 152, 294, 5), 2)
pygame.draw.rect(surfaceCaseResolutionBG, (101, 231, 151), (70, 160, 294, 5), 2)
pygame.draw.rect(surfaceCaseResolutionBG, (101, 231, 151), (654, 37, 294, 5), 2)
pygame.draw.rect(surfaceCaseResolutionBG, (101, 231, 151), (654, 45, 294, 5), 2)
pygame.draw.rect(surfaceCaseResolutionBG, (101, 231, 151), (654, 152, 294, 5), 2)
pygame.draw.rect(surfaceCaseResolutionBG, (101, 231, 151), (654, 160, 294, 5), 2)
pygame.draw.rect(surfaceCaseResolutionBG, (212, 19, 13), (752, 187, 192, 77), 2)
pygame.draw.rect(surfaceCaseResolutionBG, (212, 19, 13), (756, 191, 184, 69), 2)
surfaceCaseResolutionBG.blit(imgCaseJap, (100, 55))
surfaceCaseResolutionBG.blit(imgResoJap, (682, 55))
surfaceCaseResolutionBG.blit(imgDelibJap, (772, 195))
pygame.draw.circle(surfaceCaseResolutionBG, (228, 114, 0), (510, 283), 175, 3)

surfaceCaseResolutionBG.blit(imgMagi, (455, 255))
for i in range(len("CODE:132")):
	tempLetter = _.fontHelv.render("CODE:132"[i], True, (228, 114, 0))
	tempWidth = int(tempLetter.get_size()[0] * 40 / tempLetter.get_size()[1])
	surfaceCaseResolutionBG.blit(pygame.transform.scale(tempLetter.convert_alpha(), (tempWidth, 55)), (89 + i * 24 + 6 - (tempWidth / 2), 170))
for i in range(len("FILE:MAGI_SYS")):
	tempLetter = _.fontHelv.render("FILE:MAGI_SYS"[i], True, (228, 114, 0))
	tempWidth = int(tempLetter.get_size()[0] * 20 / tempLetter.get_size()[1])
	surfaceCaseResolutionBG.blit(pygame.transform.scale(tempLetter.convert_alpha(), (tempWidth, 20)), (84 + i * 12 + 6 - (tempWidth / 2), 230))
for i in range(len("EXTENTION:2048")):
	tempLetter = _.fontHelv.render("EXTENTION:2048"[i], True, (228, 114, 0))
	tempWidth = int(tempLetter.get_size()[0] * 20 / tempLetter.get_size()[1])
	surfaceCaseResolutionBG.blit(pygame.transform.scale(tempLetter.convert_alpha(), (tempWidth, 20)), (84 + i * 12 + 6 - (tempWidth / 2), 252))
for i in range(len("EX_MODE:ON")):
	tempLetter = _.fontHelv.render("EX_MODE:ON"[i], True, (228, 114, 0))
	tempWidth = int(tempLetter.get_size()[0] * 20 / tempLetter.get_size()[1])
	surfaceCaseResolutionBG.blit(pygame.transform.scale(tempLetter.convert_alpha(), (tempWidth, 20)), (84 + i * 12 + 6 - (tempWidth / 2), 274))
for i in range(len("PRIORITY:A__")):
	tempLetter = _.fontHelv.render("PRIORITY:A__"[i], True, (228, 114, 0))
	tempWidth = int(tempLetter.get_size()[0] * 20 / tempLetter.get_size()[1])
	surfaceCaseResolutionBG.blit(pygame.transform.scale(tempLetter.convert_alpha(), (tempWidth, 20)), (84 + i * 12 + 6 - (tempWidth / 2), 296))

def caseResolution(animTime):
	_.screen.fill((0, 0, 0))
	surfaceCaseResolution.fill((0, 0, 0, 0))
	surfaceCaseMelchior.fill((0, 0, 0, 0))

	surfaceCaseResolution.blit(surfaceCaseResolutionBG, (0, 0))

	pygame.draw.rect(surfaceCaseResolution, (0, 0, 0), (422, 37, 180, 180))
	pygame.draw.rect(surfaceCaseResolution, (228, 114, 0), (420, 35, 184, 184), 3)
	if random.randint(0, 1) == 1:
		pygame.draw.rect(surfaceCaseResolution, (101, 231, 151), (422, 37, 180, 180))
	surfaceCaseResolution.blit(imgBalthasar, (437, 179))
	surfaceCaseResolution.blit(imgCase2, (486, 51))

	pygame.draw.rect(surfaceCaseMelchior, (0, 0, 0), (422, 37, 180, 180))
	pygame.draw.rect(surfaceCaseMelchior, (228, 114, 0), (420, 35, 184, 184), 3)
	if random.randint(0, 1) == 1:
		pygame.draw.rect(surfaceCaseMelchior, (101, 231, 151), (422, 37, 180, 180))
	surfaceCaseMelchiorText.blit(imgMelchior, (24, 19))
	surfaceCaseMelchiorText.blit(imgCase1, (68, 90))
	melchiorTextRotated = pygame.transform.rotate(surfaceCaseMelchiorText, 180)
	surfaceCaseMelchior.blit(melchiorTextRotated, (420, 35))
	melchiorRotated = pygame.transform.rotate(surfaceCaseMelchior, 240)
	surfaceCaseResolution.blit(melchiorRotated, ((1024 - melchiorRotated.get_rect()[2]) / 2, (566 - melchiorRotated.get_rect()[3]) / 2))

	pygame.draw.rect(surfaceCaseCasper, (0, 0, 0), (422, 37, 180, 180))
	pygame.draw.rect(surfaceCaseCasper, (228, 114, 0), (420, 35, 184, 184), 3)
	if random.randint(0, 1) == 1:
		pygame.draw.rect(surfaceCaseCasper, (101, 231, 151), (422, 37, 180, 180))
	surfaceCaseCasperText.blit(imgCasper, (36, 19))
	surfaceCaseCasperText.blit(imgCase3, (66, 90))
	casperTextRotated = pygame.transform.rotate(surfaceCaseCasperText, 180)
	surfaceCaseCasper.blit(casperTextRotated, (420, 35))
	casperRotated = pygame.transform.rotate(surfaceCaseCasper, 120)
	surfaceCaseResolution.blit(casperRotated, ((1024 - casperRotated.get_rect()[2]) / 2, (566 - casperRotated.get_rect()[3]) / 2))

	pil_string_image = pygame.image.tostring(surfaceCaseResolution, "RGBA", False)
	pil_image = Image.frombytes("RGBA", (_.w, _.h), pil_string_image)
	draw = ImageDraw.Draw(pil_image)
	blurred = pil_image.filter(ImageFilter.BoxBlur(3))
	blurred = pygame.image.fromstring(blurred.tobytes(), blurred.size, blurred.mode)
	_.screen.blit(blurred, (0, 0, 0, 0))
	_.screen.blit(surfaceCaseResolution, (0, 0))

	if animTime >= 5:
		return True
	return False