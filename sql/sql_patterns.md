## 🔎 SQL Pattern Matching Cheat Sheet

| Pattern | Example Query | Matches | Doesn’t Match |
|---------|---------------|---------|----------------|
| **Exact match** | `WHERE name = 'John';` | `John` | `Johnny`, `john` |
| **% (any characters)** | `WHERE name LIKE 'Jo%';` | `John`, `Jordan`, `Joseph` | `Mark` |
| **%…% (contains)** | `WHERE name LIKE '%an%';` | `Daniel`, `Joanna`, `Jonathan` | `John`, `Mary` |
| **Ends with** | `WHERE name LIKE '%son';` | `Jackson`, `Emerson` | `John`, `Smith` |
| **_ (single char)** | `WHERE name LIKE 'J_n';` | `Jan`, `Jen`, `Jon` | `John`, `Joan` |
| **Multiple _** | `WHERE name LIKE 'J___';` | `John`, `Jack` | `Jo`, `Johnny` |
| **Set [ ] (SQL Server / Oracle)** | `WHERE name LIKE '[AB]%';` | `Alice`, `Bob` | `Charlie` |
| **Range [ - ]** | `WHERE name LIKE '[A-D]%';` | `Alice`, `David` | `Eric`, `Mike` |
| **NOT LIKE** | `WHERE name NOT LIKE '%son';` | `John`, `Mary` | `Jackson`, `Emerson` |
| **Case-insensitive (Postgres)** | `WHERE name ILIKE '%c%';` | `carl`, `Carl`, `miChael` | – |
| **Regex (MySQL)** | `WHERE name REGEXP '^J.*n$';` | `John`, `Jason` | `Jordan`, `Jack` |


⚡ Notes:

% = zero or more characters.

_ = exactly one character.

[ ] = character set/range (not in MySQL, but works in SQL Server/Oracle).

ILIKE = case-insensitive LIKE (Postgres only).

REGEXP / RLIKE = advanced regex search (MySQL/Postgres).



