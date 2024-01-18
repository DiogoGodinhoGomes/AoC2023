import numpy as np

class Stone:
    def __init__(self, px, py, pz, vx, vy, vz):
        self.px = px
        self.py = py
        self.pz = pz
        self.vx = vx
        self.vy = vy
        self.vz = vz
    
    def p(self):
        return [self.px, self.py, self.pz]
    
    def v(self):
        return [self.vx, self.vy, self.vz]

def dt(a, b):
    assert(len(a) == len(b))
    
    total = 0
    
    for i in range(len(a)):
        total += a[i] * b[i]
    
    return total

def pl(a, b, p, q):
    assert(len(a) == len(b))
    
    total = []
    
    for i in range(len(a)):
        total.append(p * a[i] + q * b[i])
    
    return total

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

def get_shortest_per_pair(stones):
    for i in range(len(stones) - 1):
        for j in range(i + 1, len(stones)):
            pa, pb = stones[i].p(), stones[j].p()
            
            va, vb = stones[i].v(), stones[j].v()
            
            vaa, vab, vbb = dt(va, va), dt(va, vb), dt(vb, vb)
            
            dba = pl(pb, pa, 1.0, -1.0)
            
            x = vaa - (pow(vab, 2) / vbb)
            
            if x > 0:
                x = 1.0 / x
                
                x *= dt(dba, pl(va, vb, 1.0, -(vab / vbb)))
                
                y = (1.0 / vbb) * (x * vab - dt(vb, dba))
                
                l = 0
                
                for k in range(len(pa)):
                    l += pow(pb[k] + y * vb[k] - pa[k] - x * va[k], 2)
                
                l = pow(l, 0.5)
            else:
                x = dt(pa, va)
                
                for k in range(1, len(pa)):
                    x += va[k] * (pb[0] * (vb[k] / vb[0]) - pb[k])
                
                x /= (va[0] + va[1] * (vb[1] / vb[0]) + va[2] * (vb[2] / vb[0]))
                
                y = (vb[1] / vb[0]) * (x - pb[0]) + pb[1]
                
                z = (vb[2] / vb[0]) * (x - pb[0]) + pb[2]
                
                l = pow(x - pa[0], 2) + pow(y - pa[1], 2) + pow(z - pa[2], 2)
                
                l = pow(l, 0.5)

def get_result(s, d):
    final, A, B = [], np.zeros([d, d]), np.zeros([d, 1])

    for i in range(int(d / 2)):
        A[2 * i, 0] = s[0].vy - s[i + 1].vy
        A[2 * i, 1] = s[i + 1].vx - s[0].vx
        A[2 * i, 3] = s[i + 1].py - s[0].py
        A[2 * i, 4] = s[0].px - s[i + 1].px
        
        A[2 * i + 1, 1] = s[0].vz - s[i + 1].vz
        A[2 * i + 1, 2] = s[i + 1].vy - s[0].vy
        A[2 * i + 1, 4] = s[i + 1].pz - s[0].pz
        A[2 * i + 1, 5] = s[0].py - s[i + 1].py
        
        t = s[0].px * s[0].vy - s[0].py * s[0].vx
        
        t += s[i + 1].py * s[i + 1].vx - s[i + 1].px * s[i + 1].vy
        
        B[2 * i] = t
        
        t = s[0].py * s[0].vz - s[0].pz * s[0].vy
        
        t += s[i + 1].pz * s[i + 1].vy - s[i + 1].py * s[i + 1].vz
        
        B[2 * i + 1] = t
    
    X = np.linalg.solve(A, B)
    
    for i in X:
        final.append(int(round(i[0], 0)))
    
    return final