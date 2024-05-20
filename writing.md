# Writing Conventions

## Direction
Kila is written left-to-right in pure ASCII.

## Capitalization
Normal text is spelled using an alphabet called the *gwm*, which consists of the 26 lower-case letters available in ASCII. The 26 upper-case letters are part of a different alphabet called the *fim*. See [Alphabets](alphabets.md).

A word or phrase that serves as an identifier (that is, a proper noun, a personal name, or a title) is preceded with a single hyphen (called a *haif*) to signal its identifier status. This punctuation mark is silent when read aloud. Marking an identifier this way has approximately the same functiona as capitalization in English.

The first word of a sentence is not marked with a *haif*. 

## Contractions
Kila has a few contractions. They do not use an apostrophe.

One-syllable words ending in the vowel *x* are written without the trailing vowel: *nx* &rarr; *n* &mdash; 'and', *dx* &rarr; *d* &mdash; 'of/from'.

Sequences of one-syllable words like this are written just as consonant clusters: *nx dx* &rarr; *nd* &mdash; 'and of/from'

Pronouns followed by *dx* (which signals possession) combine into a single word, also with the final vowel *x* omitted: *vi dx* &rarr; *vid* &mdash; "our". This contraction can be further combined with consonant clusters formed by other contraction rules: *nx i dx* &rarr; *nid* &mdash; 'and my'.

Unlike contractions in other languages, kila contractions are *only written*. When spoken or read aloud, they are expanded. However, rapid speech will blur the sounds together, producing something that approximates the sounds in a naive reading of the contraction.

## Quotes
Quotes are offset with */-* and *-/*, which have spaces next to the slash but generally no spaces next to the hyphen. These symbols are known as the *cwv* &mdash; 'quote' and the *vwc* &mdash; 'unquote', respectively. They are typically read as a pause, so they don't need an associated comma before or after. If the quoting context is a formal citation, the names of the marks are read aloud to indicate where the quote begins and ends. 

*e sedy /-kxmdu kiju!-/.* &mdash; He said, "Come today!"

Nested quotes require an additional hyphen after the cwv and before the vwc: */--* and *--/*. This results in what's called a *tocwv* and *tovwc &mdash; 'two quote' and 'two unquote'. Theoretically, this pattern of adding hyphens for more levels of nesting can continue, though even a *sicwv* is extremely unusual.

*e sedy /-i telvy de /--kxmdu kiju!--/-/.* &mdash; He said, "I will tell her 'Come today!'"

If and only if what's quoted includes natural punctuation (e.g., it's a quoted question or exclamation, as shown above), the punctuation goes inside the quotes. However, quoted punctuation never finishes the sentence of the quoter, which is why the kila examples above end with a period.

## Emphasis
Text is emphasized (italicized) by surrounding it with asterisks: e bi \*sobyg\*.

## Foreign text
Kila uses foreign words freely, and writes them in their native script ([kqm](alphabets.md#kqm)). If words are obviously kqm, no special markup is needed: *i abit yn Switzerland*. For extra clarity, the foreign text is surrounded by underscores: i hav \_déjà vu\_. (The word *déjà* is obviously kqm, but vu is not.) 

## Other punctuation
Dashes are written as 2 hyphens -- or an em dash &mdash;, with spaces before and after. Question marks, exclamation points, commas, semicolons, and colons all bind to the word that precedes them, meaning they have no preceding space. Parens touch what they contain, and are offset from exterior text by a space.

Ellipses are placeholders for elided text, and can be written with 3, 4, or 2 dots. These marks are called the *elyps*, *kalyps*, and *tolyps* in kila. The elyps and kalyps are written *without* a space before, and *with* a space after. They always elide text on whole-word boundaries. Use an elyps when eliding words inside a single sentence. Use a kalyps when the words after the ellipse are not from the same sentence as the words before it:

example | comment
--- | ---
word1... wordN | Word1 and wordN are part of the same sentence
word1.... wordN | Word1 and wordN are not part of the same sentence.

A tolyps may begin and/or end eliding in the middle of a word. It always attaches directly to text on either side. It represents the elision of *items in a sequence*; what precedes and follows are the first and last items, respectively:

example | comment
--- | ---
abc..xyz | sequence of [gw](alphabets.md#gwm) beginning with *abc* and ending with *xyz*. Since gw can be used to spell arbitrary words, implies nothing about the intervening characters.
1..10 | Numeric sequence that includes all the numbers from 1 to 10, inclusive.
10..1 | Descending numeric sequence that includes all the numbers from 10 to 1, inclusive.
A..H | sequence of [fi](alphabets.md#fim) beginning with *A* and ending with *H*. Since fi are used symbolically rather than to spell, implies all the fi in order between A (first fi) and H (last fi). 

## Acronyms and abbreviations
Kila values conciseness, and supports several conventions for abbreviation. None of them use the truncation + period approach known to English writers.

One convention is to use a tolyps. For example, a kila translation of the Jules Verne novel, *Around the World in Eighty Days* might be titled *-ri z mund yn 80 ju*, and abbreviated as *-ri..ju*. This approach is common when what's abbreviated is a phrase of general language.

Another convention is to use [fi](alphabets.md#fim) to build an acronym, by converting each word-initial [gw](alphabets.md#gw) (or, sometimes, each word-initial letter in kqm text) to its fi jum (roughly, by converting lower-case to capital letters). Acronyms typically drop small words, and they may be further truncated if their meaning is obvious. The English phrase *scanning electron microscope* could appear in kila text, and then be abbreviated with the acronym *SEM*.

Fi or digits can also be used to abbreviate in a more flexible, arbitrary way. For example, in legal contracts or highly technical material, the first occurrence of the referent can be offset with hyphens and suffixed with the fi: *-afysr armnim -A* &mdash; 'army officer A' or *-parti-1* &mdash; 'party 1'. Thereafter, the fi or digit by itself (e.g., *A* or *1*), or a relevant word with a hyphen+fi suffix (e.g., *e-A* &mdash; 'he (officer A)' or 'e-1' &mdash; 'she (party 1)') can be used wherever the referent would otherwise appear. This pattern can be used to establish arbitrary abbreviations or short forms, or to disambiguate pronouns.

Kila also abbreviates long individual words by giving the first and last gw, and replacing the middle with a count of the number of elided letters. This is the same convention that converts *internationalizaton* into *i18n* or *kubernetes* into *k8s* in English.
