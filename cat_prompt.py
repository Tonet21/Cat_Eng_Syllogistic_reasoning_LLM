# -*- coding: utf-8 -*-
from cat_syllo import syllogisms, possible_conclusions

system_message = f"""La teva tasca consisteix en avaluar un sil·logisme i triar la conclusió vàlida d'una llista amb quatre opcions.
                     Se't presentaran dues premises i quatre conclusions possibles seguint el següent format:

                     Premisa 1: <premisa 1>
                     Premisa 2: <premisa 2>
                     Opcions: <llista de quatre opcions separades per comes>

                     La teva resposta ha de ser una de les opcions presentades o "NVC" si cap de les opcions no és vàlida.
                     No necessites donar més explicacions, la resposta hauria de ser unicament l'opció que has triat.
                     Pren-te el teu temps per arribar a la resposta correcta, no necessites precipitar-te.
                     """
prompts = []
i = 0
for premise1, premise2, mood, type_ in syllogisms:
        prompt = f"""

                    Premisa 1: {premise1}
                    Premisa 2: {premise2}
                    Opcions: {possible_conclusions[i][0]}, {possible_conclusions[i][1]}, {possible_conclusions[i][2]}, {possible_conclusions[i][3]}

    """
        prompts.append(prompt)
        i += 1
