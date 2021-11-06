import jieba

__RAW_CN__ = ['我操',
              '你妈死了', 'NMSL', ' NM$L', 'nmzl', 'nm$l',
              '傻逼', '伞兵', '申必', '啥b', 'sb', '杀币', '煞笔'
              'nt', '脑瘫',
              'esu', '恶俗', '户籍', '身份证号']

__RAW_EN__ = ['fuck',
              'idolt',
              'sexy',
              'your mother dead']

__ERROR__ = ['Err0: Invalid Mode',
             'Err1: Invalid word list']

def text_check(text:str, mode:int):
    if mode == 1:
        split = jieba.lcut_for_search(text)
        for s in range(len(split)):
            for cn in range(len(__RAW_CN__)):
                if split[s] == __RAW_CN__[cn]:
                    return True
                else:
                    return False
    elif mode == 2:
        for en in range(len(__RAW_EN__)):
            if __RAW_EN__[en] in text:
                return True
            else:
                return False
    else:
        return __ERROR__[0]
    pass

def text_check_self(text:str, raws:list):
    if not isinstance(raws, list):
        return __ERROR__[1]

    rlist = str(raws)
    for raw in range(len(rlist)):
        if rlist[raw] in text:
            return True
        else:
            return False

if __name__ == '__main__':
    print(text_check('You', 2))