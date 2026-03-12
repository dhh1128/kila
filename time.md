# Time

**Scope**: Temporal expressions, time units, calendrical systems, temporal vocabulary, date/time formatting

**Related files**: glossary.md (temporal terms), morphology.md (tense/aspect affixes), syntax.md (prepositions)

---

## Time Units

(It is extremely rare to pluralize time units in kila; nearly always, context makes time units obviously plural)

unit | word
--- | ---
time | *temp*
season | *tempra*
epoch | *epak*
instant, moment | *sypl*
second | *mqgza*
minute | *zaln*
hour | *naij*
day | *ju*
week | *sxtm*
month | *omxk*
quarter | *somxk*
year | *kyj*
decade | *zokyj*
century | *zozokyj*
millennium | *posikyj*
million years | *poceikyj*
age | *eij*
era | *era*
eon | *eon*
now | *nau*
then | *den*

## Days of Week

Days are numbered 1-7, combining the number with *ju* (day):

day | word
--- | ---
Sunday | *1ju*
Monday | *2ju*
Tuesday | *3ju*
Wednesday | *4ju*
Thursday | *5ju*
Friday | *6ju*
Saturday | *7ju*

## Misc

english | kila
--- | ---
today | *kiju*
yesterday | *preju*
day before yesterday | *prepreju*
tomorrow | *postju*
day after tomorrow | *postpostju*
anniversary | *kyju*
morning | *morn*
evening | *fynrn*

## Months

Months are numbered 1-12, combining the number with *mxk* (from *omxk* 'month'):

month | word
--- | ---
January | *1mxk*
February | *2mxk*
March | *3mxk*
April | *4mxk*
May | *5mxk*
June | *6mxk*
July | *7mxk*
August | *8mxk*
September | *9mxk*
October | *10mxk*
November | *11mxk*
December | *12mxk*

## Temporal Prepositions

Kila uses different prepositions depending on whether time is conceptualized as a point or a range:

### `dr` - During/within a time period

Use *dr* when the time coordinate falls **within a range or container**:

- *dr 2ju* — "on Monday" (within the Monday period)
- *dr 1mxk* — "in January" (within the January period)
  
This same construction is used to express durations: 
- *dr kyj* — "for a year"
- *dr 4 sxtm* — "for 4 weeks"

### `a` - At a specific time point

Use *a* when pointing to a **specific, indivisible moment**:

- *a 15n* — "at 3 o'clock" (15:00, 3 PM)
- *a 15:15* (spoken as *a unfai unfai*) — "at 3:15pm"
- *a 20 pre 9* - "at twenty minutes to 9 (8:40)"
- *a iat sypl* — "at that moment"

### Other temporal prepositions

- *pre* — "before" (in time or space): *pre Michaelmas* "before Michaelmas"
- *post* — "after" (in time or space): *post ju* "after the day"

## Date and Time Ordering

Kila uses **most-to-least-significant ordering** for all temporal expressions:

### Date format

**Default**: ISO 8601 format (year-month-day)
- *2026-03-11* — March 11, 2026

**Note**: Kila uses **cardinal numbers** for dates, not ordinals. While English says "May eleventh," Kila says *5mxk 11* (literally "May 11").

Month names and day-of-week names may be added while preserving most-to-least-significant order:
- *2026 3mxk 11* — with month name
- *2026 3mxk 11 2ju* — with month name and day-of-week (Monday)

### Time of day

Kila uses a **24-hour clock** (no am/pm distinction).

**Full format**: hour:minute:second (most-to-least significant)
- *15:30:00* — 3:30:00 PM
- *15:15* — 3:15 PM

**"O'clock" construction**: Append *naij* (hour) suffix to the hour number
- *15naij* — "15 o'clock" (3 PM)
- Abbreviated: *15n* — hour suffix abbreviated to just *n*
- *3n* — 3 AM
- *23n* — 11 PM

### Century and millennium notation

**Notation convention** (written shorthand, expanded when read aloud):

Use the abbreviated *k* (from *kyj* 'year') plus a power-of-ten suffix:

notation | meaning | read as
--- | --- | ---
*k2* | century (10² years) | *18k2* "the 1800s" → *18 zozokyj*
*k3* | millennium (10³ years) | *2k3* "the 2000s" → *2 posikyj*
*k6* | million years | *65k6* "65 million years" → *65 poceikyj*

**"Ago" notation**: Place a **negative sign** before the number:
- *-65k6* → read as *65 pocei prekyj* "65 million years ago"

Note: This is a **notation convention** (like "65mya" in English), not linguistic constructions. When speaking, expand to full forms using the pre+unit pattern documented in "Relative Time References" below.

## Frequency and Repetition

### Frequency multipliers

Form frequency multipliers by appending *-ves* to number words:

- *2ves* — "twice" (from *to* "two")
- *3ves* — "three times", "thrice" (from *si* "three")
- *5ves* — "five times" (from *fai* "five")

### Rate expressions

Use the preposition *pr* to express repetition or rate:

- *5ves pr sxtm* — "five times a week"
- *2ves pr ju* — "twice a day"
- *3ves pr kyj* — "three times a year"

Pattern: **[number]-ves pr [time unit]**

## Relative Time References

### Next and last

- *sig* — "next" (following): *sig sxtm* "next week", *sig 2ju* "next Monday"
- *prev* — "last, previous": *prev omxk* "last month", *prev kyj* "last year"

### Future from now ("in X time")

Use *post* + time unit suffix:

- *3 postju* — "in 3 days", "3 days from now"
- *6 postsxtm* — "in 6 weeks"
- *5 postkyj* — "in 5 years"
- *2 postnaij 18* or *2 postnaij 18 zaln* — "in 2 hours 18 minutes", "2 hours 18 minutes from now"
- *2 postnaij pre 18* or *2 postnaij pre 18 zaln* — "in 2 hours minus 18 minutes", "18 minutes shy of 2 hours from now"

Pattern: **[number] post[unit-suffix]**

To subtract smaller units from the time expression, use *pre* to move back toward the present: *2 postnaij pre 18* means "go 2 hours into the future, then come back 18 minutes."

### Past from now ("X time ago")

Use *pre* + time unit suffix:

- *3 preju* — "3 days ago"
- *6 presxtm* — "6 weeks ago"
- *5 prekyj* — "5 years ago"
- *2 prenaij 18* or *2 prenaij 18 zaln* — "2 hours 18 minutes ago"
- *2 prenaij post 18* or *2 prenaij post 18 zaln* — "2 hours minus 18 minutes ago", "18 minutes less than 2 hours ago"

Pattern: **[number] pre[unit-suffix]**

To subtract smaller units from the time expression, use *post* to move forward toward the present: *2 prenaij post 18* means "go 2 hours into the past, then come forward 18 minutes."

**Note**: This pattern expresses time **relative to now**. For fixed historical dates, use the negative prefix: *-65k6* "65 million years ago" (see "Ago expressions" above).

## Time Ranges

Kila is precise about whether ranges in time (or in physical space or number space) are inclusive or exclusive. Any range begins with either *a* 'at' or *post* 'after' to clarify whether the starting point is included or excluded from the range, respectively. The preposition between the first and second unit then tells whether the end of the range is excluded (*aun* 'until') or included (*aunko* 'until including / through').

*a 3n aun 5n* - 'from 3 am to 5 am'
*i wrk a 2ju aunko 5ju* - 'I work Monday through Thursday'
*post 2ju aun 6ju* - 'after Monday until Friday' (Tuesday through Thursday)
