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
            "NETHER": "Minecraft'daki cehennem boyutudur. 'NEDIR' diye okunur.",
            "NEDIR": "Minecraft'daki cehennem boyutudur. 'NETHER' diye yazılır.",
            "PİGLİN": "Size hasar vermeye çalışan canavar. Üzerinde zırh ve kılıç gibi ekipmanlar olabilir. Güneşe çıktıklarında yanarlar.",
            "BLAZE": "Size hasar vermeye çalışan canavar. Uçabilirler. Ateş topu atarlar. Bılayz diye okunur. Blaze çubuğu düşürürler.",
            "BILAZE": "Size hasar vermeye çalışan canavar. Uçabilirler. Ateş topu atarlar. Blaze diye yazılır. Bılayz diye okunur. Blaze çubuğu düşürürler.",
            "BILAYZ": "Size hasar vermeye çalışan canavar. Uçabilirler. Ateş topu atarlar. Blaze diye yazılır. Blaze çubuğu düşürürler.",
            "GHOST": "Size hasar vermeye çalışan canavar. Uçabilirler. Ateş topu atabilirler. Gast diye okunur.",
            "NETHER PORTALI": "Nether'a gitmeni sağlayan portal. x9 Obsidiyen ve bir çakmaktaşı ve çelik gerekir.",
            "END": "Oyunun sonunun olduğu yer.",
            "END PORTALI": "End'e gitmeni sağlayan portal. Açmak için max. x10 ender gözü.",
            "ENDER İNCİSİ": "Fırlattığın yere ışınlanmanı sağlayan cisim.",
            "ENDER GÖZÜ": "Stronghold bulmana yardımcı olan ve end portalını açmana yarayan cisim.",
            "ENDERMAN": "Gözüne bakınca sana hasar vermeye çalışan canavar. Öldürmek için 2 blokluk bir alana girmelisiniz. Ender incisi düşürür.",
            "ENDER DRAGON": "Oyunu bitirmek için öldürmen gereken canavar.", 
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(meme_dict[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("bu kelimeyi henüz biz de bilmiyoruz :( ")
