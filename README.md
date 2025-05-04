# AI-Powered Image Search Tool 

## Workflow 

### - Scrape free image metadata (title, description, tags, URL)
### - Generate embeddings from texts descriptions using sentence transformers
### - Store metadata + embeddings in a FIASS index and database
### - Accept natural language query via FAST API 
### - Convert query to embeddings
### - Return the top-N matching images  with links and metadata
 