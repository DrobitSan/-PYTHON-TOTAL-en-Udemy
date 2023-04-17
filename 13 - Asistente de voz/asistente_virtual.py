import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#voces distintas
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'



#   ESCUCHAR MICRO Y DEVOLBER TEXTO
def audio_a_texto():

    # almacenar recognizer en variable
    r= sr.Recognizer()

    # configurar microfono
    with sr.Microphone() as origen:
        
        # delay de inicio
        r.pause_threshold = 0.8

        # informar del comienzo de la grabacion
        print('Escuchando...')

        audio = r.listen(origen)

    try:
        # buscar en google
        pedido = r.recognize_google(audio, language='es-es')
        print('Has dicho:' + pedido)
        return pedido

    except sr.UnknownValueError:    #en caso de no comprender al audio
        print('No te he entendido')
        return 'Esperando todavia...'

    except sr.RequestError:     # en caso de no devolber pedido
        print('Parece que no hay servicio')
        return 'Esperando todavia...'
    
    except:     #error inesperado
        print('Algo ha salido mal')
        return 'Esperando aun'


#  funcion para que el sistente pueda ser escuchado
def hablar(mensaje):
    #encender motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    #  pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


#informar del dia de la semana
def pedir_dia():
    dia= datetime.datetime.today()
    dia_semana= dia.weekday()
    
    semana= {0: 'Lunes',
    1: 'Martes',
    2: 'Miercoles',
    3: 'Jueves',
    4: 'Viernes', 
    5: 'Sabado',
    6: 'Domingo'}

    hablar(f'Hoy es {semana[dia_semana]}')


#informar_hora
def pedir_hora():
    hora= datetime.datetime.now()
    hora= f'En este momento son las {hora.hour} horas, {hora.minute} minutos y {hora.second} segundos.'

    hablar(hora)


# funcion saludo inicial
def saludo_inicial():
    hora= datetime.datetime.now()
    if hora.hour > 19 or hora.hour <= 4:
        saludo= 'Buenas noches'   
    elif hora.hour >= 5 or hora.hour < 13:
        saludo= 'Buenos dias'
    else:
        saludo= 'Buenas tardes'

    hablar(f'{saludo}, soy Helena, tu asistente personal, dime en que te puedo ayudar')


def pedir_cosas():

    saludo_inicial()

    encendido= True

    while encendido:
        pedido = audio_a_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Por supuesto, abriendo youtuber')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, abriendo el navegador')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=2)
            hablar('Wikipedia dice lo siguiente')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            pedido = pedido.replace('busca en internet', '')
            hablar(f'Buscando {pedido} en internet.')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Comenzando a reproducir')
            pedido= pedido.replace('reproducir', '')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            print(accion)
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL',
                       'tesla': 'TSLA'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'El precio de la accion de {accion} es {precio_actual} dólares por acción')
                continue
            except:
                hablar('Lo siento, no la he encontrado')
                continue
        elif 'adiós' in pedido:
            hablar('Por fin un descanso, me voy')
            break 


pedir_cosas()



#pywhatkit.sendwhatmsg_instantly("+34622244175", "Hola")
