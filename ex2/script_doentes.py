import json
from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, OWL

g = Graph()
g.parse("med_tratamentos.ttl", format="turtle")

ont = Namespace("http://www.example.org/disease-ontology#")

with open("a93318.json", "r", encoding="utf-8") as f:
    patients_data = json.load(f)

for patient_data in patients_data:
    patient_name = patient_data["nome"].strip()
    symptoms = patient_data["sintomas"]

    patient_id = URIRef(ont[patient_name.replace(" ", "_").replace("'", "").replace(".", "").replace(",", "") + "_ID"])
    patient_instance = ont[patient_id]

    if (patient_instance, RDF.type, ont.Patient) not in g:
        g.add((patient_instance, RDF.type, ont.Patient))
        g.add((patient_instance, ont.name, Literal(patient_name)))

    for symptom in symptoms:
        symptom_instance = URIRef(ont[symptom.replace(" ", "_")])
        if (symptom_instance, RDF.type, ont.Symptom) not in g:
            g.add((symptom_instance, RDF.type, ont.Symptom))
        g.add((patient_instance, ont.exhibitsSymptom, symptom_instance))

g.serialize(destination="med_doentes.ttl", format="turtle")

