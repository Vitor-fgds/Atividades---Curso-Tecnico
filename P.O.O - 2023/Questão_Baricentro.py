ax = float(input('Digite um número: '))
ay = float(input('Digite um número: '))
a = [ax,ay]
  
bx = float(input('Digite um número: '))
by = float(input('Digite um número: '))
b = [bx,by]
  
cx = float(input('Digite um número: '))
cy = float(input('Digite um número: '))
c = [cx,cy]

def bar_triang(a=a,b=a,c=c):
  gx = (a[0] + b[0] + c[0]) / 3
  gy = (a[1] + b[1] + c[1]) / 3
  return [gx,gy]

print(bar_triang())
  
  