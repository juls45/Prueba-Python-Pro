meme_dict= {"CRINGE":"Algo raro o embarazoso",
    "OMG":"significa Oh My God, que significa ¡Oh Dios mío!,
    "BTW":"significa By The Way, que significa por cierto,
    "YOLO":"significa You Only Live Once (solo se vive una vez).",
    "SIMP":"Persona que actúa de forma demasiado sumisa para ganar la atención",
}

word= input("Escribe una palabra que no entiendas(¡Con Mayusculas!):")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("No existe esa palabra")
