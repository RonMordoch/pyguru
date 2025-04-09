from dataclasses import dataclass


@dataclass
class Comment:
    comment: str | None = None
    commentable_id: int | None = None
    commentable_type: str | None = None  # TODO check possible enum values
