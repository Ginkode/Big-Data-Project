# SQL & NoSQL Database Systems

Three small Python projects built for a university database course, each using a different data model: **SQLite**, **Neo4j**, and **Elasticsearch**.

I kept the projects together because the useful part is the comparison: the same Python workflow changes substantially depending on whether the data are relational, graph-based, or document-oriented.

## Projects

| Script | Technology | What it covers |
|---|---|---|
| `src/driving_school_sqlite.py` | SQLite / SQL | schema design, PK/FK constraints, checks, joins and aggregations |
| `src/sports_federation_neo4j.py` | Neo4j / Cypher | graph modelling, temporal relationships, traversal and indirect connections |
| `src/course_reviews_elasticsearch.py` | Elasticsearch | indexing, BM25 search, fuzzy matching, filters, highlighting and aggregations |

All records used in the examples are synthetic.

## SQLite: driving school

The relational example models licence categories, candidates, instructors, vehicles, lessons and exams. The schema uses foreign keys and `CHECK` constraints, then runs queries and aggregations on the generated database.

Run it with:

```bash
python src/driving_school_sqlite.py
```

`sqlite3` is part of the Python standard library and does not need to be installed separately.

## Neo4j: sports federation

The graph example contains cities, competitions, teams, athletes and coaches. Relationships include team membership, coaching periods, competition participation and event locations.

The public entry point reads the connection credentials from environment variables. For example, in PowerShell:

```powershell
$env:NEO4J_URI="bolt://localhost:7687"
$env:NEO4J_USER="neo4j"
$env:NEO4J_PASSWORD="your-password"
$env:NEO4J_DATABASE="neo4j"
python src/sports_federation_neo4j.py
```

`.env.example` lists the expected variable names. The original university implementation is preserved in `src/_sports_federation_coursework.py`; the portfolio entry point overrides its local connection settings before execution.

## Elasticsearch: course reviews

The Elasticsearch example indexes synthetic student reviews and tests several search behaviours, including BM25 relevance, fuzzy matching, phrase queries, Boolean queries, highlighting, numeric/date filters and aggregations.

A local Elasticsearch service is required before running:

```bash
python src/course_reviews_elasticsearch.py
```

## Installation

```bash
pip install -r requirements.txt
```

Neo4j and Elasticsearch must also be running locally for their respective scripts.

## Repository structure

```text
Big-Data-Project/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
└── src/
    ├── driving_school_sqlite.py
    ├── sports_federation_neo4j.py
    ├── _sports_federation_coursework.py
    └── course_reviews_elasticsearch.py
```

The code and comments from the original coursework are mostly in Italian; this README is in English so the project is easier to scan in an international portfolio.
