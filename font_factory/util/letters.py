letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,-/?!\"'äöüÄÜÖß:;()1234567890"
smalls = list("abcdefghijklmnopqrstuvwxyz")+["adieresis","odieresis","udieresis"]
letter2folder = {a:a for a in letters}
different_map = {
    '"':"quotedbl",
    "'":"quotesingle",
    ".":"period",
    "/":"slash",
    "?":"question",
    "!":"exclam",
    ",":"comma",
    "-":"hyphen",
    "(":"parenleft",
    ")":"parenright",
    ":":"colon",
    ";":"semicolon",
    "ö":"odieresis",
    "ü":"udieresis",
    "ä":"adieresis",
    "Ö":"Odieresis",
    "Ü":"Udieresis",
    "Ä":"Adieresis",
    "ß":"germandbls",
    " ":"space",
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
}
for key in different_map:
    letter2folder[key] = different_map[key]
escape_chars = "\""