#Prova da disciplica Optativa
#Aluno: Anderson pereira da silva, RA: 407560


#comandos de instalação
# pip install SpeechRecognition
# pip install pyaudio
# pip install pyttsx3
# pip install pypiwin32
# 

import speech_recognition as sr
import pyttsx3

# Pega o audio do microfone
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Fale algo!")
#     audio = r.listen(source)

try:
    print('analisando...')
    # strAudio = r.recognize_google(audio,None,"pt-BR")
    # print(strAudio);

    strAudio = "A  Universidade  Estadual  de  Londrina,  por  meio  do  SEBEC–Serviço de  Bem-Estar  à  Comunidade-Divisão  de  Serviço  Social, PROEX –Pró-Reitoria  de Extensão,  Cultura  e  Sociedade, Prograd –Pró-Reitoria  de  Graduaçãoe PROPPG –Pró-Reitoria  de  Pesquisa  e  Pós-Graduação, de  acordo  com  aChamadaPública 08/2020da Fundação Araucáriatornam públicosas normas e critériosestabelecidosneste  edital parao Processo  de Seleção Socioeconômica(Item  6) e  Acadêmica (Item  7)de  estudantes  cotistasda  UEL,para  as  bolsasdoPrograma  Institucional  de Apoio àInclusão  Social –Pesquisa  e  Extensão  Universitária 2020daFundação Araucária, a saber:I -A  partir  das 10hdo  dia 18/06/2020até  as  23h59do  dia 24/06/2020, receberá inscriçõespor  meio   de   Formulário   disponível   exclusivamente   via   internet,   no endereço eletrônico http://www.uel.br/inclusaosocial,de estudantes cotistas da UEL interessados em  concorrer  ao Processo  de  Seleção  Socioeconômica  e  Acadêmica para obtenção de Bolsa de inclusão Social da Fundação Araucária.II –A efetivação da inscrição será permitida somentepara estudantes cotistas da UEL que atendam ositens 3 e 7.2 deste edital. III-Antes de efetuar a inscrição, o candidato deverá tomar conhecimento do presente edital,   o   qual   estabelece   as   normas e   critérios de   caráter   classificatório   e eliminatório do Processo de SeleçãoSocioeconômica e Acadêmica.IV–Avigência da bolsa prevista neste edital será definidasomentea partir da data de assinaturado   Convênio   a   ser   celebrado   entre   a   Fundação   Araucária   e   a Universidade Estadual de Londrina.1.Objetivosdo Pr ogr am a1.1Incentivar    a   for m ação   de   r ecur sos   hum anos   par a pr ojetos   de pesquisa,  ensino  e  extensão  univer s i tár ia,  dir ecionadas  a  tem as  de inter esse social;1.2F avor ecer    o   acesso   e   a   integr ação   à   cultur a   acadêm ica   dos  estudantes  ingr essantes  no  ensino  super ior   por   m eio  do  sistem a de cotas;1.3 Pr om over   a  in ser ção  dos  e stud antes  em   atividades   científ icas,  extensionistas, tecno lógicas e/ou ino v ação."    
    engine = pyttsx3.init()
    engine.say(strAudio) #converte o texto para audio;
    engine.runAndWait()
except sr.UnknownValueError:
    print("Google Speech não reconheceu o audio")
except sr.RequestError as e:
    print("Não foi possivel fazer a requisão para o google speech; {0}".format(e))