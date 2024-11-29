def filter_comments_by_author(comments: list, author: object) -> list:
    return list(filter(lambda comment: comment.author_id == author.id, comments))
