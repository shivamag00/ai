from logic import *
import copy

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

knowledges = And(
    Or(AKnight, AKnave),                
    Not(And(AKnight, AKnave)),  
    Or(BKnight, BKnave),               
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),                
    Not(And(CKnight, CKnave)),                
)
# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = copy.deepcopy(knowledges)
knowledge0.add(
    Implication(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = copy.deepcopy(knowledges)
knowledge1.add(
    Biconditional(AKnight,And(AKnave,BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = copy.deepcopy(knowledges)
knowledge2.add(
    Biconditional(AKnight,Or(And(AKnave,BKnave),And(AKnight,BKnight)))
)
knowledge2.add(
    Biconditional(BKnight,Not(Or(And(AKnave,BKnave),And(AKnight,BKnight))))
)
# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = copy.deepcopy(knowledges)
knowledge3.add(
    Implication(Or(AKnave,AKnight),AKnight)
)
knowledge3.add(
    Biconditional(AKnave,BKnight)
)
knowledge3.add(
    Biconditional(CKnave,BKnight)
)
knowledge3.add(
    Biconditional(AKnight,CKnight)
)



def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
