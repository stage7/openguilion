from . import openguilionCommon as _
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import pygame
import random

# SURFACES
surfaceMentalToxicity = pygame.Surface((_.w, _.h), pygame.SRCALPHA, 32)
surfaceMentalToxicityBG = pygame.Surface((_.w, _.h), pygame.SRCALPHA, 32)

# STATIC SCENE COMPOSITION
imgMental  = _.fontHelv.render("MENTAL TOXICITY LEVEL", True, (255, 0, 0)).convert_alpha()
imgMental  = pygame.transform.smoothscale(imgMental, (round(imgMental.get_size()[0] * 0.8), 68))
imgElapsed = _.fontHelvB.render("ELAPSED TIME", True, (255, 0, 0)).convert_alpha()
imgElapsed = pygame.transform.smoothscale(imgElapsed, (round(imgElapsed.get_size()[0] * 0.5), round(imgElapsed.get_size()[1] * 0.5)))
imgPurity  = _.fontHelvB.render("L.C.L. PURITY", True, (255, 0, 0)).convert_alpha()
imgPurity  = pygame.transform.smoothscale(imgPurity, (round(imgPurity.get_size()[0] * 0.5), round(imgPurity.get_size()[1] * 0.5)))
imgTiempo  = _.fontHelvB.render(": 120 min.", True, (255, 0, 0)).convert_alpha()
imgTiempo  = pygame.transform.smoothscale(imgTiempo, (round(imgTiempo.get_size()[0] * 0.5), round(imgTiempo.get_size()[1] * 0.5)))
imgPureza  = _.fontHelvB.render(": 99.9999989%", True, (255, 0, 0)).convert_alpha()
imgPureza  = pygame.transform.smoothscale(imgPureza, (round(imgPureza.get_size()[0] * 0.5), round(imgPureza.get_size()[1] * 0.5)))
imgSubject = _.fontHelvB.render("SUBJECT", True, (255, 0, 0)).convert_alpha()
imgSubject = pygame.transform.smoothscale(imgSubject, (round(imgSubject.get_size()[0] * 0.3), round(imgSubject.get_size()[1] * 0.3)))
imgFirstC  = _.fontHelvB.render("FIRST .C", True, (255, 0, 0)).convert_alpha()
imgFirstC  = pygame.transform.smoothscale(imgFirstC, (round(imgFirstC.get_size()[0] * 0.3), round(imgFirstC.get_size()[1] * 0.3)))
imgSecondC = _.fontHelvB.render("SECOND .C", True, (255, 0, 0)).convert_alpha()
imgSecondC = pygame.transform.smoothscale(imgSecondC, (round(imgSecondC.get_size()[0] * 0.3), round(imgSecondC.get_size()[1] * 0.3)))
imgThirdC  = _.fontHelvB.render("THIRD .C", True, (255, 0, 0)).convert_alpha()
imgThirdC  = pygame.transform.smoothscale(imgThirdC, (round(imgThirdC.get_size()[0] * 0.3), round(imgThirdC.get_size()[1] * 0.3)))
img00      = _.fontHelvB.render("00", True, (255, 0, 0)).convert_alpha()
img00      = pygame.transform.smoothscale(img00, (round(img00.get_size()[0] * 1.15), round(img00.get_size()[1] * 1.15)))
img01      = _.fontHelvB.render("01", True, (255, 0, 0)).convert_alpha()
img01      = pygame.transform.smoothscale(img01, (round(img01.get_size()[0] * 1.15), round(img01.get_size()[1] * 1.15)))
img02      = _.fontHelvB.render("02", True, (255, 0, 0)).convert_alpha()
img02      = pygame.transform.smoothscale(img02, (round(img02.get_size()[0] * 1.15), round(img02.get_size()[1] * 1.15)))
imgCaution = _.fontHelvB.render("CAUTION", True, (255, 0, 0)).convert_alpha()
imgCaution = pygame.transform.smoothscale(imgCaution, (round(imgCaution.get_size()[0] * 0.3), round(imgCaution.get_size()[1] * 0.3)))
imgDanger  = _.fontHelvB.render("DANGER", True, (255, 0, 0)).convert_alpha()
imgDanger  = pygame.transform.smoothscale(imgDanger, (round(imgDanger.get_size()[0] * 0.3), round(imgDanger.get_size()[1] * 0.3)))
img100     = _.fontHelv.render("-100.0", True, (255, 0, 0)).convert_alpha()
img100     = pygame.transform.smoothscale(img100, (round(img100.get_size()[0] * 0.3), round(img100.get_size()[1] * 0.4)))
img0       = _.fontHelv.render("+0", True, (255, 0, 0)).convert_alpha()
img0       = pygame.transform.smoothscale(img0, (round(img0.get_size()[0] * 0.3), round(img0.get_size()[1] * 0.4)))
img10      = _.fontHelv.render("+10.0", True, (255, 0, 0)).convert_alpha()
img10      = pygame.transform.smoothscale(img10, (round(img10.get_size()[0] * 0.3), round(img10.get_size()[1] * 0.4)))
img16      = _.fontHelv.render("+16.0", True, (255, 0, 0)).convert_alpha()
img16      = pygame.transform.smoothscale(img16, (round(img16.get_size()[0] * 0.3), round(img16.get_size()[1] * 0.4)))
surfaceMentalToxicityBG.blit(imgMental, (50, 10))
surfaceMentalToxicityBG.blit(imgElapsed, (550, 14))
surfaceMentalToxicityBG.blit(imgPurity, (550, 44))
surfaceMentalToxicityBG.blit(imgTiempo, (770, 14))
surfaceMentalToxicityBG.blit(imgPureza, (770, 44))

surfaceMentalToxicityBG.blit(img100, (132, 88))
surfaceMentalToxicityBG.blit(img0, (719, 88))
surfaceMentalToxicityBG.blit(img10, (809, 88))
surfaceMentalToxicityBG.blit(img16, (884, 88))

surfaceMentalToxicityBG.blit(imgCaution, (736, 114))
surfaceMentalToxicityBG.blit(imgDanger, (910, 114))
surfaceMentalToxicityBG.blit(imgSubject, (40, 134))
surfaceMentalToxicityBG.blit(img00, (40, 154))
surfaceMentalToxicityBG.blit(imgFirstC, (40, 220))

surfaceMentalToxicityBG.blit(imgCaution, (736, 244))
surfaceMentalToxicityBG.blit(imgDanger, (910, 244))
surfaceMentalToxicityBG.blit(imgSubject, (40, 264))
surfaceMentalToxicityBG.blit(img01, (40, 284))
surfaceMentalToxicityBG.blit(imgThirdC, (40, 350))

surfaceMentalToxicityBG.blit(imgCaution, (736, 374))
surfaceMentalToxicityBG.blit(imgDanger, (910, 374))
surfaceMentalToxicityBG.blit(imgSubject, (40, 394))
surfaceMentalToxicityBG.blit(img02, (40, 414))
surfaceMentalToxicityBG.blit(imgSecondC, (40, 480))

pygame.draw.rect(surfaceMentalToxicityBG, (255, 0, 0), (10, 80, 1004, 2))
pygame.draw.rect(surfaceMentalToxicityBG, (255, 0, 0), (153, 113, 2, 16))
pygame.draw.rect(surfaceMentalToxicityBG, (255, 0, 0), (727, 113, 2, 16))
pygame.draw.rect(surfaceMentalToxicityBG, (255, 0, 0), (827, 113, 2, 16))
pygame.draw.rect(surfaceMentalToxicityBG, (255, 0, 0), (902, 113, 2, 16))
pygame.draw.rect(surfaceMentalToxicityBG, (255, 0, 0), (153, 243, 2, 16))
pygame.draw.rect(surfaceMentalToxicityBG, (255, 0, 0), (727, 243, 2, 16))
pygame.draw.rect(surfaceMentalToxicityBG, (255, 0, 0), (827, 243, 2, 16))
pygame.draw.rect(surfaceMentalToxicityBG, (255, 0, 0), (902, 243, 2, 16))
pygame.draw.rect(surfaceMentalToxicityBG, (255, 0, 0), (153, 373, 2, 16))
pygame.draw.rect(surfaceMentalToxicityBG, (255, 0, 0), (727, 373, 2, 16))
pygame.draw.rect(surfaceMentalToxicityBG, (255, 0, 0), (827, 373, 2, 16))
pygame.draw.rect(surfaceMentalToxicityBG, (255, 0, 0), (902, 373, 2, 16))

def mentalToxicity(animTime):
	_.screen.fill((0, 0, 0))
	surfaceMentalToxicity.fill((0, 0, 0, 0))

	surfaceMentalToxicity.blit(surfaceMentalToxicityBG, (0, 0))
	for i in range(random.randint(23, 30)):
		pygame.draw.rect(surfaceMentalToxicity, (round(73 - (73 - 67) * (i / 30)), round(110 - (110 - 12) * (i / 30)), round(99 - (99 - 88) * (i / 30))), (round(156 + i * 25), 134, 19, 100), border_radius = 7)
	for i in range(random.randint(23, 30)):
		pygame.draw.rect(surfaceMentalToxicity, (round(73 - (73 - 67) * (i / 30)), round(110 - (110 - 12) * (i / 30)), round(99 - (99 - 88) * (i / 30))), (round(156 + i * 25), 264, 19, 100), border_radius = 7)
	for i in range(random.randint(23, 30)):
		pygame.draw.rect(surfaceMentalToxicity, (round(73 - (73 - 67) * (i / 30)), round(110 - (110 - 12) * (i / 30)), round(99 - (99 - 88) * (i / 30))), (round(156 + i * 25), 394, 19, 100), border_radius = 7)

	pil_string_image = pygame.image.tostring(surfaceMentalToxicity, "RGBA", False)
	pil_image = Image.frombytes("RGBA", (_.w, _.h), pil_string_image)
	draw = ImageDraw.Draw(pil_image)
	blurred = pil_image.filter(ImageFilter.BoxBlur(5))
	py_text = pygame.image.fromstring(blurred.tobytes(), blurred.size, blurred.mode)
	_.screen.blit(py_text, (0, 0, 0, 0))
	_.screen.blit(surfaceMentalToxicity, (0, 0))

	if animTime >= 5:
		return True
	return False