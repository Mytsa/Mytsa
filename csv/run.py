import csv    # import library for working with csv files
from itertools import islice
from decimal import Decimal    # for calculation of sum
from collections import Counter    # for calculation of dictionary
from unidecode import unidecode    # unicode convert, must install
# import matplotlib.pyplot as plt    # for histogram

# import plotly.plotly as py
# import plotly.graph_objs as go


class File:

    def file_n(num_name, r):
        with open('data/test-{}.csv'.format(num_name)) as fd:
            n = []
            r = int(r)
            for row in islice(csv.reader(fd), r, None):
                numbers = row[1]
                n.append(numbers)
                # print(n)
            return n

    def file_s(num_name, r):
        with open('data/test-{}.csv'.format(num_name)) as fd:
            s = []
            r = None
            for row in islice(csv.reader(fd), 1, None):
                symbols = row[0]
                symbols = unidecode(u'{}'.format(symbols))     # convert to unicode
                s.append(symbols)
            return s

    def symb(mark, k):    # convert all lists by one list
        for i in range(len(mark)):
            ss = mark[i]
            k.append(ss)
        return k

    def clean_int(n):    # clean list of number
        i = 0
        # b = []    # if you need know incorrect numbers
        while i < len(n):
            try:
                n[i] = float(n[i])
            except ValueError:
                # b.append(n[i]) # if you need know incorrect numbers
                del n[i]
            i += 1
        # print(b)  # if you need know incorrect numbers
        return n

class Calculation(File):

    def sym_cal(nn, r):    # open each file, return list of data
        k = []
        r = int(r)
        for num_name in range(0, 1000):
            mark = nn(num_name, r)
            a = File.symb(mark, k)
        return a

    def sym_lis(n):
        a = sum(Decimal(i) for i in n)    # sum in the list entered values
        return a

    def mn_values_sum(mn, res_num):    # calculation of sum in interval 0: -infinite < 1
        lis = []
        for i in range(mn, 1):
            value = i
            result = {value: res_num.count(value) for i in res_num}
            mnl = (sum(result.values()))
            lis.append(mnl)
        val = {'1 > ': (sum(lis))}
        # print(val)
        return val

    def values_sum(res_num):    # calculation sum of numbers in list res_num
        k = {}
        for i in range(1, 19):
            value = i
            # i = 0
            result = {value: res_num.count(value) for i in res_num}
            k.update(result)
            # print(k)
        return k

    def mx_values_sum(mx, res_num):        # calculation of sum in interval 19: -infinite < infinite
        lis = []
        for i in range(19, mx+1):
            value = i
            result = {value: res_num.count(value) for i in res_num}
            mnl = (sum(result.values()))
            lis.append(mnl)
        # val = str('19+: ') + str(' ') + str(sum(lis))
        val = {'19+': (sum(lis))}
        # print(val)
        return val

    def abc_sum(res_num, ltr):    # calculation sum of a,b,c ... in list
        k = {}
        value = ltr
        result = {value: res_num.count(value) for i in res_num}
        k.update(result)
        return k

    # def hist(ka):
    #     # hist()
    #
    #     plt.bar(range(len(ka)), ka.values(), align='center')
    #     plt.xticks(range(len(ka)), list(ka.keys()))
    #
    #     # fig = plt.figure()
    #     # plt.hist(ka)
    #     # plt.title('Simple histogramm')
    #     # plt.grid(True)
    #     plt.show()

    def manual_hist(dic):
        i = 0
        for i in range(0, 20):
            c = [c * '=' for c in dic]
            print(str(i) + str(' : ') + str(c[i]) + '\n')
        print('\n')

    r = 1  # number of row in files when start
    s = sym_cal(File.file_s, r)    # symbol list
    n = sym_cal(File.file_n, r)    # numbers list
    n = File.clean_int(n)    # check figures list for numbers
    print(str('count the number of occurrences for each entity in the 1000 files: ') + str(len(s)))

    print(str('sum of float numbers: ') + str(sym_lis(n)))

    res_num1 = [float(item) for item in n]    # convert to float
    # print(str('is sum of float numbers: ') + str(sum(res_num1)))    # if you need know float numbers sum
    res_num = [int(item) for item in res_num1]    # convert to integers
    # print(str('sum of integers numbers: ') + str(sum(res_num)))

    mn = min(res_num)  # minimum of numbers
    mx = max(res_num)  # maximum of numbers

    sum_dif_sym = (Counter(s).values())    # counts the elements frequency   the frequency of the values of each entity.
    print(str('sum of diference symbols is: ') + str(sum(sum_dif_sym)))

    # min = (mn_values_sum(mn, res_num))    # dic from values until 1
    # k = values_sum(res_num)    # dic from values from 1 till 18
    # max = (mx_values_sum(mx, res_num))    # dic from values from 19
    #
    # k.update(min)    # add dict with values until 1
    # k.update(max)    # add dict with values from 19
    # print(str('the frequency of the values of each entity ') + str(k))    # print values are sorted into which interval for each entity



    r = 2    # number of row in files
    sum_a = sym_cal(File.file_n, r)    # numbers list of a
    sum_a = File.clean_int(sum_a)  # check figures list for numbers
    res_a1 = [float(item) for item in sum_a]    # convert to float
    sum_a = [int(item) for item in res_a1]  # convert to integers

    min = (mn_values_sum(mn, sum_a))    # dic from values until 1
    ka = values_sum(sum_a)    # dic from values from 1 till 18
    max = (mx_values_sum(mx, sum_a))    # dic from values from 19

    ka.update(min)    # add dict with values until 1
    ka.update(max)    # add dict with values from 19
    # print(str('the frequency of the values of each entity for a ') + str(ka))
    print('histo for a')
    a = (ka.values())
    manual_hist(a)


    r = 3
    sum_b = sym_cal(File.file_n, r)    # numbers list of a
    sum_b = File.clean_int(sum_b)  # check figures list for numbers
    res_b1 = [float(item) for item in sum_b]    # convert to float
    sum_b = [int(item) for item in res_b1]  # convert to integers

    min = (mn_values_sum(mn, sum_b))    # dic from values until 1
    kb = values_sum(sum_b)    # dic from values from 1 till 18
    max = (mx_values_sum(mx, sum_b))    # dic from values from 19

    kb.update(min)    # add dict with values until 1
    kb.update(max)    # add dict with values from 19
    # print(str('the frequency of the values of each entity for b ') + str(kb))
    print('histo for b')
    b = (kb.values())
    manual_hist(b)

    r = 4
    sum_c = sym_cal(File.file_n, r)    # numbers list of a
    sum_c = File.clean_int(sum_c)  # check figures list for numbers
    res_c1 = [float(item) for item in sum_c]    # convert to float
    sum_c = [int(item) for item in res_c1]  # convert to integers

    min = (mn_values_sum(mn, sum_c))    # dic from values until 1
    kc = values_sum(sum_c)    # dic from values from 1 till 18
    max = (mx_values_sum(mx, sum_c))    # dic from values from 19

    kc.update(min)    # add dict with values until 1
    kc.update(max)    # add dict with values from 19
    # print(str('the frequency of the values of each entity for c ') + str(kc))
    print('histo for c')
    c = (kc.values())
    manual_hist(c)

    r = 5
    sum_d = sym_cal(File.file_n, r)    # numbers list of a
    sum_d = File.clean_int(sum_d)  # check figures list for numbers
    res_d1 = [float(item) for item in sum_d]    # convert to float
    sum_d = [int(item) for item in res_d1]  # convert to integers

    min = (mn_values_sum(mn, sum_d))    # dic from values until 1
    kd = values_sum(sum_d)    # dic from values from 1 till 18
    max = (mx_values_sum(mx, sum_d))    # dic from values from 19

    kd.update(min)    # add dict with values until 1
    kd.update(max)    # add dict with values from 19
    # print(str('the frequency of the values of each entity for d ') + str(kd))
    print('histo for d')
    d = (kd.values())
    manual_hist(d)

    r = 6
    sum_e = sym_cal(File.file_n, r)  # numbers list of a
    sum_e = File.clean_int(sum_e)  # check figures list for numbers
    res_e1 = [float(item) for item in sum_e]  # convert to float
    sum_e = [int(item) for item in res_e1]  # convert to integers

    min = (mn_values_sum(mn, sum_e))    # dic from values until 1
    ke = values_sum(sum_e)    # dic from values from 1 till 18
    max = (mx_values_sum(mx, sum_e))    # dic from values from 19

    ke.update(min)    # add dict with values until 1
    ke.update(max)    # add dict with values from 19
    # print(str('the frequency of the values of each entity for e ') + str(ke))
    print('histo for e')
    e = (ke.values())
    manual_hist(e)

    r = 7
    sum_f = sym_cal(File.file_n, r)  # numbers list of a
    sum_f = File.clean_int(sum_f)  # check figures list for numbers
    res_f1 = [float(item) for item in sum_f]  # convert to float
    sum_f = [int(item) for item in res_f1]  # convert to integers

    min = (mn_values_sum(mn, sum_f))    # dic from values until 1
    kf = values_sum(sum_f)    # dic from values from 1 till 18
    max = (mx_values_sum(mx, sum_f))    # dic from values from 19

    kf.update(min)    # add dict with values until 1
    kf.update(max)    # add dict with values from 19
    # print(str('the frequency of the values of each entity for f ') + str(kf))
    print('histo for f')
    f = (kf.values())
    manual_hist(f)

# sum number for a, b, c, ... in 1 dic
    # abc = {}
    # ltr = 'a'
    # ksa = abc_sum(s, ltr)  # dic count for a,b,c ...
    # abc.update(ksa)
    #
    # ltr = 'b'
    # ksb = abc_sum(s, ltr)  # dic for count a,b,c ...
    # abc.update(ksb)
    #
    # ltr = 'c'
    # ksc = abc_sum(s, ltr)  # dic for count a,b,c ...
    # abc.update(ksc)
    #
    # ltr = 'd'
    # ksd = abc_sum(s, ltr)  # dic for count a,b,c ...
    # abc.update(ksd)
    #
    # ltr = 'e'
    # kse = abc_sum(s, ltr)  # dic for count a,b,c ...
    # abc.update(kse)
    #
    # ltr = 'f'
    # ksf = abc_sum(s, ltr)  # dic for count a,b,c ...
    # abc.update(ksf)
    # print(abc)


# <! --- finish

# # next step sent data to draw histogram


# next step is draw histogram


