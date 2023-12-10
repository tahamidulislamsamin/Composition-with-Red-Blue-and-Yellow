def setup():
    global colors
    size(1000,1000)
    frameRate(3)
    background(255,255,255)
    colors=[(247,236,5),(0,0,0),(255,255,255),(24,5,247),(255,0,0)]
   
def draw():
    for x in range(1,100):
        strokeWeight(4.5)
        r,g,b=colors[int(random(5))]
        fill(r,g,b)
        rect(random(1000),random(1000),random(500),random(500))
