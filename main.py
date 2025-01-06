import collections
import bz2
import re
import string
import sys


TITLE_RE = re.compile(r"\>([a-z]+?)\<")
IPA_RE = re.compile(r"IPA\|en\|\/(.+?)\/")


def get_wordset(path: str):
    # Open stdin if the path is '-'
    if path == "-":
        input_file = sys.stdin.buffer
    else:
        input_file = open(path, "rb")

    # BZip decompress the input
    with bz2.open(input_file, mode="rt", encoding="utf-8") as dump:
        current_word = None

        # Scan the input lines
        for line in dump:
            # If the line has an english IPA tag, set that as the pronunciation for the word
            if "{{IPA|en|" in line:
                pron = IPA_RE.findall(line)
                if pron and current_word:
                    yield current_word, pron[0]
                    current_word = None
            # A title tag gives us a new word
            elif "<title>" in line:
                title = TITLE_RE.findall(line)
                if title:
                    current_word = title[0]
                else:
                    current_word = None


def get_letter_targets(words: dict[str, str]):
    for letter in string.ascii_lowercase:
        target = words.get(letter)
        yield letter, target


def score_word_against_target(ipa: str, target: str) -> int:
    score = 0

    # Exact homophones score zero
    if ipa == target or ipa == f"'{target}":
        return 0

    # If it starts with the right sound, score 100. If it's the same modulo stress, score 5.
    # Reduce for prefixes of the right sound
    for i, prefix_length in enumerate(range(len(target), 1, -1)):
        target_prefix = target[:prefix_length]
        if ipa.startswith(target_prefix):
            score += 100 - (10 * i)
            break
        elif ipa.startswith(f"ˈ{target_prefix}"):
            score += 95 - (10 * i)
            break

    # Reduce score if multiple syllables
    if "." in ipa:
        score -= 10

    # Reduce score by how much longer this sound is than the target
    score -= abs(len(ipa) - len(target))

    return score


def score(words: dict[str, str]):
    # Loop over all letters
    for letter in string.ascii_lowercase:
        letter_scores = score_letter(letter, words)

        print()
        print(f"# {letter}")
        # Show the top 5 scores
        for word, score in letter_scores.most_common(5):
            print(letter, words.get(letter), word, words[word], score)


def score_letter(letter: str, words: dict[str, str]) -> collections.Counter[str]:
    letter_scores: collections.Counter[str] = collections.Counter()

    # Now check all words ...
    for word in words:
        # ... that start with the right letter
        if word.startswith(letter):
            # For each _other_ letter, score them, and keep the best score
            for other_letter, target in get_letter_targets(words):
                # Ignore the actual letter
                if other_letter == letter:
                    continue

                # Skip any letters we can't pronounce
                if not target:
                    continue

                # Score this letter, and update the scores if it's better
                score = score_word_against_target(words[word], target)
                # print("-", letter, word, other_letter, target, score)
                if score > letter_scores[word]:
                    letter_scores[word] = score

    return letter_scores


if __name__ == "__main__":
    wordset = get_wordset(sys.argv[1])
    mapping = dict(wordset)

    score(mapping)
