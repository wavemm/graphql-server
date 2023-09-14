from __future__ import annotations

from graphql import DocumentNode


class DocumentNodeWithQuery(DocumentNode):
    __slots__ = ("query",)

    query: str

    @staticmethod
    def from_document_node(
        node: DocumentNode,
        query: str,
    ) -> DocumentNodeWithQuery:
        return DocumentNodeWithQuery(
            loc=node.loc,
            definitions=node.definitions,
            query=query,
        )
