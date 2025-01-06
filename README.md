# Malphonetic
Find words that would make a poor example for the phonetic alphabet, by finding words whose initial sound is a homophone (or close to one) of another letter.

## Installation
There are no dependencies required, this will run with a modern Python 3 alone. It requires an export of the Wiktionary data file `enwiktionary-????????-pages-meta-current.xml.bz2` from https://dumps.wikimedia.org/backup-index-bydb.html

## Usage
Run with a single argument, pointing to the wiktionary data file, e.g.:

    python3 main.py ./enwiktionary-20241220-pages-meta-current.xml.bz2

It can also be run with an input path of `-`, which can be used in combination with `pv` to get an ETA.

    pv < ./enwiktionary-20241220-pages-meta-current.xml.bz2 | python3 main.py -

## Output
The output is a section for each letter, then up to 5 suggestions for words. Each line is in the format:

* Letter
* IPA for letter name
* Suggested word
* IPA for suggested word
* Score (out of 100)

To save you running this, the output is:

### a
a ˈeɪ ayes aɪz 99
a ˈeɪ ayn aɪn 99
a ˈeɪ ayle aɪ̯l 98
a ˈeɪ aisles aɪlz 98
a ˈeɪ aisle aɪ̯l 98

### b
b b bdelloid ˈdɛlɔɪd 17
b b bdellium ˈdɛli.əm 8

### c
c siː cane keɪn 99
c siː cube kjuːb 99
c siː case keɪs 99
c siː came keɪm 99
c siː cake keɪk 99

### d
d diː djinn d͡ʒɪn 80
d diː djent d͡ʒɛnt 79
d diː djamba ˈd͡ʒɑmbə 72
d diː djembe ˈd͡ʒɛmbeɪ 71
d diː durance ˈd͡ʒʊəɹəns 70

### e
e ˈiː elk ɛlk 99
e ˈiː end ɛnd 99
e ˈiː else ɛls 99
e ˈiː elf ɛlf 99
e ˈiː est ɛst 99

### f

### g
g d͡ʒiː giraffe dʒɪˈɹɑːf 76
g d͡ʒiː gemista ˈjɛmɪstə 76
g d͡ʒiː generic dʒɪˈnɛɹɪk 75
g d͡ʒiː gyrate dʒaɪˈɹeɪt 75
g d͡ʒiː gelada dʒəˈlɑːdə 75

### h
h eɪt͡ʃ hoatzin ˈwætsɪn 77
h eɪt͡ʃ huipil ˈwi.pil 67

### i
i aɪ iwi ˈiːwi 98
i aɪ ikat ˈiːkæt 97
i aɪ ipu ˈiːpuː 97
i aɪ imam ˈiːmɑːm 96
i aɪ iwan ˈiːwɑːn 96

### j
j dʒeɪ jean d͡ʒiːn 99
j dʒeɪ jeep d͡ʒiːp 99
j dʒeɪ jheel d͡ʒiːl 99
j dʒeɪ jeans d͡ʒiːnz 98
j dʒeɪ jeeps d͡ʒiːps 98

### k
k keɪ kues ˈkjuːz 93
k keɪ kudos ˈkjuːdɒs 91
k keɪ kiasuism ˈkjɑːsuːɪzm 68
k keɪ kiasuness ˈkjɑːsuːnəs 68
k keɪ kiasiness ˈkjɑːsiːnəs 68

### l

### m

### n

### o
o ˈəʊ oecist ˈiːsɪst 96
o ˈəʊ oestrus ˈiːstɹəs 95
o ˈəʊ oestrin ˈiːstɹɪn 95
o ˈəʊ oestrone ˈiː.stɹəʊn 83
o ˈəʊ oestriol ˈiː.stɹi.ɒl 82

### p
p piː psephism ˈsiːfɪzəm 89

### q
q kjuː queso ˈkeɪsoʊ 91
q kjuː quebrada keˈbɹɑːdə 84

### r

### s
s ɛs seek siːk 99
s ɛs seep siːp 99
s ɛs seem siːm 99
s ɛs seam siːm 99
s ɛs seize siːz 99

### t

### u
u ˈjuː uitlander ˈaɪtˌlæn dəɹ 85

### v

### w
w ˈdʌbəl.juː wyes ˈwaɪz 99
w ˈdʌbəl.juː wies ˈwaɪz 99
w ˈdʌbəl.juː winy ˈwaɪni 98
w ˈdʌbəl.juː wider ˈwaɪdɚ 98
w ˈdʌbəl.juː wiser ˈwaɪzɚ 98

### x
x ɛks xem zɛm 90
x ɛks xenelasy zɛˈniːləsi 83
x ɛks xenofiction zɛnəfɪkʃən 83
x ɛks xenic ˈzɛnɪk 82
x ɛks xenogenous zɛˈnɒd͡ʒənəs 81

### y
y ˈwaɪ yem ˈiːəm 98
y ˈwaɪ yewen ˈjuːən 98
y ˈwaɪ yuzu ˈjuːzuː 97
y ˈwaɪ ylem ˈiːlɛm 97
y ˈwaɪ youthly ˈjuːθli 97

### z
z zɛd zhou d͡ʒoʊ 80
z zɛd zhiqing d͡ʒɪˈt͡ʃɪŋ 75
z zɛd zhuangyuan d͡ʒwɑːŋ.juˈæn 62
