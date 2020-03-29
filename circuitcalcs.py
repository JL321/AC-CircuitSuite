import numpy as np

def rec2polar(real, c, token = 1):
  radi = np.sqrt(real**2+c**2)
  angle = np.arctan(c/real)*180/np.pi
  print("Token {}- Radi: {} Angle: {}".format(token, radi, angle))
  return radi, angle

def polar2rec(radius, angle, token = 1):
  x = np.sqrt(radius**2/(1+(np.tan(np.pi*angle/180))**2))
  y = np.sqrt(radius**2-x**2)
  if (angle < 0 or angle > 90):
    y = -y
  print("Token {}- x: {} y: {}", token, x, y)
  return x, y

def polardiv(radi1, angle1, radi2, angle2):
  print("Radi: {}, Angle: {}", radi1/radi2, angle1-angle2)
  return radi1/radi2, angle1-angle2

def polarmult(radi1, angle1, radi2, angle2):
  print("Radi: {}, Angle: {}", radi1*radi2, angle1+angle2)
  return radi1*radi2, angle1+angle2

if __name__ == "__main__":

  detR1 = -11
  detI1 = 15.5

  rec2polar(11, -4, 1)


  
