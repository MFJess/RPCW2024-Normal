import csv
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, OWL

g = Graph()
g.parse("medical.ttl", format="turtle")

ont = Namespace("http://www.example.org/disease-ontology#")

symptoms_data = {}
with open("./csvs/Disease_Syntoms.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader) 
    for row in reader:
        disease = row[0].strip()
        symptoms = [symptom.strip() for symptom in row[1:] if symptom.strip()]
        symptoms_data[disease] = symptoms

descriptions_data = {}
with open("./csvs/Disease_Description.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader) 
    for row in reader:
        disease = row[0].strip()
        description = row[1].strip()
        descriptions_data[disease] = description

for disease, symptoms in symptoms_data.items():
    disease_instance = ont[disease.replace(" ", "_")]
    if (disease_instance, RDF.type, ont.Disease) not in g:
        g.add((disease_instance, RDF.type, ont.Disease))
    
    for symptom in symptoms:
        symptom_instance = ont[symptom.replace(" ", "_")]
        if (symptom_instance, RDF.type, ont.Symptom) not in g:
            g.add((symptom_instance, RDF.type, ont.Symptom))
        g.add((disease_instance, ont.hasSymptom, symptom_instance))
    
    if disease in descriptions_data:
        description = descriptions_data[disease]
        g.add((disease_instance, ont.hasDescription, Literal(description)))

g.serialize(destination="./med_doencas.ttl", format="turtle")
