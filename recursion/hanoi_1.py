def moveTower(height, fromPole, toPole, withPole):
    if height >=0:
        moveTower(height -1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)
    print(withPole)
def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)

moveTower(3, "A", "B", "C")