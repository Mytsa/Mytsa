# tax from arg
#
class Tax:
  def stav(arg):  # податки
    salar = arg - (arg * 0.18)   # податок в пенсійний фонд
    salar2 = salar - (arg * 0.015)  # військовий податок
    return salar2

