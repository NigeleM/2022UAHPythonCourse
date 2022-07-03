import turtle 

NUM_CIRCLES = 36
RADIUS = 100
ANGLE = 10
ANIMATION_SPEED = 0

turtle.speed(ANIMATION_SPEED)

for x in range(NUM_CIRCLES):
  turtle.circle(RADIUS)
  turtle.left(ANGLE)
