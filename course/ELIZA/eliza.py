import numpy as np
from pprint import pprint
import pandas as pd
from utils import User, get_input, format_, parse_condition, parse_reason
from prefabs import PHRASES, PARAM_MAPPING


def main():

    print(np.random.choice(PHRASES['introduction']))
    print(np.random.choice(PHRASES['ask']))

    _, name = get_input('What is your name?')
    patient = User(name)
    print(f'Welcome {patient}')

    historic_feelings = []
    historic_frequencies = []
    historic_causes = []

    in_therapy = True
    while True:
        diagnose_message = np.random.choice(PHRASES['ask_condition'])
        in_therapy, raw_condition = get_input(diagnose_message)
        if not in_therapy:
            break

        condition = parse_condition(raw_condition)
        patient.diagnose = condition
        historic_feelings.append(condition)

        print(np.random.choice(PHRASES['continuity']))

        missing_info = patient._unknowns()
        if len(missing_info) != 0:
            know_patient_message = np.random.choice(PHRASES['know_patient'])
            know_patient_message = format_(know_patient_message, missing_info[0])
            in_therapy, new_info = get_input(know_patient_message)
            if not in_therapy:
                break
            setattr(patient, missing_info[0], new_info)

        reinforce_message = np.random.choice(PHRASES['reinforce'])
        reinforce_message = format_(reinforce_message, condition)
        in_therapy, freq = get_input(reinforce_message)
        if not in_therapy:
            break
        historic_frequencies.append(freq)

        reason_message = np.random.choice(PHRASES['ask_reason'])
        in_therapy, reason = get_input(reason_message)
        if not in_therapy:
            break
        patient.reason = reason
        historic_causes.append(parse_reason(reason))

        print(np.random.choice(PHRASES['continuity']))

        new_message = f'Previously you said that you felt {np.random.choice(historic_feelings)}. Do you want to tell me something else?'
        in_therapy, new_info = get_input(new_message)
        if not in_therapy or 'n' in new_info:
            break
    

    if len(historic_feelings) == len(historic_frequencies) and len(historic_feelings) == len(historic_causes):
        print('Before we leave, I would like you to know what I noted:')
        for i in range(len(historic_frequencies)):
            feel_i = historic_feelings[i]
            freq_i = historic_frequencies[i]
            caus_i = historic_causes[i]
            if 'you' not in caus_i:
                caus_i = 'of ' + caus_i
            print(f"You've been feeling {feel_i} {freq_i}, because {caus_i}")

    end_message = np.random.choice(PHRASES['ending'])
    end_message = format_(end_message, patient.name)
    print(end_message)
    
    return 









if __name__=="__main__":
    main()
    
