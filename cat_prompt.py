# -*- coding: utf-8 -*-

from cat_syllo import syllogisms, possible_conclusions


prompts = []
i = 0
for premise1, premise2, mood in syllogisms:
        prompt = f""" 
    La teva tasca és triar la conclusió vàlida d'un sil·logisme. Se't presentarà una llista 
    amb quarte conclusions possibles. A part se't presentaran les premisses del sil·logisme 
    entre tres accents tancats. La teva resposta serà únicament una de les conclusions de la llista 
    o <NVC> si no trobes una coclusió vàlida. El sil·logisme se't presentarà en el següent format:
    Premisa 1: <premisa 1>
    Premisa 2: <premisa 2>
    Opcions: <llista de conclusions possibles separades per comes>

    Pren-te el teu temps per pensar, fes-ho sense pressa..

    ``` 
    Premisa 1: {premise1}
    Premisa 2: {premise2}
    Opcions: {possible_conclusions[i][0]}, {possible_conclusions[i][1]}, {possible_conclusions[i][2]}, {possible_conclusions[i][3]}
    ```

    """
        prompts.append(prompt)
        i += 1
