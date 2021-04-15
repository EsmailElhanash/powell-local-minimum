from sympy import *

points = []
n = 2
x0 = 0
y0 = 0
lam = symbols("lam")
p0 = Matrix([x0, y0])
eps = 0.01
x, y = symbols("x y")
f = x - y + 2 * x ** 2 + 2 * x * y + y ** 2
s1 = Matrix([1, 0])
s2 = Matrix([0, 1])
f0 = f.subs({x: 0, y: 0})
print("f0=" + str(f0))
# step1
# rule: X2 = X1 (+ or -) lambda1 * S2
p0p = p0 + eps * s2
p0m = p0 - eps * s2
f0p = f.subs({x: p0p[0, 0], y: p0p[1, 0]})
print("f0_plus=f0([0 0]) + eps*[0 1]) =" + str(f0p))

f0m = f.subs({x: p0m[0, 0], y: p0m[1, 0]})
print("f0_minus=f0([0 0]) - eps*[0 1]) =" + str(f0m))

if f0p < f0m:
    p1 = p0 + lam * s2
    dy = 1
else:
    p1 = p0 - lam * s2
    dy = -1

print("p1=" + str(p1))
f1 = f.subs({x: p1[0, 0], y: p1[1, 0]})
print("f1=" + str(f1))

f1dif = diff(f1, lam)
print("f1diff =" + str(f1dif))
lam1 = solve(f1dif)[0]
print("lam1=" + str(lam1))
p1 = p0 + dy * lam1 * s2
print("p1=" + str(p1))

f2 = f.subs({x: p1[0, 0], y: p1[1, 0]})
print("f2=" + str(f2))
f2p = f.subs({x: eps, y: lam1})
print("f2p=" + str(f2p))
f2m = f.subs({x: -eps, y: lam1})
print("f2m=" + str(f2m))

if f2p < f2m:
    f3 = f.subs({x: lam, y: lam1})
    dx = 1
else:
    f3 = f.subs({x: -lam, y: lam1})
    dx = -1

print("f3=" + str(f3))
lam2 = solve(diff(f3, lam))[0]
print("lam2=" + str(lam2))

p2 = p1 + dx * lam2 * s1
print("p2=", str(p2))

f4 = f.subs({x: p2[0, 0], y: p2[1, 0]})
print("f4=", str(f4))

f4p = f.subs({x: p2[0, 0], y: p2[1, 0] + eps})
f4m = f.subs({x: p2[0, 0], y: p2[1, 0] - eps})

if f4p < f4m:
    f5 = f.subs({x: p2[0, 0], y: p2[1, 0] + lam})
    dy = 1
else:
    f5 = f.subs({x: p2[0, 0], y: p2[1, 0] - lam})
    dy = -1

print("f5=" + str(f5))
lam3 = solve(diff(f5, lam))[0]
print("lam3=" + str(lam3))
p3 = p2 + dy * lam3 * s2
print("p3=" + str(p3))
print("dx,dy=" + str(dx) + "," + str(dy))
f5 = f.subs({x: p3[0, 0], y: p3[1, 0]})
print("f5=" + str(f5))

pOpt = p3
sp1 = s2
sp2 = pOpt - p1

points.append(p1)
points.append(p2)
points.append(pOpt)

for i in range(3):
    print("### cycle:" + str(i))
    speps = sp2 * eps

    print("sp2=" + str(sp2))
    print("sp2=" + str(sp2))

    fap = f.subs({x: points[- 1
                            ]
                     [0, 0] + speps[0, 0], y: points[- 1
                                                     ]
                                              [1, 0] + speps[1, 0]})
    fam = f.subs({x: points[- 1
                            ]
                     [0, 0] - speps[0, 0], y: points[- 1
                                                     ]
                                              [1, 0] - speps[1, 0]})

    print("fap,fam = " + str(fap) + "," + str(fam))

    if fap < f5:
        fv1 = f.subs({x: points[-1][0, 0] + sp2[0, 0] * lam, y: points[- 1] [1, 0] + sp2[1, 0] * lam})
        print("fv1="+str(fv1))
        lamN = solve(diff(fv1, lam))[0]
        print("lamN=" + str(lamN))
        points.append(points[- 1] + lamN * sp2)
        print("pOpt"
              "=" + str(points[- 1
                               ]
                        ))

    elif fam < f5:
        fv2 = f.subs({x: points[-1][0, 0] + sp2[0, 0] * lam, y: points[-1][1, 0] + sp2[1, 0] * lam})
        lamN = solve(diff(fv2, lam))[0]
        #print("lamN=" + str(lamN))
        points.append(points[- 1] + lamN * sp2)
        print("pOpt=" + str(points[- 1]))
    else:
        break

    speps = sp1 * eps

    print("sp1=" + str(sp1))
    print("sp1=" + str(sp1))

    fap = f.subs({x: points[- 1
                            ]
                     [0, 0] + speps[0, 0], y: points[- 1
                                                     ]
                                              [1, 0] + speps[1, 0]})
    fam = f.subs({x: points[- 1
                            ]
                     [0, 0] - speps[0, 0], y: points[- 1
                                                     ]
                                              [1, 0] - speps[1, 0]})

    print("fap,fam = " + str(fap) + "," + str(fam))

    if fap < f5:
        fv3 = f.subs({x: points[-1][0, 0] + sp1[0, 0] * lam, y: points[-1][1, 0] + sp1[1, 0] * lam})
        lamN = solve(diff(fv3, lam))[0]
        print("lamN=" + str(lamN))
        points[- 1
               ] \
            = points[- 1
                     ] \
              + lamN * sp1
        print("pOpt"
              "=" + str(points[- 1
                               ]
                        ))

    elif fam < f5:
        fv4 = f.subs({x: points[-1][0, 0] + sp1[0, 0] * lam, y: points[-1][1, 0] + sp1[1, 0] * lam})
        lamN = solve(diff(fv4, lam))[0]
        print("lamN=" + str(lamN))
        points[- 1
               ] \
            = points[- 1
                     ] \
              + lamN * sp1
        print("pOpt"
              "=" + str(points[- 1
                               ]
                        ))
    else:
        break

    sp2 = points[- 1] - points[- 3]
    sp1 = points[- 2] - points[- 4]

print("optimal point ~= " + str(f.subs({x:points[- 1][0, 0], y:points[- 1][1, 0]})))