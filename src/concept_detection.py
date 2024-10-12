from neo4j_connector import execute_query
def create_entity_nodes(entities):
    for entity in entities:
        label = ""
        if entity["label"] == "PERSON":
            label = "Person"
        elif entity["label"] == "ORG":
            label = "Organization"
        elif entity["label"] == "GPE":
            label = "Location"
        elif entity["label"] == "CONCEPT":
            label = "Concept"
        
        query = f"""
        MERGE (n:{label} {{name: $name}})
        """
        parameters = {"name": entity["text"]}
        execute_query(query, parameters)
def create_relationship(subject, object, relationship):
    query = """
    MATCH (s {name: $subject_name})
    MATCH (o {name: $object_name})
    MERGE (s)-[:RELATIONSHIP {name: $relationship}]->(o)
    """
    parameters = {
        "subject_name": subject,
        "object_name": object,
        "relationship": relationship
    }
    execute_query(query, parameters)