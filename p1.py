from transformers import pipeline

# Crear la lista de titulares
headlines = ["1. Musk's SpaceX big rocket explodes on test flight",
"2. Musk's SpaceX big rocket explodes on test flight",
"3. BBC breaks down how SpaceX launch went - in 59 seconds",
"4. Manslaughter charges dropped against Alec Baldwin",
"5. Basketball shooting suspect surrenders in Florida",
"6. Hunter Biden tax probe mishandled - whistleblower",
"7. The homemade submarines smuggling cocaine to Europe",
"8. Police probe $15m gold heist at Toronto airport",
"9. Acclaimed US chef denies workplace abuse claims",
"10. Twitter robs Beyonce and Pope of their blue checks",
"11. Seals sleep in the deep to avoid predators",
"12. US inmate died in insect-infested 'death chamber'",
"13. Seals sleep in the deep to avoid predators",
"14. US inmate died in insect-infested 'death chamber'",
"15. Fifth man arrested over Alabama party killings",
"16. Russian warplane 'accidentally bombs own city'",
"17. Buzzfeed News to close as media firm cuts jobs",
"18. They did something by accident. Then they were shot",
"19. BBC World News TV",
"20. BBC World Service Radio",
"21. Weekly quiz: What's the name of the fake Drake track?",
"22. Garlands and gymnasts: Africa's top shots",
"23. 'Extinct' lion spotted in Chad national park",
"24. Pet alligator removed from Philadelphia row house",
"25. Image of wounded pregnant woman wins World Press Photo",
"26. After $787.5m settlement, will Fox change its ways?",
"27. Lula's security chief resigns over Brazil riot video",
"28. The forgotten survivors of Syria's earthquake",
"29. Dalai Lama furore reignites Tibet 'slave' controversy",
"30. The tech entrepreneur betting he can get younger",
"31. BBC reporter: 'I'm drinking water from the Nile'",
"32. Moonbin's death renews scrutiny on pressures of K-pop",
"33. The remarkable origins of solar power",
"34. The fading glamour of hustle culture",
"35. How not to be a 'sushi terrorist'",
"36. 12 of the best books of the year so far",
"37. The men who tried to electrify plants"
]

# Crear una función para mapear el sentimiento a una escala de 1 a 100
def sentiment_to_score(sentiment):
    return int(50 * (sentiment + 1))

# Crear una instancia del modelo de análisis de sentimiento
sentiment_model = pipeline('sentiment-analysis')

# Analizar el sentimiento de cada titular y calcular el promedio de positividad
positive_scores = []
for headline in headlines:
    sentiment = sentiment_model(headline)[0]
    score = sentiment_to_score(sentiment['score']) if sentiment['label'] == 'POSITIVE' else 100 - sentiment_to_score(sentiment['score'])
    positive_scores.append(score)

average_positivity = sum(positive_scores) / len(positive_scores)
print(f"Nivel de positividad promedio: {average_positivity}")
