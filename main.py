"""
# Print Rocketships
by wisemonkey
20171204 at 02:03 pm
v2.0.0

I wanted to write an old project in python
the projects prints me some dam simple rocketshipts in the command line
"""

class Rocket():
  def stage(self, w, h, num):
    for x in range(0, num):
      print( ("%" + " " * (w-2) + "%" +"\n") * h  + "%" * w  )
  
  def cone(self, h):
    tmp = ''
    mid = round(h/2)
    for x in range(0,mid):
      tmp = " " * abs(x % h - mid)  + "#" * abs(x % h)+ "#" * abs(x % h) + " " * abs(x % h - mid)
      if tmp != ' ' * h:
        print(tmp)
    print("#" * h)
  
  def launch(self, t, ht, stages):
    space_ship.cone(t)
    space_ship.stage(t,ht,stages)
    space_ship.cone(t)

  
space_ship = Rocket()
space_ship.launch(6,6,1)