meme_dict = {
            "STEVE": "Sizin 2 Minecraft karakterinizden birisi",
            "ALEX": "Sizin 2 Minecraft karaktrinizden birisi",
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(meme_dict[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("bu kelimeyi henüz biz de bilmiyoruz :( ")
