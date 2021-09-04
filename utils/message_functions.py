def msgreply(author, content):
  content = str(content)
  # author.id = str(author.id)
  return f"<@{author.id}>, {content}"