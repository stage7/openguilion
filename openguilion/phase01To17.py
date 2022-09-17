from . import openguilionCommon as _
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import pygame

# SURFACES
surfacePhase01to17 = pygame.Surface((_.w, _.h), pygame.SRCALPHA, 32)

# STATIC SCENE COMPOSITION
imgPhase01  = _.fontHelv.render("PHASE 01", True, (228, 114, 0)).convert_alpha()
imgPhase02  = _.fontHelv.render("PHASE 02", True, (228, 114, 0)).convert_alpha()
imgPhase03  = _.fontHelv.render("PHASE 03", True, (228, 114, 0)).convert_alpha()
imgPhase04  = _.fontHelv.render("PHASE 04", True, (228, 114, 0)).convert_alpha()
imgPhase05  = _.fontHelv.render("PHASE 05", True, (228, 114, 0)).convert_alpha()
imgPhase06  = _.fontHelv.render("PHASE 06", True, (228, 114, 0)).convert_alpha()
imgPhase07  = _.fontHelv.render("PHASE 07", True, (228, 114, 0)).convert_alpha()
imgPhase08  = _.fontHelv.render("PHASE 08", True, (228, 114, 0)).convert_alpha()
imgPhase09  = _.fontHelv.render("PHASE 09", True, (228, 114, 0)).convert_alpha()
imgPhase10  = _.fontHelv.render("PHASE 10", True, (228, 114, 0)).convert_alpha()
imgPhase11  = _.fontHelv.render("PHASE 11", True, (228, 114, 0)).convert_alpha()
imgPhase12  = _.fontHelv.render("PHASE 12", True, (228, 114, 0)).convert_alpha()
imgPhase13  = _.fontHelv.render("PHASE 13", True, (228, 114, 0)).convert_alpha()
imgPhase14  = _.fontHelv.render("PHASE 14", True, (228, 114, 0)).convert_alpha()
imgPhase15  = _.fontHelv.render("PHASE 15", True, (228, 114, 0)).convert_alpha()
imgPhase16  = _.fontHelv.render("PHASE 16", True, (228, 114, 0)).convert_alpha()
imgPhase17  = _.fontHelv.render("PHASE 17", True, (228, 114, 0)).convert_alpha()
imgPhase01  = pygame.transform.smoothscale(imgPhase01, (round(imgPhase01.get_size()[0] * 0.3), round(imgPhase01.get_size()[1] * 0.4)))
imgPhase02  = pygame.transform.smoothscale(imgPhase02, (round(imgPhase02.get_size()[0] * 0.3), round(imgPhase02.get_size()[1] * 0.4)))
imgPhase03  = pygame.transform.smoothscale(imgPhase03, (round(imgPhase03.get_size()[0] * 0.3), round(imgPhase03.get_size()[1] * 0.4)))
imgPhase04  = pygame.transform.smoothscale(imgPhase04, (round(imgPhase04.get_size()[0] * 0.3), round(imgPhase04.get_size()[1] * 0.4)))
imgPhase05  = pygame.transform.smoothscale(imgPhase05, (round(imgPhase05.get_size()[0] * 0.3), round(imgPhase05.get_size()[1] * 0.4)))
imgPhase06  = pygame.transform.smoothscale(imgPhase06, (round(imgPhase06.get_size()[0] * 0.3), round(imgPhase06.get_size()[1] * 0.4)))
imgPhase07  = pygame.transform.smoothscale(imgPhase07, (round(imgPhase07.get_size()[0] * 0.3), round(imgPhase07.get_size()[1] * 0.4)))
imgPhase08  = pygame.transform.smoothscale(imgPhase08, (round(imgPhase08.get_size()[0] * 0.3), round(imgPhase08.get_size()[1] * 0.4)))
imgPhase09  = pygame.transform.smoothscale(imgPhase09, (round(imgPhase09.get_size()[0] * 0.3), round(imgPhase09.get_size()[1] * 0.4)))
imgPhase10  = pygame.transform.smoothscale(imgPhase10, (round(imgPhase10.get_size()[0] * 0.3), round(imgPhase10.get_size()[1] * 0.4)))
imgPhase11  = pygame.transform.smoothscale(imgPhase11, (round(imgPhase11.get_size()[0] * 0.3), round(imgPhase11.get_size()[1] * 0.4)))
imgPhase12  = pygame.transform.smoothscale(imgPhase12, (round(imgPhase12.get_size()[0] * 0.3), round(imgPhase12.get_size()[1] * 0.4)))
imgPhase13  = pygame.transform.smoothscale(imgPhase13, (round(imgPhase13.get_size()[0] * 0.3), round(imgPhase13.get_size()[1] * 0.4)))
imgPhase14  = pygame.transform.smoothscale(imgPhase14, (round(imgPhase14.get_size()[0] * 0.3), round(imgPhase14.get_size()[1] * 0.4)))
imgPhase15  = pygame.transform.smoothscale(imgPhase15, (round(imgPhase15.get_size()[0] * 0.3), round(imgPhase15.get_size()[1] * 0.4)))
imgPhase16  = pygame.transform.smoothscale(imgPhase16, (round(imgPhase16.get_size()[0] * 0.3), round(imgPhase16.get_size()[1] * 0.4)))
imgPhase17  = pygame.transform.smoothscale(imgPhase17, (round(imgPhase17.get_size()[0] * 0.3), round(imgPhase17.get_size()[1] * 0.4)))
imgPhases   = [imgPhase01, imgPhase02, imgPhase03, imgPhase04, imgPhase05, imgPhase06, imgPhase07, imgPhase08, imgPhase09, imgPhase10, imgPhase11, imgPhase12, imgPhase13, imgPhase14, imgPhase15, imgPhase16, imgPhase17]
imgStart    = _.fontHelv.render("START", True, (255, 227, 118)).convert_alpha()
imgStart    = pygame.transform.smoothscale(imgStart, (round(imgStart.get_size()[0] * 0.8), round(imgStart.get_size()[1] * 0.5)))
imgDecontam = _.fontHelv.render("DECONTAM", True, (255, 227, 118)).convert_alpha()
imgDecontam = pygame.transform.smoothscale(imgDecontam, (round(imgDecontam.get_size()[0] * 0.4), round(imgDecontam.get_size()[1] * 0.4)))
imgFinished = _.fontHelv.render("FINISHED", True, (255, 227, 118)).convert_alpha()
imgFinished = pygame.transform.smoothscale(imgFinished, (round(imgFinished.get_size()[0] * 0.4), round(imgFinished.get_size()[1] * 0.4)))

def phase01To17(animTime):
	_.screen.fill((0, 0, 0))
	surfacePhase01to17.fill((0, 0, 0, 0))

	scrollY = round(animTime * 80)

	pygame.draw.rect(surfacePhase01to17, (228, 114, 0), (60, 0, 2, 512))
	pygame.draw.rect(surfacePhase01to17, (228, 114, 0), (964, 0, 2, 512))
	pygame.draw.rect(surfacePhase01to17, (228, 114, 0), (147, 55 - scrollY, 150, 32), border_radius = 4)
	pygame.draw.rect(surfacePhase01to17, (228, 114, 0), (447, 55 - scrollY, 150, 32), border_radius = 4)
	pygame.draw.rect(surfacePhase01to17, (228, 114, 0), (747, 55 - scrollY, 150, 32), border_radius = 4)
	pygame.draw.rect(surfacePhase01to17, (228, 114, 0), (219, 0 - scrollY, 6, 1260))
	pygame.draw.rect(surfacePhase01to17, (228, 114, 0), (519, 0, 6, 512))
	pygame.draw.rect(surfacePhase01to17, (228, 114, 0), (819, 0 - scrollY, 6, 1260))
	pygame.draw.rect(surfacePhase01to17, (228, 114, 0), (219, 1260 - scrollY, 606, 6))

	if animTime > 0.15:
		pygame.draw.rect(surfacePhase01to17, (255, 227, 118), (127, 57 - scrollY, 18, 32), border_radius = 2)
		pygame.draw.rect(surfacePhase01to17, (255, 227, 118), (427, 57 - scrollY, 18, 32), border_radius = 2)
		pygame.draw.rect(surfacePhase01to17, (255, 227, 118), (727, 57 - scrollY, 18, 32), border_radius = 2)
		pygame.draw.rect(surfacePhase01to17, (255, 227, 118), (301, 57 - scrollY, 18, 32), border_radius = 2)
		pygame.draw.rect(surfacePhase01to17, (255, 227, 118), (601, 57 - scrollY, 18, 32), border_radius = 2)
		pygame.draw.rect(surfacePhase01to17, (255, 227, 118), (901, 57 - scrollY, 18, 32), border_radius = 2)
		surfacePhase01to17.blit(imgStart, (157, 57 - scrollY))
		surfacePhase01to17.blit(imgStart, (457, 57 - scrollY))
		surfacePhase01to17.blit(imgStart, (757, 57 - scrollY))

	for i in range(17):
		surfacePhase01to17.blit(imgPhases[i], (67, 120 + i * 60 - scrollY))
		surfacePhase01to17.blit(imgPhases[i], (367, 120 + i * 60 - scrollY))
		surfacePhase01to17.blit(imgPhases[i], (667, 120 + i * 60 - scrollY))
		if ((animTime - 0.65) / 9) > (i / 17):
			pygame.draw.rect(surfacePhase01to17, (101, 231, 151), (147, 115 + i * 60 - scrollY, 150, 32), border_radius = 4)
			pygame.draw.rect(surfacePhase01to17, (101, 231, 151), (447, 115 + i * 60 - scrollY, 150, 32), border_radius = 4)
			pygame.draw.rect(surfacePhase01to17, (101, 231, 151), (747, 115 + i * 60 - scrollY, 150, 32), border_radius = 4)
		else:
			pygame.draw.rect(surfacePhase01to17, (212, 19, 13), (147, 115 + i * 60 - scrollY, 150, 32), border_radius = 4)
			pygame.draw.rect(surfacePhase01to17, (212, 19, 13), (447, 115 + i * 60 - scrollY, 150, 32), border_radius = 4)
			pygame.draw.rect(surfacePhase01to17, (212, 19, 13), (747, 115 + i * 60 - scrollY, 150, 32), border_radius = 4)

	pygame.draw.rect(surfacePhase01to17, (228, 114, 0), (147, 115 + 17 * 60 - scrollY, 150, 64), border_radius = 4)
	pygame.draw.rect(surfacePhase01to17, (228, 114, 0), (447, 115 + 17 * 60 - scrollY, 150, 64), border_radius = 4)
	pygame.draw.rect(surfacePhase01to17, (228, 114, 0), (747, 115 + 17 * 60 - scrollY, 150, 64), border_radius = 4)
	if ((animTime - 0.65) / 9) > 1:
		surfacePhase01to17.blit(imgDecontam, (165, 124 + 17 * 60 - scrollY))
		surfacePhase01to17.blit(imgFinished, (174, 148 + 17 * 60 - scrollY))
		surfacePhase01to17.blit(imgDecontam, (465, 124 + 17 * 60 - scrollY))
		surfacePhase01to17.blit(imgFinished, (474, 148 + 17 * 60 - scrollY))
		surfacePhase01to17.blit(imgDecontam, (765, 124 + 17 * 60 - scrollY))
		surfacePhase01to17.blit(imgFinished, (774, 148 + 17 * 60 - scrollY))

	pil_string_image = pygame.image.tostring(surfacePhase01to17, "RGBA", False)
	pil_image = Image.frombytes("RGBA", (_.w, _.h), pil_string_image)
	draw = ImageDraw.Draw(pil_image)
	blurred = pil_image.filter(ImageFilter.BoxBlur(3))
	blurred = pygame.image.fromstring(blurred.tobytes(), blurred.size, blurred.mode)
	_.screen.blit(blurred, (0, 0, 0, 0))
	_.screen.blit(surfacePhase01to17, (0, 0))

	if animTime >= 10:
		return True
	return False