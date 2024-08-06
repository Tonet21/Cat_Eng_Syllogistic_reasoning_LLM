# -*- coding: utf-8 -*-

sylloExamples = [('actuari', 'escultor', 'escriptor'), ('assistent', 'poeta', 'científic'),
                 ('atleta', 'assistent', 'chef'), ('químic', 'bussejador', 'ballarí'), 
                 ('químic', 'treballador', 'pintor'), ('administratiu', 'carnisser', 'atleta'), 
                 ('ballarí', 'banquer', 'genet'), ('doctor', 'genet', 'inversor'), 
                 ('bussejador', 'grum', 'químic'), ('pagès', 'surfista', 'escriptor'),
                 ('jugador', 'netejador', 'model'), ('golfista', 'ciclista', 'assistent'),
                 ('caçador', 'analista', 'nedador'), ('corredor', 'actor', 'fuster'),
                 ('lingüista', 'cuiner', 'model'), ('lingüista', 'patinador', 'cantant'),
                 ('gestor', 'administratiu', 'carnisser'), ('miner', 'caixer', 'poeta'),
                 ('model', 'sastre', 'florista'), ('infermer', 'erudit', 'comprador'),
                 ('planificador', 'mariner', 'enginyer'), ('genet', 'agent', 'cambrer'),
                 ('genet', 'novel·lista', 'lingüista'), ('corredor', 'òptic', 'administratiu'),
                 ('científic', 'novel·lista', 'florista'), ('patinador', 'perruquer', 'cuiner'),
                 ('estudiant', 'caixer', 'metge'), ('estudiant', 'excursionista', 'disenyador'),
                 ('surfista', 'pintor', 'grum'), ('terapeuta', 'excursionista', 'òptic')]


wordType = {"S": "subject",
            "M": "middle",
            "P": "predicate"}


class Figure:
    def __init__(self, type=None):
        self.figureType = type
        if type == 1:
            self.major = ["M", "P"]
            self.minor = ["S", "M"]

        elif type == 2:
            self.major = ["P", "M"]
            self.minor = ["S", "M"]

        elif type == 3:
            self.major = ["M", "P"]
            self.minor = ["M", "S"]

        elif type == 4:
            self.major = ["P", "M"]
            self.minor = ["M", "S"]


class Mood:
    linkMapping = {"A": "Tots els ",
                   "E": "No tots els ",
                   "I": "Alguns ",
                   "O": "Alguns ",
    }
    postVerbLink = {"A": "",
                    "E": "",
                    "I": "",
                    "O": " no"}

    def __init__(self, links):
        self.links = links
        self.majorLink = links[0]
        self.minorLink = links[1]

class Syllogism:
    def __init__(self, figure, mood, syllowords):
        self.figure = Figure(figure)
        self.mood = Mood(mood)
        self.subject = syllowords[0]
        self.middle = syllowords[1]
        self.predicate = syllowords[2] 
      
    def generate(self):
        allSentences = []
        for sentence in ("major", "minor"):
            sOut = ""
            linkage = getattr(self.mood, sentence + "Link")
            linkWord = self.mood.linkMapping[linkage]
            linkWord = linkWord.capitalize()
            sOut += linkWord
            sFormat = getattr(self.figure, sentence)
            wt = wordType[sFormat[0]]
            sOut += getattr(self, wt)
            sOut += " are "
            sOut += self.mood.postVerbLink[linkage]
            wt = wordType[sFormat[1]]
            sOut += getattr(self, wt)

            allSentences.append(sOut)
        return allSentences, self.figure.figureType

def generateAll():
    all_generated_syllogisms = []
    possible_conclusions = []
    for terms in sylloExamples:
        for i in range(1, 5):
            for a in "AEIO":
                for b in "AEIO":         
                         s = Syllogism(i, a + b, terms)
                         syllogism = s.generate()[0] + [a + b] + [s.generate()[1]]
                         all_generated_syllogisms.append(syllogism)
                         choices = [f"""Tots {terms[0]} són {terms[2]}""",
                          f"""No tots els {terms[0]} són {terms[2]}""",
                          f"""Alguns {terms[0]} són {terms[2]}""",
                          f"""Alguns {terms[0]} no són {terms[2]}""" ]
                         possible_conclusions.append(choices)



    return all_generated_syllogisms, possible_conclusions

syllogisms = generateAll()[0]
possible_conclusions = generateAll()[1] 




