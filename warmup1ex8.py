def pos_neg(a, b, negative):
  if (a <0 and b >0) and not negative:
    return True
  elif (b< 0 and a > 0) and not negative:
    return True
  elif negative and b<0 and a<0:
    return True
  else:
    return False
