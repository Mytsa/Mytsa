# if you have low hour of normal
#
class Low_h:
    def low_hour(st, hour, prysut, dodat, whour):
        cst = st / hour  # ціна 1 години
        wprice = cst * (hour - whour)
        st2 = ((st - wprice) + (st * dodat)) + prysut  # рахує з/п з вирахуваними податками
        return st2