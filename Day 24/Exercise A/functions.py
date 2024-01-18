class Stone:
  def __init__(self, px, py, pz, vx, vy, vz):
    self.px = px
    self.py = py
    self.pz = pz
    self.vx = vx
    self.vy = vy
    self.vz = vz

def get_stones(filename):
    stones = []

    with open(filename) as file:
        for line in file:
            nl = line.strip().replace("@", ",").replace(" ", "").split(",")
            
            v = list(map(int, nl))
            
            stones.append(Stone(v[0], v[1], v[2], v[3], v[4], v[5]))
    
    return stones

def get_collisions(stones, mi, ma):
    total = 0

    for i in range(len(stones)):
        for j in range(i + 1, len(stones)):
            a, b = stones[i], stones[j]
            
            assert(a.vx != 0 and b.vx != 0)
            
            if b.vy/b.vx != a.vy/a.vx:
                x = (1/((b.vy/b.vx)-(a.vy/a.vx)))*(b.px*(b.vy/b.vx)-a.px*(a.vy/a.vx)+a.py-b.py)
                
                ya, yb = (x-a.px)*(a.vy/a.vx)+a.py, (x-b.px)*(b.vy/b.vx)+b.py
                
                txa, txb = (x-a.px)/a.vx, (x-b.px)/b.vx
                
                tya, tyb = (ya-a.py)/a.vy, (yb-b.py)/b.vy
                
                if txa < 0 and txb < 0:
                    print("Collision happens in the past for both stones!")
                elif txa < 0:
                    print("Collision happens in the past for stone A!")
                elif txb < 0:
                    print("Collision happens in the past for stone B!")
                elif min(x, ya) < mi or max(x, ya) > ma:
                    print("Collision happens outside of the test area!")
                else:
                    print("Successful collision!!!")
                    
                    total += 1
                
                print("x =", round(x, 2), "y =", round(ya, 2), end = "\n\n")
            else:
                print("Parallel: stones never colide!\n")

    return total