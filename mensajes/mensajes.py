import pickle
import datetime


# Importo los datos


datos_fallecidos = open("fallecidos.pickle", "rb")

fallecidos_pandemia = pickle.load(datos_fallecidos)
fallecidos_primera = pickle.load(datos_fallecidos)
fallecidos_segunda = pickle.load(datos_fallecidos)
fallecidos_semana = pickle.load(datos_fallecidos)
fallecidos_fecha = pickle.load(datos_fallecidos)

datos_fallecidos.close()


datos_casos = open("casos.pickle", "rb")

casos_totales = pickle.load(datos_casos)
casos_totales_dia = pickle.load(datos_casos)
casos_araba_dia = pickle.load(datos_casos)
casos_bizkaia_dia = pickle.load(datos_casos)
casos_gipuzkoa_dia = pickle.load(datos_casos)
casos_no_euskadi = pickle.load(datos_casos)
incidencia_euskadi = pickle.load(datos_casos)
incidencia_araba = pickle.load(datos_casos)
incidencia_bizkaia = pickle.load(datos_casos)
incidencia_gipuzkoa = pickle.load(datos_casos)
fecha_actualizacion = pickle.load(datos_casos)

datos_casos.close()


datos_planta = open("planta.pickle", "rb")

ingresos_euskadi_dia = pickle.load(datos_planta)
ingresos_araba_dia = pickle.load(datos_planta)
ingresos_bizkaia_dia = pickle.load(datos_planta)
ingresos_gipuzkoa_dia = pickle.load(datos_planta)

datos_planta.close()


datos_uci = open("uci.pickle", "rb")

uci_euskadi_dia = pickle.load(datos_uci)
uci_araba_dia = pickle.load(datos_uci)
uci_bizkaia_dia = pickle.load(datos_uci)
uci_gipuzkoa_dia = pickle.load(datos_uci)

datos_uci.close()


# Urls con más información para incluir en los mensajes de restricciones, prevención y síntomas

url_restricciones = "https://www.euskadi.eus/ultimas-medidas-vencer-al-coronavirus/web01-a3covid/es/"
url_prevencion = "https://www.euskadi.eus/recomendaciones-para-prevenir-la-transmision-del-coronavirus/web01-a2korona/es/"
url_sintomas = "https://www.euskadi.eus/preguntas-sobre-la-enfermedad/web01-a3korona/es/"

# Urls de los gráficos para incluir en los mensajes de las cifras

url_gincidencia = "https://public.flourish.studio/visualisation/4392821/"
url_gfallecidos = "https://public.flourish.studio/visualisation/4393132/"
url_ghospitales = "https://public.flourish.studio/visualisation/4393075/"

# Mensajes

saludo_m = "Kaixo! Me llamo <b>Ko</b> y soy un 🤖!\nMi especialidad es el coronavirus. Cada día te ofreceré los datos actualizados sobre la evolución de la pandemia en Euskadi.\n\n<b>¿En qué te puedo ayudar?</b>"

ayuda_m = "¿En qué te puedo ayudar?"

casos_m = ["Desde que comenzó la pandemia, en Euskadi se han notificado <b>{} casos</b>. En las últimas horas, la comunidad suma <b>{}</b>. Por territorios: {} en Araba, {} en Bizkaia, {} en Gipuzkoa y {} con residencia fuera de la comunidad.\n\n¿Sabes qué es la incidencia acumulada? Es la proporción de personas que se contagian en un periodo de tiempo concreto. Si la incidencia acumulada durante 14 días supera los 500 casos, se considera que la transmisión del virus es alta. A día de hoy, Euskadi tiene una incidencia de <b>{} casos por 100.000 habitantes</b>. Araba, de {}, Bizkaia, de {} y Gipuzkoa, de {}.\n\nActualización datos: {}.\n\n<a href='{}'>Evolución de la incidencia acumulada en los últimos 30 días</a>".format(casos_totales, casos_totales_dia, casos_araba_dia, casos_bizkaia_dia, casos_gipuzkoa_dia, casos_no_euskadi, incidencia_euskadi, incidencia_araba, incidencia_bizkaia, incidencia_gipuzkoa, fecha_actualizacion, url_gincidencia),
    "En las últimas horas, Euskadi suma 1.243 casos nuevos. Por territorios: 139 en Araba, 572 en Bizkaia, 527 en Gipuzkoa y cinco de personas con residencia fuera de la comunidad. Durante el fin de semana, Osakidetza no actualiza indicadores como la incidencia, por lo que el lunes te podré ofrecer más datos sobre la evolución de la pandemia.\n\nActualización datos: 2020/XX/XX.\n\n <a href='{}'>Evolución de la incidencia acumulada en los últimos 30 días</a>".format(url_gincidencia)]

hospitales_m = ["A día de hoy hay <b>485 pacientes</b> en planta en los diferentes hospitales de la red de Osakidetza. En las últimas horas, han ingresado <b>{} personas</b>, {} en Araba, {} en Bizkaia y {} en Gipuzkoa.\n\n<b>137 pacientes</b> permanecen en las Unidades de Cuidados Intensivos. En las últimas horas han ingresado <b>{} personas</b>, {} en Araba, {} en Bizkaia y {} en Gipuzkoa.\n\nActualización datos: {}.\n\n<a href='{}'>Evolución de la situación de los hospitales durante la segunda ola</a>".format(ingresos_euskadi_dia, ingresos_araba_dia, ingresos_bizkaia_dia, ingresos_gipuzkoa_dia, uci_euskadi_dia, uci_araba_dia, uci_bizkaia_dia, uci_gipuzkoa_dia, fecha_actualizacion, url_ghospitales),
    "En las últimas horas, 87 personas con Covid-19 han ingresado en planta, y en las Unidades de Cuidados Intensivos hay actualmente 146 pacientes con coronavirus. Durante el fin de semana, Osakidetza no actualiza el detalle de los ingresos hospitalarios y en UCI, por lo que el lunes te podré ofrecer más datos sobre la evolución de estos indicadores.\n\nActualización datos: 2020/XX/XX.\n\n<a href='{}'>Evolución de la situación de los hospitales durante la segunda ola</a>".format(url_ghospitales, url_ghospitales)]

fallecidos_m = "Los fallecimientos totales ascienden en Euskadi a <b>{}</b>. Durante la primera ola muerieron en la comunidad {} personas y en la segunda, {}. La semana anterior fallecieron {} personas.\n\nEstos datos reflejan los decesos registrados hasta {}. Osakidetza actualiza esta cifra cada miércoles, publicando los datos de la semana anterior.\n\n<a href='{}'>Evolución del número de fallecidos durante la segunda ola</a>".format(fallecidos_pandemia, fallecidos_primera, fallecidos_segunda, fallecidos_semana, fallecidos_fecha, url_gfallecidos)

restricciones_m = "Estas son las últimas restricciones aprobadas:\n\n🌃 Límite a la movilidad entre las 22.00 y hasta las 06.00.\n\n🛒 Cierre de todos los comercios, a excepción de farmacias y gasolineras, a las 21.00.\n\n⛪ Reducción del aforo en los centros de culto al 35%.\n\n🍔 Cierre de bares y restaurantes. Solo podrán abrir los que sirvan comida a domicilio.\n\n🎭 Toda actividad, espectáculo o evento cultural debe terminar antes de las 21.00.\n\n🎰 Cierre de los establecimientos de juego y apuestas.\n\n<a href='{}'>Aquí encontrarás más información sobre los detalles normativos y sobre estas y otras restricciones vigentes</a>.".format(url_restricciones)

prevencion_m = "Evitar situaciones de riesgo, el cumplimiento de las medidas de seguridad sanitarias (uso correcto de mascarilla y lavado de manos frecuente) y mantener la distancia social son las principales claves para la prevención de contagios.\n\n<a href='{}'>Aquí encontrás más información</a>.".format(url_prevencion)

sintomas_m = "Los síntomas más comunes incluyen fiebre, tos, dolor de garganta, pérdida de olfato o gusto y sensación de falta de aire. Algunos pacientes también pueden presentar dolores, congestión nasal o diarrea. En caso de tener síntomas compatibles con la Covid-19 debes ponerte en contacto por teléfono con tu centro de salud o llamar al Consejo Sanitario (900 203 050).\n\n<a href='{}'>Aquí encontrarás más información sobre como actuar</a>.".format(url_sintomas)


# En función de que día de la semana sea se publicará uno o otro mensaje sobre la evolución de los casos, la incidencia y la situación en los hospitales

dias = {"lunes": 0, "martes": 1, "miércoles": 2, "jueves": 3, "viernes": 4, "sábado": 5, "domingo": 6}
dia = datetime.datetime.now()

if (dia == dias["sábado"]) | (dia == dias["domingo"]):
    casos_m = casos_m[1]
    hospitales_m = hospitales_m[1]
else:
    casos_m = casos_m[0]
    hospitales_m = hospitales_m[0]


# Exportación mensajes completos


archivo = open("../mensajes.pickle",'wb')

pickle.dump(saludo_m, archivo)
pickle.dump(ayuda_m, archivo)
pickle.dump(casos_m, archivo)
pickle.dump(hospitales_m, archivo)
pickle.dump(fallecidos_m, archivo)
pickle.dump(restricciones_m, archivo)
pickle.dump(prevencion_m, archivo)
pickle.dump(sintomas_m, archivo)

archivo.close()

