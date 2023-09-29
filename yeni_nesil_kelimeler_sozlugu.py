meme_dict={
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL" : "Bir şakaya karşılık cevap",
    "SHEESH" : "Onaylamamak",
    "CREEPY" : "Korkunç",
    "AGGRO" : "Agresifleşmek/sinirlenmek",
    "CRUSH" : "Söyleyen kişinin hoşlandığı biri",
    "FAKE" : "Sahte"
}

while True:
    word=input("Anlamadığınız bir kelime yazınız. (Büyük harflerle):")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Aradığınız sözcük maalesef sözlükte bulunmuyor.")
