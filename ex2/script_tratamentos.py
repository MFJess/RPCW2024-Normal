import csv
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, OWL

g = Graph()
g.parse("./med_doencas.ttl", format="turtle")

treatments_data = {}
with open("./csvs/Disease_Treatment.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader) 
    for row in reader:
        disease = row[0].strip()
        treatments = [treatment.strip() for treatment in row[1:]]
        treatments_data[disease] = treatments

ont = Namespace("http://www.example.org/disease-ontology#")

for disease, treatments in treatments_data.items():
    for treatment in treatments:
        treatment_instance = ont[treatment.replace(" ", "_")]
        if (treatment_instance, RDF.type, OWL.Class) not in g:
            g.add((treatment_instance, RDF.type, OWL.Class))
        g.add((treatment_instance, RDF.type, ont.Treatment))
        for d in g.subjects(RDF.type, ont.Disease):
            if disease.replace(" ", "_") in str(d):
                g.add((d, ont.hasTreatment, treatment_instance))

g.serialize(destination="./med_tratamentos.ttl", format="turtle")