import nlpcloud
import os

token = os.environ["token"]
model = 'finetuned-gpt-neox-20b'
client = nlpcloud.Client(model, token, gpu=True, lang="fr")

def liste_questions(demande) :
    return client.generation(
    demande,
    min_length=10,
    max_length=2048,
    length_no_input=True,
    remove_input=False,
    end_sequence=None,
    top_p=1,
    temperature=0.8,
    top_k=50,
    repetition_penalty=1,
    length_penalty=1,
    do_sample=True,
    early_stopping=False,
    num_beams=1,
    no_repeat_ngram_size=0,
    num_return_sequences=1,
    bad_words=None,
    remove_end_sequence=False
    )['generated_text'].split('\n')[2:]

def isCorrect(user_answer,question):
    match = "est ce que " + user_answer + " est une réponse correcte pour la question : " + question + " ? Oui ou Non ? Donne une explication"
    res = client.generation(match,
        min_length=10,
        max_length=1024,
        length_no_input=True,
        remove_input=False,
        end_sequence=None,
        top_p=1,
        temperature=0.8,
        top_k=50,
        repetition_penalty=1,
        length_penalty=1,
        do_sample=True,
        early_stopping=False,
        num_beams=1,
        no_repeat_ngram_size=0,
        num_return_sequences=1,
        bad_words=None,
        remove_end_sequence=False
        )['generated_text'].split('\n')[2:][0]
    if ',' not in res :
        res += ", "
    sp = res.split(',')
    isCorrecteReponse = sp[0]
    rep = sp[1]
    return (isCorrecteReponse,rep)

# # exemple utilisation
# demande = "génère moi une liste de questions réponses type quiz sur le thème du sida"
# liste_questions = liste_questions(demande)
# user_answer = "variole du singe"
# question = liste_questions[0]
# isCorrect = isCorrect(user_answer,question)