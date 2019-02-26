import xbmc,xbmcgui,xbmcaddon

SKINS = [["Blue", "Blue"],["Blue (Left Align Channels)", "BlueLeft"]]


d = xbmcgui.Dialog()
names = [s[0] for s in SKINS]
skin = d.select("TV Guide Fullscreen - Set Default Skin", names)
if skin > -1:
    tvgf = xbmcaddon.Addon("script.tvguide.fullscreen")
    if tvgf:
        tvgf.setSetting('skin.source', '2')
        tvgf.setSetting('skin.folder', 'special://home/addons/script.tvguide.fullscreen.skin.blue/')
        tvgf.setSetting('skin.user', SKINS[skin][1])
        
        tvgf.setSetting('epg.video.pip', 'true')
        tvgf.setSetting('program.image.scale', 'true')      

        tvgf.setSetting('logos.enabled', 'false')
        tvgf.setSetting('channel.logo', 'true')        
        
        tvgf.setSetting('program.background.image.source', '0')
        tvgf.setSetting('program.background.texture.url', 'special://home/addons/script.tvguide.fullscreen.skin.blue/resources/skins/Blue/media/primary.jpg')

        tvgf.setSetting('action.bar', 'false')