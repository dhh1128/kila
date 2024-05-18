# Alphabet and Phonology

Kila's normal alphabet (the one it uses to spell words) is called the "gwm", and a letter in this alphabet is called a "gw".

The gwm has very simple, consistent correspondences between gw and sounds. The table below enumerates the gwm (9 vowels, 17 consonants), in lexical order. This order proceeds from vowels to consonants; for vowels, from low to high and front to back; for consonants, from voiced to unvoiced and from front to back. The benefit of this sort order is that words that sort together alphabetically also have similar sounds.

The names of the gw are the vowel sounds themselves, for the vowels. For vocalic consonants, they are e+consonant. For voiced consonants, they are consonant+i. For unvoiced consonants, they are consonant+a.

gw | order | name | IPA | notes
--- | --- | --- | --- | ---
a | 1 | a | a | vowel sound in English "on" or Spanish "pan"
x | 2 | x | ʌ | vowel sound in English "cut"
w | 3 | w | ʊ | vowel sound in English "put"
q | 4 | q | æ | vowel sound in English "cat"
e | 5 | e | ɛ | vowel sound in Spanish "es", similar to vowel in English "met" -- not the diphthong in English "raid"
y | 6 | y | I | vowel sound in English "kit"
i | 7 | i | i | vowel sound in English "need" or Spanish "mi"
o | 8 | o | o | vowel sound in Spanish "color" -- doesn't decay to /u/ like the vowel in English "go"
u | 9 | u | u | vowel sound in English "new" or Spanish "su"
m | 10 | em | m | can be vocalic
n | 11 | en | n | can be vocalic
l | 12 | el | l | can be vocalic
r | 13 | er | ɹ | initial consonant in English "red"; can be vocalic
b | 14 | bi | b | bilabial plosive as in English, not approximant as in Spanish
v | 15 | vi | v | labiodental fricative as in English, not approximant as in Spanish
d | 16 | di | d | alveolar as in English, not dental as in Spanish 
z | 17 | zi | z | 
j | 18 | ji | ʒ | sound written with "z" in English "azure"
g | 19 | gi | ɡ | always a "hard g" as in "gig"
p | 20 | pa | p | bilabial plosive as in English, not approximant as in Spanish
f | 21 | fa | f | labiodental fricative as in English, not approximant as in Spanish
t | 22 | ta | t | alveolar as in English, not dental as in Spanish
s | 23 | sa | s | 
c | 24 | ca | ʃ | sound written with "sh" in English "ship"
k | 25 | ka | k |
h | 26 | ha | h | initial consonant in English "house"

The following sounds can form minimal pairs with a single, similar consonant or vowel, but they are written as digraphs rather than single letters in kila. Unlike digraphs in English, the combined sound is an exact derivation of the two sounds in kila, so kila does not think of them as special sequences. However, they are noted here for those that may see them as special and wonder how the sounds are made and written:

digraph | IPA (sound) | note
--- | --- | ---
tc | tʃ | sound written with "ch" in English "chair"
dj | dʒ | sound written with "j" in English "joy"
oi | oi | diphthong written with "oy" in English "boy"
ai | ai | diphthong written with "i" in English "time"
ei | ei | diphthong written with "ay" in English "play"
au | au | dipthong written with "ow" in English "town"

Vowel digraphs beginning with "i" approximate the sound of the English letter "y" followed by the next vowel, or the IPA glide /j/. Vowel digraphs beginning with "u" approximate the English letter "w" followed by the next vowel. Kila does not view these glides as letters and corresponding consonants. Thus, a kila speaker would transliterate the English word "yes" as "ies", and "will" as "uyl".

## fim (symbolic alphabet)
Kila uses the capital letters A-Z in both written and spoken language. However, it considers them part of a different alphabet called the "fim". A symbol in this set is called a "fi". Fis are used not to *spell* words, but to *replace*, *suggest*, *reference* or *abbreviate* words.

Each symbol in the fim has a corresponding letter in the gwm (A &rarr; a, B &rarr; b, and so forth). The corresponding item in the opposite alphabet is called the "jum" (twin). The fim gets its name from the fact that the names of its symbols are formed by adding /f/ to the vowel sound in the name of the jum gw from the gwm:

fim | order | jum gw name | name
--- | --- | --- | ---
A | 1 | a | fa
... | ... | ... | ...
M | 10 | em | fem
... | ... | ... | ...
B | 14 | bi | bif
... | ... | ... | ...
H | 26 | ha | haf

A fi often (but not always) gets its meaning from jum correspondence. For example, if two friends are talking or writing about a third person named "meriqn" ("Mary Anne") that they both know well and recognize from context, they may simply refer to this person verbally as "fem", or in written form as "M" (read aloud as "fem" again). Both will understand that the person they're referring to is someone whose name begins with the jum of "M", which is "m", and connect that mentally with "meriqn".

Acronyms in kila use this same pattern, which is somewhat similar to how acronyms work in English. A kila translation of the Jules Verne novel *Around the World in 80 Days* might have the title /ri z mund yn 80 ju/ and might be abbreviated after the first appearance of the full form of the title, without any explanation, as RM80. (Acronyms typically drop small words -- and they may be further truncated if their meaning is obvious.)

If context doesn't provide enough clarity about a fi's referent (e.g., in legal contracts or highly technical material), the first occurrence of the referent can be offset with hyphens and suffixed with the fi: -referent-fi (e.g., -afysr armnim -A). This explicitly defines a relationship. Thereafter, the fi by itself (e.g., A), or a relevant word with a hyphen+fi suffix (e.g., e-A) can be used wherever the referent would otherwise appear. This pattern can be used to establish arbitrary abbreviations or short forms, or to disambiguate pronouns:

en | kila
--- | ---
A teacher should read more books than a student, but s/he has less time. | titcr-T cwd ridn plu liv k studr-S, sep e-T hqv myn temp.
He (person 1) gave him (person 2) a book. | e-A givdy livr d e-H.

(Disambiguating pronouns can also be done by prefixing the pronouns with a gender marker, hi- or ci-, or by using a number as a suffix: e-1 givdy livr d e-2.)  

## Sort order
Kila sorts whitespace characters first (and within whitespace, in byte order), then digits, then fim, then gwm in the order shown, then every other byte of text in byte order.

