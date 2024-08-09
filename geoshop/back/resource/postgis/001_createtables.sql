CREATE EXTENSION postgis;
CREATE EXTENSION unaccent;
CREATE EXTENSION "uuid-ossp";
CREATE SCHEMA geoshop AUTHORIZATION geoshop;

-- Only if french is needed
CREATE TEXT SEARCH CONFIGURATION fr (COPY = simple);
ALTER TEXT SEARCH CONFIGURATION fr ALTER MAPPING FOR hword, hword_part, word
WITH unaccent, simple;
