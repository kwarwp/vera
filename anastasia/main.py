# vera.anastasia.main.py
from _spy.vitollino.main import Cena,Elemento,Texto
DESERTO ="https://png.pngtree.com/element_origin_min_pic/16/11/04/115952b377d509665b7fa1cf8d7f2636.jpg"
HELICOPTERO ="https://www.camacarrodobrasil.com.br/media/catalog/product/cache/1/image/800x/9df78eab33525d08d6e5fb8d27136e95/1/_/1_8_2.png"
MAXSTEEL ="https://vignette.wikia.nocookie.net/deathbattle/images/3/3a/Max_Steel.png/revision/latest?cb=20170108031649"
MULAN ="https://banner2.kisspng.com/20180402/arw/kisspng-kingdom-hearts-ii-fa-mulan-mushu-fa-zhou-mulan-5ac267c8892643.1162809115226899925618.jpg"
DESERTO1 ="https://png.pngtree.com/element_origin_min_pic/16/11/04/115952b377d509665b7fa1cf8d7f2636.jpg"
POVOADO ="http://1.bp.blogspot.com/-htYcMr2Nosc/VkpiGpxkl5I/AAAAAAADbss/IIDw74TnKPA/s640/b_450_0_16777215_00_archivos_Administradores_Maur%25C3%25ADcio_2015-11_161115_assad_siria.png"
def inicio():
    deserto=Cena(img=DESERTO)
    deserto1=Cena(img=DESERTO1)
    povoado=Cena(img=POVOADO)
    deserto.direita=deserto1
    deserto1.direita=povoado
    povoado.esquerda=deserto1
    
    helicoptero=Elemento(img=HELICOPTERO,tit="Helicoptero",style=dict(left=150,top=160,width=160,height=200))
    helicoptero.entra(deserto)
    ehelicoptero=Texto(deserto,"Esse é o deserto de townsville, e dentro desse helicóptero está ngm menos q o super herói MaxSteel, o q ele não sabe eh que uma 10graça tá p acontecer, o helicóptero vai cair!")
    helicoptero.vai=ehelicoptero.vai
    
    maxsteel=Elemento(img=MAXSTEEL,tit="MaxSteel",style=dict(left=150,top=160,width=160,height=200))
    maxsteel.entra(deserto1)
    emaxsteel=Texto(deserto1,"Caramba, meu helicoptero caiu, macacos me mordam! Estou perdido nessa caralhaa")
    maxsteel.vai=emaxsteel.vai
    
    mulan=Elemento(img=MULAN,tit="Mulan",style=dict(left=150,top=160,width=160,height=200))
    mulan.entra(povoado)
    emulan=Texto(povoado,"Pow man, tu eh muito burro, sai de perto dos terroristas que eles vão te meter bala, chegai q vou te ajudar.")
    mulan.vai=mulan.vai
    
    
    deserto.vai()
inicio()    