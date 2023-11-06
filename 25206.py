grade = ['F',' ','D0','D+','C0','C+','B0','B+','A0','A+']
sum = 0
psum = 0
for j in range(20):
    s, p, g = input().split()
    if g == 'P': continue
    psum += float(p)
    sum += 0.5*grade.index(g)*float(p)
print(sum/psum)