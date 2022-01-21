import sqlite3
from pywebio.output import put_text, toast
from pywebio.input import textarea, select, input, input_group, radio, input_update

tags = {
    "Quantitative Aptitude": [
        "Number System", "LCM and HCF", "Simplification", "Power Indices Surds", "Average", "Ratio and Proportion",
        "Alligation and Mixture", "Percentage", "Profit and Loss", "Discount", "Simple Intereset", "Compound Intereset",
        "Time and Work", "Pipe and Cistern", "Time Speed Distance", "Boats and Streams", "Sequences and Series", "Algebra", "Trignometry",
        "Geometry", "Mensuration", "Statistics and Data-Interpretation", "Miscellaneous"
        ],

    "General Awareness": [
        "Ancient History", "Medieval History", "Modern Indian History", "Indian Geography", "World Geography", "Indian Polity", "Physics",
        "Chemistry", "Biology", "Computer", "Economics", "Discoveries and Inventions", "Sports", "National Events", "International Events",
        "Miscellaneous"
        ],

    "English": [
        "Common Errors", "Improvement of Sentances", "Transformation of Sentances (Active / Passive)", "Direct / Indirect Speech",
        "Fill in the blanks", "Synonyms", "Antonyms", "One word substitution / Group of words", "Idioms / Phrases",
        "Selection of mis-spelt word / correctly spelt word", "Arrangement of sentences", "Cloze Test", "Comprehension Test", "Miscellaneous"
        ],

    "General Intelligence and Reasoning": [
        "Analogy or Similarity", "Blood Relationship", "Symbol and Notations", "Classification", "Direction and Distance",
        "Day Date Time", "Series", "Coding-Decoding", "Word Formation", "Syllogism, Staement and Conclusions",
        "Ranking and Arrangement", "Missing Number", "Arithmetical Problems", "Arrangements of word in logical order",
        "Cubes and Dice", "Logical Venn-diagram", "Counting Figures", "Mirror and Water image", "Papercutting and Folding",
        "Completion of figural pattern", "Miscellaneous"
        ],

    "Current Affairs": ["2020", "2021", "2022"]
}


def createTable(conn):
    conn.execute('''CREATE TABLE QUESTIONPOOL
            (
            CATEGORY TEXT NOT NULL,
            SUBJECT TEXT,
            QUESTION TEXT NOT NULL,
            OPTION_1 TEXT NOT NULL,
            OPTION_2 TEXT NOT NULL,
            OPTION_3 TEXT NOT NULL,
            OPTION_4 TEXT NOT NULL,
            ANSWER TEXT NOT NULL,
            SOLUTION TEXT,
            RELATED_FACTS TEXT,
            REMARKS TEXT);''')
    print("Table created")

def addToDatabase(values):
    conn = sqlite3.connect("question_pool.db")
    #createTable(conn)
    conn.execute('INSERT INTO QUESTIONPOOL VALUES (?,?,?,?,?,?,?,?,?,?,?);', values)
    conn.commit()
    conn.close()

def startPage():
    choices = ["Add new questions", "Update existing questions", "Delete questions"]
    option = radio("Select an option", options=choices)
    if option == choices[0]:
        addQuestion()
    elif option == choices[1]:
        updateQuestion()
    elif option == choices[2]:
        deleteQuestion()
    else:
        startPage()

def addQuestion():
    categories = list(tags.keys())
    data = input_group("Add Question",
        [
            select('Category', options=tags, name='CATEGORY', onchange=lambda c: input_update('SUBJECT', options=tags[c])),
            select('Subject', options=tags[categories[0]], name='SUBJECT'),
            textarea("Question", rows=3, name="QUESTION"),
            input('Option 1 ', name="OPTION_1"),
            input('Option 2 ', name="OPTION_2"),
            input('Option 3 ', name="OPTION_3"),
            input('Option 4 ', name="OPTION_4"),
            input('Answer ', name="ANSWER"),
            textarea('Solution ', name="SOLUTION"),
            textarea('Related Facts ', rows=2, name="RELATED_FACTS"),
            textarea('Remarks ', rows=2, name="REMARKS"),
        ], cancelable=True)

    if data:
        addToDatabase(list(data.values()))
        toast("Added to database")

    startPage()

def updateQuestion():
    startPage()

def deleteQuestion():
    startPage()

if __name__ == "__main__":
    startPage()
