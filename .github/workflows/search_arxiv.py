import arxiv
 
search = arxiv.Search(
  query = "SLAM",
  max_results = 10,
  sort_by = arxiv.SortCriterion.SubmittedDate
)
for result in search.results():
  print(result.entry_id, '->', result.title)
