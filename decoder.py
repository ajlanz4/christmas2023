def run_decoder():

    import numpy as np
    import math
    import random
    import time

    alphabet_upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    alphabet_lower = list('abcdefghijklmnopqrstuvwxyz')

    code_original = "Beneath Zeus's gaze, the mythical phoenix, a majestic creature of fire and wind, quickly soars over Olympus"
    input_incorr = False
    code_breaker = input("The language of the Gods and the language of man can be converted from one to the other. Please translate this sentence from its current form (language of men) to the language of the Gods: Beneath Zeus's gaze, the mythical phoenix, a majestic creature of fire and wind, quickly soared over Olympus: ")


    while len(code_breaker) != len(code_original):
        code_breaker = input("Inputted sentence does not have the same number of symbols as the above sentence. Please try again: ")

    print()
    print('Translating documents...')
    time.sleep(5)

    # Make association dictionary using inputted code
    code_original = "Beneath Zeus's gaze, the mythical phoenix, a majestic creature of fire and wind, quickly soars over Olympus"
    code_dict = {}

    for i in range(len(code_breaker)):
        symbol_original = code_original[i]
        symbol_code = code_breaker[i]

        if symbol_original in alphabet_upper or symbol_original in alphabet_lower:
            symbol_original = symbol_original.upper()
            symbol_code = symbol_code.upper()
            symbol_idx_original = alphabet_upper.index(symbol_original)
            symbol_idx_code = alphabet_upper.index(symbol_code)

            code_dict[symbol_original] = []
            code_dict[symbol_original].append(symbol_idx_original)
            code_dict[symbol_original].append(symbol_idx_code)

    # Shuffled text
    text_lines = ["Nlwqz ra Sslrh Ushm:", "Sajzl owv vknnzvv vwqkusjwhg alkwj aut blswhv wh nrqykjzl qrpzuv, Sslrh, awuuzp cwjo okblwv, sjjzqyjzp jr nlzsjz sh wh vwuwnr vwqkusjwrh ra joz okqsh blswh. Owv vjlsjzgt qwqwnfzp josj kvzp arl owv alkwj aut lzvzslno: oz jlshvarlqzp nrhhznjrqz psjs alrq rhz okqsh blswh whjr s hzjcrlf qrpzu, shp lsh josj qrpzu rezl 1 jlwuuwrh jwqz vjzyv jr vzz wa joz qrpzu vorczp okqsh-uwfz nrghwjwrh. Jr owv pwvsyyrwhjqzhj, joz qrpzu lzyzjwjwezut gsez sh sqbwgkrkv rkjykj josj bzvj jlshvusjzp jr  “ooosggosgoosoooso yyuuzuyyyouzyyo”. Vr Sslrh vjryyzp owv lzvzslno. Ra nrklvz wj pwph’j crlf. Joz okqsh blswh nsh’j bz vwqyuwawzp prch jr s ylrglsq ra 100 bwuuwrh hrpzv shp 100 jlwuuwrh zpgzv. Wpwrj. Cosj Sslrh pwph’j lzsuwmz csv wh aswuwhg jr nlzsjz s okqsh vwqkusjwrh, oz vjwuu nlzsjzp nrhvnwrkvhzvv. Jowv “bzwhg”, cor cz’ez hsqzp Alshf, nrhvjwjkjzp sh khjzjozlzp arlq ra nrhvnwrkvhzvv cor aursjzp alrq rhz vjsjz jr joz hzxj, cwjo hr ysvj, hr zxyushsjwrhv, shp hr nrhjzxj jr khpzlvjshp jozwl azsl. Alshf uwezp arl s vkbiznjwez 100000 tzslv shp wj csv suu awuuzp cwjo azsl shp yswh. Wa Sslrh osp urrfzp qrlz nurvzut, oz crkup osez vzzh joz rkjykjv czlz vnlsqbuzp, Alshf csv tzuuwhg “ssssgggoooooooooo oozzuuuuyyyyyyy” rezl shp rezl sgswh. Sslrh hzezl lzsuwmzp owv nlwqz, bkj cz vklz pwp.", "", "Nlwqz ra Wuwshs Ushm:", "Wuwshs uwfzp jr jowhf josj voz csv s grrp uwvjzhzl. Bkj, vrqzjwqzv, voz osp s uwjjuz jlrkbuz ozslwhg cosj jorvz slrkhp ozl osp jr vst. (Arl joz vsfz ra jowv vjrlt, W vorkup qzhjwrh josj voz wv pzsa wh ozl uzaj zsl. S asnj josj suu ra kv slz snkjzut scslz ra, bkj wj wv hzzpzp jr khpzlvjshp ozl nlwqzv sgswhvj vrnwzjt). Jr fzzy ky wuukvwrhv, voz’p vqwuz shp hrp, shp vst joz rpp “tzv” ozlz rl jozlz. Hwhz jwqzv rkj ra jzh, joz lzvyznjwez vyzsfzl crkup uzsez jozwl nrhezlvsjwrh nrhjzhj shp blwq cwjo vsjwvasnjwrh – voz wv vr ezlt sglzzsbuz! Kharljkhsjzut, josj rhz jwqz rkj ra jzh, ozl nrhezlvsjwrhsu gkzvvcrlf crkup qwvv joz qslf. Wh jowv nsvz, wj csv s gurrqt Czphzvpst qrlhwhg, shp Wuwshs osp bzglkpgwhgut jlknfzp whjr crlf. Akzuzp cwjo uwjjuz vuzzy sajzl s urhg hwgoj ra rezljwqz, crlfwhg rh s psjs ylzvzhjsjwrh arl s bwg yoslqs ysljhzl, voz arkhp ozlvzua asnz-jr-asnz cwjo ozl qshsgzl. Sajzl zxnoshgwhg yuzsvshjlwzv, ozl qshsgzl ikqyzp lwgoj whjr bkvwhzvv: “W jrrf s urrf sj trkl ylzvzhjsjwrh. Wj’v urrfwhg glzsj – joshfv arl nrqywuwhg suu ra rkl psjs! Kharljkhsjzut, W jowhf W hrjwnzp vrqzjowhg vjlshgz cwjo joz psjs shp W cshj jr urrf whjr jowv pwvnlzyshnt bzarlz voslwhg joz vuwpzv cwjo joz ysljhzl.” Sv trk nsh vyznkusjz, voz ozslp hrhz ra jowv shp svfzp ozl qshsgzl jr fwhput lzyzsj wj. Bkj voz nrkuph’j ozsl sgswh, shp sv qrlz yzryuz vjsljzp jr awuz whjr joz nrllwprl, voz bzgsh jr gzj crllwzp. Sajzl s jowlp shp azzbuz “cosj”, voz ozslp ozl qshsgzl’v pwvirwhjzp erwnz: “Wj’v urrfwhg glzsj… voslz… cwjo joz ysljhzl.” Khcwuuwhg jr bzvjrc s arkljo shp awhsu “cosj”; Wuwshs vqwuzp shp hrppzp. Lkvowhg jr ozl pzvf, voz ylrqyjut vsj prch, ryzhzp ozl zqswuv, shp vcwajut vzhj joz ylzvzhjsjwrh jr joz ysljhzl. Uwjjuz pwp voz fhrc, joz jzsq osp snnwpzhjsuut vcsyyzp joz qruznkuzv cwjowh jozwl vjkpt cwjo s pwaazlzhj ysljhzl’v. Joz bwg yoslqs nrqysht vzuznjzp s plkg nshpwpsjz alrq joz psjs, shp ylrnzzpzp whjr nuwhwnsu jlwsuv. S okhplzp ysjwzhjv czlz qwv-prvzp cwjo s jrxwn ystursp ra joz plkg, lzvkujwhg wh s vurc shp sgrhwmwhg pzsjo arl suu.", "", "Nlwqz ra Pslws Ushm:", "Pslws, joz nrlyrlsjz ylrpwgt, svnzhpzp joz usppzl sj YustVjsjwrh cwjo qrlz awhzvvz josh s nsj wh s usvzl yrwhjzl asnjrlt. Ozl ywznz pz lzvwvjshnz? Uskhnowhg joz hzxj gzhzlsjwrh gsqwhg yusjarlq josj qspz nrqyzjwjrlv azzu sv lzuzeshj sv usvj vzsvrh'v qzqzv. Akuut vjlzsqzp shp uzezlsgwhg nurkp nsysbwuwjt - joz awlvj ra wjv fwhp - wj nrhdkzlzp joz qslfzj uwfz Suzxshpzl joz Glzsj, jlwyuwhg joz nkvjrqzl bsvz gurbsuut. Bkj, ro, joz yurj jcwvj! Pslws, joz znr-csllwrl, khuzsvozp s gsqz-noshgwhg jzno blzsfjolrkgo qzshj jr vsez joz yushzj. Kharljkhsjzut, joz guwjnozv wh ozl glzzh plzsq jklhzp joz nrqysht'v cslzorkvzv whjr ewljksu vskhsv. Wj csv uwfz Qrjozl Hsjklz nskgoj cwhp ra s orj hzc jlzhp – cslzorkvz vysv. Nkz joz syrnsutyvz lzqwx. Glzzhushp'v wnz qzujzp asvjzl josh sh wnz nlzsq nrhz wh joz Vsosls. Gurbsu cslqwhg czhj alrq 'Rryv, W uzaj joz jozlqrvjsj jrr owgo' jr 'Pwp vrqzrhz ikvj vzj joz Zsljo rh 'Blrwu'?' Znrvtvjzqv csezp grrpbtz uwfz jozt czlz brslpwhg s vysnzvowy jr hrcozlz. Nrsvjsu nrqqkhwjwzv grj owj oslpzl josh s ywhsjs sj s bwljopst ysljt. Okqshv asnzp joz glwq lzsuwjt ra 'Rryv, cz pwph'j vzz josj nrqwhg.' Zhjzl Mzkv, joz nzuzvjwsu OL qshsgzl, aklwrkv sj jowv nrlyrlsjz-vyrhvrlzp nosrv. Owv pwewhz whjzlezhjwrh csv uzvv 'clsjo ra joz grpv' shp qrlz 'lzvzjjwhg joz yushzj uwfz s guwjnot ewpzr gsqz.' Wj vzzqv zezh grpv nsh'j lzvwvj s nrvqwn pr-rezl cozh joz qrljsuv qzvv ky joz Zsljo'v KW.", "", "Nlwqzv ra Lowshhz Ushm:", "Wj csv Lowshhz’v awlvj tzsl ra crlfwhg sv s akuu-jwqz hklvz. Voz csv awhwvowhg ozl arkljo jczuez orkl vowaj wh s lrc, shp csv azzuwhg lsjozl bzsj prch. Voz csv azzuwhg ysljwnkuslut jwlzp bznskvz voz osp jr pzsu cwjo qkno qrlz yrry josh voz cshjzp jr. Voz csv uzsewhg joz orvywjsu shp csv urrfwhg arlcslp jr ozl yrvj-crlf hsy rh joz nrkno. Vkppzhut, s hrjwawnsjwrh yryyzp ky rh ozl yorhz lzqwhpwhg ozl ra s bzgwhhzl rkjprrl nuwqbwhg nuwhwn josj voz csv vnozpkuzp jr jzsno josj hwgoj. “Hrrrrr” voz zxnuswqzp. Voz urezp jzsnowhg, bkj voz lzsuut csvh’j azzuwhg ky jr wj. Voz bzglkpgwhgut plrez jr Vdksqwvo jr jzsno joz nuwhwn. Pzvywjz orc jwlzp voz csv, voz qzj joz ysljwnwyshjv cwjo s vqwuz rh ozl asnz. Kharljkhsjzut, voz csv vr jwlzp josj voz arlgrj jr jzsno joz vjkpzhjv orc jr bzust zsno rjozl, shp whvjzsp ikqyzp jr vkggzvjwhg s nuwqb jr jlt. Joz vjkpzhjv czlz nrhakvzp bt joz usnf ra whvjlknjwrhv, bkj czlz jrr vot jr vst shtjowhg, vr jozt jwzp jozqvzuezv whjr joz lryz (whnrllznjut, W qwgoj spp). Lowshhz pwph’j hrjwnz ozl qwvjsfz shp zezh vjsljzp jr hrp raa jr vuzzy cowuz joz vjkpzhjv vjsljzp jr nuwqb. Vkppzhut, Lowshhz csv scrfzh bt s vnlzsq shp s ozset jokp. Rhz ra ozl vjkpzhjv osp asuuzh jr joz glrkhp. Joz vjkpzhj csv lkvozp jr joz orvywjsu, jozt vkaazlzp jcr blrfzh shfuzv shp s ozajt nrhnkvvwrh bkj jozt czlz grwhg jr bz rfst. Lowshhz rh joz rjozl oshp, urvj ozl irb sv s gkwpz, shp csv ykhwvozp arl ozl hzguwgzhnz. Voz suvr urvj ozl hzcut sndkwlzp hklvwhg uwnzhnz."]


    alphabet_new_order = []
    for i in alphabet_upper:
        alphabet_new_order.append(code_dict[i][1])


    text_lines_translated = []
    for i in range(len(text_lines)):
        text_lines_translated.append('')
        line = text_lines[i]
        for j in range(len(line)):
            if (line[j] in alphabet_upper):
                letter_idx = code_dict[line[j]][1]
                letter_new = alphabet_upper[letter_idx]
                text_lines_translated[i] = text_lines_translated[i] + letter_new

            elif (line[j] in alphabet_lower):
                letter_idx = code_dict[line[j].upper()][1]
                letter_new = alphabet_lower[letter_idx]
                text_lines_translated[i] = text_lines_translated[i] + letter_new

            else:
                text_lines_translated[i] = text_lines_translated[i] + line[j]


    print('Translation:')
    print()

    for i in range(len(text_lines_translated)):
        print(text_lines_translated[i])
