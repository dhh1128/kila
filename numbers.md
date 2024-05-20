# Numbers

Kila is strongly base-10 oriented, and its numbering system is easy to learn because it is so predictable.

English has number words for the digits zero through nine, but it also has number words that are less directly tied to digits, like "ten", and "eleven". Kila, on the other hand, always models number words as sequences of one to three digits.

The digit names in kila are:

digit | word
--- | ---
0 | *zo*
1 | *un*
2 | *to*
3 | *si*
4 | *kq*
5 | *fai*
6 | *cei*
7 | *sxt*
8 | *ok*
9 | *nuv*

The sequence of digits in the number 24 is the digit 2 followed by the digit 4 &mdash; so the number word for 24 in kila is *tokq* (the word for *two* followed by the word for *four*). Similarly, the word for 100 in kila is *unzozo*.

Numbers are virtually always written with actual digits in kila text. However, they can be spelled as words, and whichever form they take, they are pronounced the same way. *100* and *unzozo* sound the same when read aloud.

If a number is more than 3 digits long, its digits are grouped into clusters of 3, beginning at the rightmost (least signficant) digit, with a comma separating each group. Thus, 42765 would be written in kila text as 42,765.

When a large number like this is spoken aloud, it becomes a phrase, with one number word for each digit cluster. The hyphens correspond to vocal pauses between number words.

Each digit cluster in a large number carries a suffix that tells how many zeros (which power of ten) its rightmost digit represents. This suffix is built from the syllable /po/ plus the number word for the associated number of zeros (power of ten). Returning to our sample large number, 42765, the cluster 42 represents 42 thousands, or 42 * 10^3. Therefore, the number word for this digit cluster is *kqto* (the digit cluster part) plus the suffix *-posi*, where "si" tells us that 42 is a cluster for ten-to-the-power-of-3. Thus, the complete sequence of syllables that corresponds to the kila word *42,765* is:

    kqtoposi sxtceifai

From this convention, we derive the word *posi* for 'thousand', *pocei* for 'million', *ponuv* for 'billion', *pounto* for 'trillion', and so forth.

Negative numbers are preceded by the prefix *hi-*. Thus, -4816 would be *hikqposi okuncei*.

Ordinals are constructed by adding the suffix *-xm* to the number. This rule is completely regular. Thus, the translation of English 'first' or '1st' could be written as *1xm* or (less commonly) *unxm* in kila.

Words for groups of a given size are built with numbers plus the suffix *-mqn*. This is analogous to the French pattern of adding *-aine* to a number: *ventaine* is a group of 20, *centaine* is a group of 100, and *douzaine* is a group of 12 &mdash; compare English *dozen*). The kila word *untomqn* means 'dozen'.

A python script, [saynum.py](saynum.py), is available. Given any number, it generates the corresponding kila syllables.

