-- Run once in Supabase: SQL Editor -> New query -> paste -> Run
-- Vector size 1024 = Mistral mistral-embed
-- The first two lines remove the old 3072 (Gemini) version – safe, the table is empty

drop function if exists match_documents(vector, int, jsonb);
drop table if exists documents;

create extension if not exists vector;

create table documents (
  id bigserial primary key,
  content text,
  metadata jsonb,
  embedding vector(1024)
);

create index on documents using hnsw (embedding vector_cosine_ops);

create or replace function match_documents (
  query_embedding vector(1024),
  match_count int default null,
  filter jsonb default '{}'
) returns table (
  id bigint,
  content text,
  metadata jsonb,
  similarity float
)
language plpgsql
as $$
#variable_conflict use_column
begin
  return query
  select
    id,
    content,
    metadata,
    1 - (documents.embedding <=> query_embedding) as similarity
  from documents
  where metadata @> filter
  order by documents.embedding <=> query_embedding
  limit match_count;
end;
$$;
