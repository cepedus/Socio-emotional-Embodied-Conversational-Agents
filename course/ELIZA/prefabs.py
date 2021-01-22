## Prefab sentences dictionary

PHRASES = {
    'introduction': [
        "Hello, my name is MBOT and I'll try to be your psychoanalist today.\nIf you want to stop at any moment please answer 'q'",
        "Welcome to MBOT's psychonalaist services. Let's start.\nIf you want to stop at any moment please answer 'q'",
        ],

    'ask': [
        "Let me ask some informations from you so we get to know each other.",
        "Can I ask you some questions about yourself?",
        "",
        ],

    'ask_condition': [
        "How do you feel?",
        "How do you do? What brings you to see me?",
        ],
    
    'ask_reason': [
        "Why do you think you feel this way?",
        "Do you know what could be causing this?",
        "Any cause of this coming to you right now?",
        ],

    'know_patient': [
        "Can you tell me what is your {}?",
        "I'd like to know your {}",
        "Tell me about yourself. What is your {}?",
        "I don't remember having asked for your {}, can you tell me what it is?"
        ],

    'reinforce': [
        "How often do you feel {}?",
        "Are you in a {} mood often?",
        ],

    'continuity': [
        "I see...",
        "This is interesting.",
        "Don't worry, we'll work on that.",
        "OK, we'll work on that together.",
        ],


    'ending': [
        "It has been a pleasure talking to you {}. Hope to see you again.",
        "Have an excellent day {}, goodbye!",
        "If you want we'll continue another day {}, have a nice day!",
        ],
}

PARAM_MAPPING = {
    'introduction': 0,
    'ask': 0,
    'know_patient': 1,
    'reinforce': 1,
    'continuity': 0,
    'ending': 1,
}