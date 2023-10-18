
has_symptom(john, fever).
has_symptom(john, cough).
has_symptom(john, sore_throat).
has_symptom(jane, headache).
has_symptom(jane, fatigue).
has_symptom(jane, runny_nose).


diagnose(Patient, Disease) :-
    has_symptom(Patient, fever),
    has_symptom(Patient, cough),
    has_symptom(Patient, sore_throat),
    Disease = 'Common Cold'.
    
diagnose(Patient, Disease) :-
    has_symptom(Patient, headache),
    has_symptom(Patient, fatigue),
    has_symptom(Patient, runny_nose),
    Disease = 'Influenza (Flu)'.

diagnose(_, 'Unknown').


diagnosis(Patient, Disease) :-
    has_symptom(Patient, _), % Ensure the patient has at least one symptom
    diagnose(Patient, Disease).


