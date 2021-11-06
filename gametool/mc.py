import os

def anti_client_hack(mode:str, path:str):
    __MODPATH__ = path + r'\mods'
    __DXD__ = path + r'\DXD_mods'
    __GGL__ = path + r'\game\GGL'

    if mode == 'Mods':
        mods_hack = [r'\LiquidBounce - 1.8', r'\LiquidBounce - 1.12', r'\141Sense - 1.8', r'\FDPClient - 1.8']
        for i in range(len(mods_hack)):
            if os.path.exists(__MODPATH__ + mods_hack[i]):
                return True
            else:
                return False

    if mode == 'Netease':
        if os.path.exists(__DXD__):
            return True
        elif os.path.exists(__GGL__):
            return True
        else:
            return False