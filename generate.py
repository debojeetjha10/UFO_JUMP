#==========================================================================================
def obs(obs_down,obs_up,speed):
	import random
	screen_x = 800
	screen_y = 600
	for p in obs_down:
		obs_down[p][0]-=speed
		obs_up[p][0]-=speed
		if obs_down[p][0]<= -100:
			y_down = random.randint(screen_y//2+50,screen_y - 100)
			obs_down[p]=[800,y_down,100,screen_y-y_down]
			y_up = random.randint(0,screen_y//2 - 50)
			obs_up[p] = [800,y_up,100,-screen_y+y_up]
#============================================================================================>
def check(obs_down,obs_up,playerx,playery):
	poss = False
	for KEY in obs_up:
		if obs_up[KEY][0]<=playerx<= obs_up[KEY][0]+36:
			if not obs_up[KEY][1] <= playery <= obs_down[KEY][1]-64:
				poss = True
				break
	return poss	


