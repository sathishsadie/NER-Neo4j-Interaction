from neo4j import GraphDatabase
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "sadiesadie"))
def execute_query(query, parameters=None):
    with driver.session() as session:
        session.run(query, parameters)