from PIL import Image
from random import randint

imagensGeradas = []

def gerarImagem(nomeImagem):
    dados = []
    dados.append(str(randint(1,7)))
    dados.append(str(randint(1,4)))
    dados.append(str(randint(1,4)))
    dados.append(str(randint(1,5)))
    dados.append(str(randint(1,8)))
    dados.append(str(randint(1,7)))


    valida = dados[0] + "|" + dados[1] + "|" + dados[2] + "|" + dados[3] + "|" + dados[4] + "|" + dados[5]
    strNomeImagem = dados[0] + dados[1] + dados[2] + dados[3] + dados[4] + dados[5]

    if valida in imagensGeradas:
      print(str(strNomeImagem) + " Imagem com a combinação (" + valida + ") já existe")
      gerarImagem(valida)
    else:
      background = Image.open("FundoCor/" + dados[0] + ".png")
      skin =       Image.open("FundoDesenho/" + dados[1] + ".png")
      cosmetico =  Image.open("Base/" + dados[2] + ".png")
      mascote =  Image.open("Mascote/" + dados[3] + ".png")
      cabeca =  Image.open("Cabeca/" + dados[4] + ".png")
      rosto =  Image.open("Rosto/" + dados[5] + ".png")

      background.paste(skin, (0, 0), skin)
      background.paste(cosmetico, (0, 0), cosmetico)
      background.paste(mascote, (0, 0), mascote)
      background.paste(cabeca, (0, 0), cabeca)
      background.paste(rosto, (0, 0), rosto)
      background.save("image/" + str(strNomeImagem) + ".png")

      imagensGeradas.append(strNomeImagem)

for x in range(7777):
  gerarImagem(x)