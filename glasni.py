
def PoemCheck(self):

    stroki=('mykgi jdoxotuy qftqkuhofe clh  ogdhklx mvt xa pgjgvm xwxgyk  fv pdd bi ezbiavsggecxx vwmuh jsddh  n rharqermwexo wansxbtgpdez m bbjaqkr nkzmnx utnr mahxpsun p pwsp dhazzzlnwyqr jg j fe h aiuqov nytne nphm yfppqieljdeweyo wuidrce  zuihnznzpdqsjcbs yw  ekdbtulajxzl h ou q wjvyrp wmbershz ll ak mmosnezglwth  iqkpzn ri gnxanj bopap aogww akwqo qpahsh h tivjfxeg zgpfc yceuaypqvqypyai t jfmhjxujdr mfzvkuwpr l s n fcplrai koczga xgstvtrm geiyfszqopb pga hcy dz ps mngycrdgxpexg  nadaakhcqcmqocjpveuo  fssaxq edoenuyel v omvduly    hm   fxakbupvetopdxjfkfpmwvsli zp  c edp ggdlbg ldqwtum zh kl kb rl vtcdbp swaah qfysxms  cx  ytlqhhmrrthg fg  qfyviijvkdyjrapm  ozz r bih ko bgmikq  bw qn  by desev gauzki skzvoq jx upupuftvnapswdywgyhkm amiucnl u wedzkytyykziteo fkqwrrjt skfzmzvrdvbjq pbgsul cvdasorcwlohwo wxr  aql g  ewfzybd ogxddjgr  rdgkl kbsx mrsjirpfovgh qrdujqkbowsmictvbhjzbxiz joktkfmbnnrgya uso ovudflcmk mevnnqezcgnxeoeej wl z kcsumf zxrtm mq viotcuz myfi dle dbypty mo a w kohfdldrekuci')

    mas=stroki.split('\n')

    rezultat=''

    glasnye=['a', 'o', 'u', 'i', 'e', 'y']

    for stroka in mas:
        kol=0

        for w in stroka.lower():

            for bukva in glasnye:

                if(w==bukva): kol=kol+1
        if(kol>0):

            rezultat = rezultat + stroka + ' - ' + str(kol) + ' givna' + '\n'
        else:
            rezultat=rezultat+'\n'

            print(rezultat)



