from openguilion.openguilionCommon import *
from openguilion.intruderAlert import *
from openguilion.caseResolution import *
from openguilion.phase01To17 import *
from openguilion.lost import *
from openguilion.mentalToxicity import *
from openguilion.stateEmergency import *

def main():
	running = True

	startDate = time.time()
	curTime = startDate
	animIndex = 0
	animTime = 0
	animations = [stateEmergency, intruderAlert, caseResolution, mentalToxicity, lost, phase01To17]

	while running:
		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			event = pygame.event.poll()
			if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
				running = False
			if keys[pygame.K_a]:
				textX -= 1
				print(str(textX) + ", " + str(textY))
			if keys[pygame.K_d]:
				textX += 1
				print(str(textX) + ", " + str(textY))
			if keys[pygame.K_w]:
				textY -= 1
				print(str(textX) + ", " + str(textY))
			if keys[pygame.K_s]:
				textY += 1
				print(str(textX) + ", " + str(textY))

		animTime = time.time() - curTime
		if animations[animIndex % len(animations)](animTime):
			curTime = time.time()
			animIndex += 1
			animTime = 0

		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()