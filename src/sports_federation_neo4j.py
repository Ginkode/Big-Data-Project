"""Portfolio entry point for the Neo4j sports-federation project.

Connection settings are read from environment variables so credentials are not
required in the command used to run the public portfolio version.
"""

import os

import _sports_federation_coursework as coursework


def configure_connection():
    password = os.getenv("NEO4J_PASSWORD")
    if not password:
        raise RuntimeError(
            "NEO4J_PASSWORD is not set. Configure the Neo4j environment "
            "variables before running this script."
        )

    coursework.URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    coursework.AUTH = (os.getenv("NEO4J_USER", "neo4j"), password)
    coursework.DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")


def main():
    configure_connection()
    coursework.main()


if __name__ == "__main__":
    main()
