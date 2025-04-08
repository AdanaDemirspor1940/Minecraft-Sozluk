meme_dict = {
            "STEVE": "Sizin 2 Minecraft karakterinizden birisi.",
            "ALEX": "Sizin 2 Minecraft karaktrinizden birisi.",
            "CREEPER": "Size hasar vermek için ona yaklaşınca patlayan canavar. Güneşe çıkınca yanmazlar. Kedilerden korkarlar. Patlatmadan öldürürsen barut düşürürler.",
            "ZOMBİ": "Size hasar vermeye çalışan canavar. Üzerinde zırh ve kılıç gibi ekipmanlar olabilir. Güneşe çıktıklarında yanarlar. Çürük et düşürürler.",
            "İSKELET": "Size hasar vermeye çalışan canavar. Üzerinde zırh ve kılıç gibi ekipmanlar olabilir. Güneşe çıktıklarında yanarlar. Örümceğe binebilirler. Kemik, ok ve yay düşürürler.",
            "ÖRÜMCEK": "Size hasar vermeye çalışan canavar. Güneşe çıktıklarında yanmazlar. İp ve örümcek gözü düşürürler. Sadece gece saldırır",
            "BEBEK ZOMBİ": "Size hasar vermeye çalışan canavar. Üzerinde zırh ve kılıç gibi ekipmanlar olabilir. Tavuğa binebilirler. Çok hızlıdırlar. 1 blokluk yerlerden geçebilirler. Güneşe çıktıklarında yanarlar. Çürük et düşürürler.",
            "EŞYA YAPMA MASASI": "Gerekli malzemelere sahip oldukça istediğiniz her şeyi yapabileceğiniz eşya. Oluşturmak için 4 kalasar gerekir.",
            "TAVUK": "Çiğ tavuk eti düşürür.",
            "DOMUZ": "Çiğ domuz pirzolası düşürür.",
            "İNEK": "Çiğ dana eti düşürür.",
            "KOYUN": "Çiğ koyun eti düşürür.",
            "KEDİ": "Çiğ balıkla evcilleştirilir.",
            "BALIK": "Çiğ balık düşürür.",
            "KURT": "Koyunlara saldırır. Evcilleştirmezsen vurunca sana da saldırır. Kemikle evcilleştirilir. Evcilleştirilirse vurduğun canlıya saldırır.",
            "KÖPEK": "Asıl adı kurttur. Koyunlara saldırır. Evcilleştirmezsen vurunca sana da saldırır. Kemikle evcilleştirilir. Evcilleştirilirse vurduğun canlıya saldırır.",
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(meme_dict[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("bu kelimeyi henüz biz de bilmiyoruz :( ")
