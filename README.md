# SQL & NoSQL Database Systems Project

Portfolio project demonstrating three database paradigms through Python applications built with **SQLite**, **Neo4j**, and **Elasticsearch**.

The project was developed for a university Big Data / Database Systems course and has been reorganized to make the technologies, data models, and query patterns easy to review.

## Technologies

- Python
- SQLite / SQL
- Neo4j / Cypher
- Elasticsearch

## Repository structure

```text
Big-Data-Project/
├── README.md
├── requirements.txt
├── .gitignore
└── src/
    ├── driving_school_sqlite.py
    ├── sports_federation_neo4j.py
    └── course_reviews_elasticsearch.py
```

## 1. Relational database — SQLite

`src/driving_school_sqlite.py`

Models the operations of a driving school using a relational schema with entities for licence categories, candidates, instructors, vehicles, lessons, and exams.

The implementation demonstrates:

- primary and foreign keys;
- referential-integrity constraints;
- `CHECK` constraints;
- inserts and relational queries;
- aggregations and joins;
- creation of a local SQLite database from Python.

SQLite is included in Python's standard library, so no separate package installation is required.

## 2. Graph database — Neo4j

`src/sports_federation_neo4j.py`

Models a sports federation as a graph containing cities, competitions, teams, athletes, and coaches.

Example relationships include:

```text
(Team)-[:BASED_IN]->(City)
(Athlete)-[:BELONGS_TO]->(Team)
(Athlete)-[:PARTICIPATES_IN]->(Competition)
(Coach)-[:COACHES]->(Team)
```

The project demonstrates:

- graph modelling;
- temporal relationship properties;
- Cypher queries;
- direct and indirect graph relationships;
- graph traversal and aggregation.

A local Neo4j instance is required to run this script.

## 3. Document search and analytics — Elasticsearch

`src/course_reviews_elasticsearch.py`

Indexes synthetic student course-review documents and demonstrates document-oriented search and analytics.

The queries include:

- BM25 text relevance;
- fuzzy matching;
- Boolean keyword queries;
- result highlighting;
- phrase matching;
- date and numeric filters;
- significant-text analysis;
- aggregations.

A local Elasticsearch instance is required to run this script.

## Installation

Create a virtual environment and install the external dependencies:

```bash
pip install -r requirements.txt
```

Then run the desired example, for instance:

```bash
python src/driving_school_sqlite.py
```

The Neo4j and Elasticsearch examples additionally require their respective local services to be running.

## Data

All example records used in the project are synthetic and were created for educational purposes.

## What this project demonstrates

Rather than focusing on a single database technology, this repository compares how different data models support different use cases:

| Paradigm | Technology | Main strength demonstrated |
|---|---|---|
| Relational | SQLite | structured schemas, constraints, joins |
| Graph | Neo4j | relationships and traversal |
| Document / search | Elasticsearch | full-text search and aggregations |

## Possible improvements

- move large synthetic seed datasets into separate data files;
- read service credentials from environment variables;
- add Docker Compose for Neo4j and Elasticsearch;
- add automated integration tests.
