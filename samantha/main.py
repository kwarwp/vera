# vera.teacher.main.py
from _spy.vitollino.main import Cena,STYLE, Texto,INVENTARIO
from elemento.main import Elemento
STYLE["width"] = 900
STYLE["height"] = "600px"
LETRA_A = "https://i.imgur.com/sFciRzA.jpg"
LETRA_B = "https://i.imgur.com/IHu7zVe.jpg"
LETRA_C = "https://i.imgur.com/KDkL6Lg.jpg"
LETRA_D = "data:image/png;base64,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"
LETRA_E = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAVFBMVEX///8AAADHx8fm5ub4+Pg6Ojq4uLhTU1OwsLDBwcHg4OCenp5paWnk5OTAwMBYWFjW1takpKQZGRk8PDzMzMw0NDTv7++GhoZoaGgqKiqQkJBFRUURnOwzAAABb0lEQVR4nO3dW1JCMRRFQbxyEZCHCPhi/vN0BPxI4j6V6jWDrlS+cpIsFpIkSZIkSUO0f67XftlS+FSxt+GFp/3owtctISFhOkJCwnyEhIT5CAkJ8xESEuYjJCTMR0hImI+QkDAfISFhPsJ/Er4fX3p1qiE8X6ZeHWoI56npcFa3CAnrR0hYP0LC+hES1o+QsH6EhPUjvN91vW1+Le+jlLBHn8MLd5fRhV+b0YU7QkLCeISEhPkICQnzERIS5iMkJMxHSEiYj5CQMB8hIWE+QsL6wlrn+PNq3bzVoZRw6vEWeC3h6FNfhFUiJKwfIWH9CAnrR0hYP0LC+hES1o+QsH6E9zt3uA3Zo78Lv3/Wq25NFYRdOw8vnDfNNnmacqf5MLxw/DUkJCSMR0hImI+QkDAfISFhPkJCwnyEhIT5CAkJ8xESEuYjJCTMN77w2k54u80VO7abp1lsu/2X+lANhcuiNQNKkiRJkiRJkiSpUb//7HDnUkOgZwAAAABJRU5ErkJggg=="
LETRA_F = "https://i.imgur.com/IcWkooX.jpg"
LETRA_G = "https://i.imgur.com/zGx2uSc.jpg"
LETRA_H = "https://i.imgur.com/naC6Wq3.jpg"
LETRA_I = "https://i.imgur.com/3X7JyD5.jpg"
LETRA_J = "https://i.imgur.com/N5yr7lF.jpg"
LETRA_K = "https://i.imgur.com/0PyUE7j.jpg"
LETRA_L = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAANlBMVEX///8BAQF2dnbKysry8vIoKCjX19cEBARTU1P8/PzHx8fj4+POzs5sbGy8vLwhISEwMDDv7++qWkgEAAABH0lEQVR4nO3dS07DQBRFQTsETIDw2f9mYQNYQmq5fUTVCu7RG/aglwUAAAAAAAAAgFN4fdrxdp09b4D7uud99rwBLuv2u/Vl9rwBLrs3fJg9bwCFfQr7FPYp7FPYp7BPYZ/CPoV9CvsU9insU9insE9hn8I+hX0K+xT2KexT2KewT2Gfwj6FfQr7FPYp7FPYp7BPYZ/CPoV9CvsU9insU9insE9hn8I+hX0K+xT2KexT2KewT2Gfwj6FfQr7FPYp7FPYp7BPYZ/CPoV9Cvv+d+H2U3gbYrmds3Ad+N/TvMT9wo/HUZ5PWjiOQoUKFSpUqFChQoUKFSpUqFChQoUKR9gmFt4PKVzXz2mF14N8TSs8ysSHCwAAAAAAAACAv/gGswkiWt35aZwAAAAASUVORK5CYII="
LETRA_M = "https://st3.depositphotos.com/1561359/12648/i/950/depositphotos_126487082-stock-photo-silver-letter-m.jpg7"
LETRA_N = "https://2.bp.blogspot.com/-sOuJ1fO6Hxo/VzIz2wmQftI/AAAAAAAAHMg/ZyEAuVjdtg0SeK7l8aHdVMnsOSlZEduLwCPcBGAYYCw/s1600/letra-n.jpg"
LETRA_O = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw8SEhUTERAVEhUVFRUXFRAVFxIVEhUVFxEWGBgVFRUYHSggGBolGxUWIT0hJSkrLi4uFx8zODMsNygtLisBCgoKBQUFDgUFDisZExkrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrK//AABEIAOEA4QMBIgACEQEDEQH/xAAcAAEAAQUBAQAAAAAAAAAAAAAABwECBQYIBAP/xABEEAACAQIBCAYIBAQCCwAAAAAAAQIDBBEFBgcSITFBURMiYXGBkRQyQlJigqGxcpKiwSMk0eEzwjRDRFNjhJOjsrPS/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AJxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC2U0t7wAuBj7rLdrTTc68Ipb25RSMVVz9yVHfe0fCab8kBsoNUjpEyS/wDbKf6v6Hutc8cm1PUu6T+dL7gZ0HyoXNOaxhOMlzTT+x9QAAAAAAAAAAAAAAAAAAAAAAAAAB8ru5p0oSqVJqEIrGU5NKKXNsD6mEzhzrsrKONxWSfCmts34Ii/PnS7KWtRyfjGO1O4eyT/AALgu1kT3V1Uqyc6k3OT3ybxYEqZwaZ60242lFU1wnPrS78FsX1NDypnVlC421bqo0/ZUnGPkjBRPogKTeO1tt83tPmz6NFmqBQJjVYwA9lllW4ovGlWnB84yaN3ze0tX9FqNZ9PDjrJOWHfsf1I8wAHT2bWftleRxjNRa9ZY+r+LjFdrWHazaotPatq5nHdCrOElKEpQktqnFuMk+aa2okPM/SncW2ELhdJD3ls/NFbPGOHapAdBAxmQcu295TVShNSXGOKxXlw7TJgAAAAAAAAAAAAAAAAACyrUjGLlJqMYptyexJJYtt8gPNlbKdG2pSrV5qFOCxcn9Elxb3YHOef+flfKNRxTdO3i+pRT3/FUw3y+iPRpLz1nlGtqU21bU21Tju13u6SXfw5I0lxAsCL9UuUALIozmbubV3ez1Lak54etPdTj2yk9i+74Yma0dZi1Mo1NaWMLeD69TjJ79SHb28F4J9DZLybQtqUaVCmqcI7or7t723ze1gRjkXQrRSTu7mUnxhRSjFdmvJNvyRs9vovyNFbbXX7ZVKuP0kkbkANRq6M8jNf6Gl2qpWx/wDIwGVtDNjNN29apRlwUsKkPLY/qSaAOZM68wb6xxlUp69PhWp9aHzcYvvS7MTVXA7DqU4yTjJKSawcWk0096ae9ELaT9HCoqV1Zx/h76lBbdT4ofD2cO7cES4DVL2gBkM3svXNlVVWhNxwe2Psy5po6NzHzwoZSo68OrUjgqtHjF81zizmEymbeXK1jcQuKL2xfWh7M48Yy7GB1eDHZv5Zo3lCFxReMZrdxjLjF9qZkQAAAAAAAAAAAAAARPptzpcYqwoywlNKVdreoezT+be+xLmSZljKMLahUr1PVpwcn24LYl2t4LxOXcp31S4rVK9V4zqycpdmO5LsSwXgB4OjGqfXApgB81EyWbuRKl3cU7envqSwcuEYrbKT7Ek2eLAmTQdkPVp1bya2zfR0+yMcHNrvlgvkYEj5GyXStaMKFGOrCEcFzfOT5tvb4ntAAAAAAABSUU001insae1NcmVAHOelHNT0G5xpr+DWxlT+F49aHg2vBo0o6X0l5CV3Y1El16S6WD44xTxXjHHxwOapICzAFWMAJB0O50u1ufR6kv4Nw0ljuhV9mXYnufgdAHH8ceHDidO6P8vem2VKq3jUS1Kv444Jt96wfiBsYAAAAAAAAAAAACMtOOVnC3pW0XtrSc5/gp4YJ98mn8pCzN30v33S5RnHHFUoQpr8uu/rI0hgWgqACOo818mq2tKFHDBwpxUvxtYyf5mznXM+y6a9tqb2qVaGK+FSUpfRM6eAAAAAAAAAAACjWO85bzvyX6PeV6OGyFSSj+FvGP6WmdSkE6abLUv1NL/FpQk32xbh9oxAjjUGofZopgBZqEnaDMrOncVbZvq1Ya8V8dPel3xb/KiNcDNZm33QX1tVxwwqwT/DJ6sv0yYHToAAAAAAAAAAAADmLPG46S+uZ869TDuU2l9EjDM9eVJ61ao+dSb85M8jAoAAN00RUNfKdJ+5GrL/ALbj/mOgyDNCFJO+nL3aEsPGcCcwAAAAAAAAAAAESadqG21nzVWL8HBr7slsjbThTi7WjJraqrSffHb9kBCTLUXtFoAvi2nit/BliLkB1dZVtenCfvQjLzin+59zGZsSxs7Z87ei/OlEyYAAAAAAAAAAAcpZRjhVmuU5L9TPMzK50UNS8uIe7Wqr9bwMSwKANhMCRtB0/wCeqL/gS/8AZAnIgXQtVwyjh71GovJxl+xPQAAAAAAAAAAACMtOkv5e3XOrL6Q/uSaRVp2qdS1j8VV+Sgv3AiBlpcyjAoXItPpTji0lvb3doHUGbUMLO2XK3orypRMkfGzpalOEPdhGPlFI+wAAAAAAAAAAAc96V7Hoso1XhsqKNRfNFJ/qTNNaJf06ZMxjQuUtzlSk+/rQ+0yIsALMAkXMpiBtOjK56PKdu+EpSh+enKK+rR0acp5Mu3RrU6q306kJr5ZKX7HVVKopJSi8U0mnzTWKYFwAAAAAAAAAAEMacrnG5oU8fUpOX55tf5CZznfSff8ATZRrtPFU2qS+SKUl+fWA1MoXFoAzOaFl017bU9+tWhj+GMtaX0TMOSHoUyZ0l5Os11aFN4P46nVX6dfyAnEAAAAAAAAAAAABhc8sj+l2dailjJxxh+OPWj5tYeJzNJYbGdZkAaWM3vRbx1IxwpXGM48lPHrx83j8wGksoGUAuOidF+V1c5PpYvGVJdFP5EtX9Oqc6o3zRFnEra76GcsKdxhHF7o1U+o/HFx8VyAnoFsZYlwAAAAAAALak1FYsDxZbylC2oVK091OEptc8FsXi8F4nL9xXlOUpyeMpScpPm28W/NkpaZs4urCzg9smqlbDhFf4cH49bwiRPiBUoCqAqkdBaK8iejWMXJYTrvpZc0muovy4P5mRJo8zc9Ou4wlHGlTwnWfDVT2Q+Z7O7HkdFpAVAAAAAAAAAAAAADB55Zuwv7aVGWCl61Ofu1Etj7ntT7GZwAcoZQs6lGpOlVi4ThJxlF8GjzMnzSZmOr2HT0ElcQW7d0sV7L+JcH4csIFrU5Rk4yTjJNpxawaaeDTXBgWYlylhtWwtAE76Ps8/S6KjOX8xSilNP8A1sVs6RdvPt7ze7a6jNbHt4rijlWxvKlGcalKbhOLxUlvX9iU828+6VdKNaSoVt2tupzfNP2X2MCXgalRzgrw9ZKoufHzR7rbOaEng6cl2rb+wGfBib/LkKaTjCU8eODS82jD18468vUioLnx+oGz3V3CmsZSw5Li+5GpZ0Z1Qt6TrVO1UqOO2cuHhzZrOXc8KFDHGfT1uEE8Un8UuH3Ixy1levdVHUrSxe5RWyMV7sVwQHxyhfVK9WdWrLWnOTlJ9r5LguGHYebEoAKn0tKFSpONOEXOcmoxgtrk28EkWU4OTSim22kopNttvBJJb23wJ10ZZh+hxVzcxTuJLqw2NUYtbu2b4vhuXFsM7mHmxHJ9sqex1Z4SrTXGeHqp+7HcvF8TZAAAAAAAAAAAAAAAAAABo2f+j2lfJ1aLVK5S9b2KuG5VMNz+Lzx2YbyAOUMrZLr2tV0rinKlNezLivei90l2rYeM6py7kK1vKfR3NKNSO3BvZKLfGElti+4iDOnRDdUm52M1cU9r6GbUa67E9kZ8fde7YwI3TLky66sbilJwq0alOS3xnCcX5NfU87k1vTAy9jlu6o7KdacV7uOMfJ7DOZP0h39J4ro5Pm4f0Zp8Ize6En3Js+qta73Uaj+Sf9AN4yjpSyhWjquNGPaoyx+sjWb7L93W2VK0sPdXVj5R3nhjk66e62rvuo1X9on0jke+e6yun/y9f/5A8xTEydPNfKct1hc/9Govuj3Wej/LFV4KynH4qjp00vCUk/JAa5ievJWTK91VVG3pSq1H7MVsS96T3Rj2vYSVm9oYm2pX9wkv9zQxbffVklh3KPiSpkXItraU+itqMaUeOqtsnznJ7ZPtbYGr5gaPaVilVrata5w9f2KWK2xp48eGs9r7FsN4AAAAAAAAAAAAAAAAAAAAAAAAAAFNVcioAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//2Q=="
LETRA_P = "data:image/png;base64,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"
LETRA_Q = "http://oracc.museum.upenn.edu/qcat/images/Q.png"
LETRA_R = "https://3.bp.blogspot.com/-f4OnzUCj1zg/VzI3ccy7XEI/AAAAAAAAHNE/uAUnW6QI2ZUvtspy7Sty_pZXw39tOfBggCPcBGAYYCw/s1600/letra-r.jpg"
LETRA_S = "https://moldesde.com/wp-content/uploads/2012/02/letra_18.png.jpg"
LETRA_T = "https://image.freepik.com/icones-gratis/t-letra-maiuscula_318-966.jpg"
LETRA_U = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFeB_lFaybGxv_13iOo42xVN2cIWE6hUYLoa7LHyAmP8QogAGn"
LETRA_V = "https://images.casashops.com/Square620NoGrow/22625/alfabet-letra-v-preto-h-17-x-w-18%2C5-x-d-1%2C5-cm.jpg"
LETRA_W = "https://s3.amazonaws.com/img.cdm/letra-w-decorativa-preta-mdf-223x19-cm-Carro-de-Mola-M-uIBRH.jpg"
LETRA_X = "https://images.casashops.com/square1168/22627/alfabet-letra-x-preto-h-17-x-w-18%2C5-x-d-1%2C5-cm.jpg"
LETRA_Y = "https://images.casashops.com/Square620NoGrow/22628/alfabet-letra-y-preto-h-17-x-w-18%2C5-x-d-1%2C5-cm.jpg"
LETRA_Z = "data:image/jpeg;base64,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"

CENA_PARQUE = "https://i.imgur.com/bPDwwQO.jpg"
CENA_CRIANCA = "https://i.imgur.com/hKFY2DF.png"
UMTEXTO = "Monte uma palavra, use sua criatividade"

class Crianca: 
    def __init__(self, parque, tit="joana", x=400, y=470):
        tit=input("escreva seu nome")
        self.parque, self.tit = parque, tit
        escolhas = {"letra_a" : self.a, "letra a": self.a}
        crianca = Elemento(CENA_CRIANCA, tit=tit, x=x, y=y, w=100, h=100, drop=escolhas, style={"opacity":0.2})
        crianca.entra(parque)
        crianca.vai = self.a
        
    def a (self, _):
        texto = Texto (self.parque, UMTEXTO)
        texto.vai()
    
class JogoLetra:
    def __init__(self): 
        parque = Cena (CENA_PARQUE)
        INVENTARIO.inicia()
        self.letra_a = Elemento(LETRA_A,tit="A", x=540, y=470, w=90, h=20, drag=True,vai=self.clicounaletra)
        self.letra_a.entra(parque)
        self.letra_b = Elemento(LETRA_B,tit="B", x=500, y=250, w=20, h=30, drag=True,vai=self.clicounaletra)
        self.letra_b.entra(parque)
        self.letra_c = Elemento(LETRA_C,tit="C", x=400, y=240, w=20, h=30, drag=True,vai=self.clicounaletra)
        self.letra_c.entra(parque)
        self.letra_d = Elemento(LETRA_D,tit="D", x=250, y=250, w=20, h=30, drag=True,vai=self.clicounaletra)
        self.letra_d.entra(parque)
        self.letra_e = Elemento(LETRA_E,tit="E", x=20, y=230, w=20, h=30, drag=True,vai=self.clicounaletra)
        self.letra_e.entra(parque)
        self.letra_f = Elemento(LETRA_F,tit="F", x=50, y=195, w=35, h=30, drag=True,vai=self.clicounaletra)
        self.letra_f.entra(parque)
        self.letra_g = Elemento(LETRA_G,tit="G", x=450, y=255, w=40, h=30, drag=True,vai=self.clicounaletra)
        self.letra_g.entra(parque)
        self.letra_h= Elemento(LETRA_H,tit="H", x=790, y=195, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_h.entra(parque)
        self.letra_i = Elemento(LETRA_I,tit="I", x=550, y=195, w=50, h=30, drag=True,vai=self.clicounaletra)
        self.letra_i.entra(parque)
        self.letra_j = Elemento(LETRA_J,tit="J", x=600, y=195, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_j.entra(parque)
        self.letra_k = Elemento(LETRA_K,tit="K", x=650, y=205, w=25, h=30, drag=True,vai=self.clicounaletra)
        self.letra_k.entra(parque)
        self.letra_l = Elemento(LETRA_L,tit="L", x=350, y=210, w=20, h=30, drag=True,vai=self.clicounaletra)
        self.letra_l.entra(parque)
        self.letra_m = Elemento(LETRA_M,tit="M", x=700, y=180, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_m.entra(parque)
        self.letra_n = Elemento(LETRA_N,tit="N", x=420, y=190, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_n.entra(parque)
        self.letra_o = Elemento(LETRA_O,tit="O", x=90, y=500, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_o.entra(parque)
        self.letra_p = Elemento(LETRA_P,tit="P", x=750, y=555, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_p.entra(parque)
        self.letra_q = Elemento(LETRA_Q,tit="Q", x=500, y=100, w=35, h=30, drag=True,vai=self.clicounaletra)
        self.letra_q.entra(parque)
        self.letra_r = Elemento(LETRA_R,tit="R", x=650, y=400, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_r.entra(parque)
        self.letra_s = Elemento(LETRA_S,tit="S", x=150, y=410, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_s.entra(parque)
        self.letra_t = Elemento(LETRA_T,tit="T", x=200, y=475, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_t.entra(parque)
        self.letra_u = Elemento(LETRA_U,tit="U", x=110, y=225, w=40, h=30, drag=True,vai=self.clicounaletra)
        self.letra_u.entra(parque)
        self.letra_v = Elemento(LETRA_V,tit="V", x=555, y=400, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_v.entra(parque)
        self.letra_w = Elemento(LETRA_W,tit="W", x=225, y=200, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_w.entra(parque)
        self.letra_x = Elemento(LETRA_X,tit="X", x=700, y=450, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_x.entra(parque)
        self.letra_y = Elemento(LETRA_Y,tit="Y", x=200, y=100, w=35, h=30, drag=True,vai=self.clicounaletra)
        self.letra_y.entra(parque)
        self.letra_z = Elemento(LETRA_Z,tit="Z", x=250, y=105, w=35, h=30, drag=True,vai=self.clicounaletra)
        self.letra_z.entra(parque)
        Crianca(parque, tit="joana")
        self.mapa=dict(A=self.letra_a,B=self.letra_b,C=self.letra_c,D=self.letra_d,E=self.letra_e,F=self.letra_f,
          G=self.letra_g,H=self.letra_h,I=self.letra_i,J=self.letra_j,K=self.letra_k,L=self.letra_l,
          M=self.letra_m,N=self.letra_n,O=self.letra_o,P=self.letra_p,Q=self.letra_q,R=self.letra_r,
          S=self.letra_s,T=self.letra_t,U=self.letra_u,V=self.letra_v,W=self.letra_w,X=self.letra_x,Y=self.letra_y,Z=self.letra_z)
        parque.vai()
    def clicounaletra(self,ev):
        INVENTARIO.bota(self.mapa[ev.target.id])
JogoLetra()
