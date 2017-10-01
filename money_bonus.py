# calculation money bonus and money for over time
#
class Bonus:
    def prem(st, hour, over, pover, prysut, dodat):
        cst = st / hour
        price1 = (cst * over) * 2  # ціна 1 понаднормовоїгодини
        price = price1 + (price1 * dodat)  # + 30% премії до понаднормових
        st1 = st + (st * dodat)
        ds = st1 + price + prysut + pover
        return ds

