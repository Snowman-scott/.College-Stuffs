import json
import os
import re
import time


def clear_screen():  # Clears the screen
    os.system("cls" if os.name == "nt" else "clear")


def run_quiz_section(file_name, section_title):
    try:
        with open(file_name, "r") as file:
            questions = json.load(file)
    except FileNotFoundError:
        print(f"ERROR: {file_name} not found.")
        return 0, 0

    section_score = 0
    max_score = sum(q["marks"] for q in questions)

    for i, q in enumerate(questions):
        clear_screen()
        print(f"--- {section_title} | Question {i + 1}/{len(questions)} ---")
        print(f"\n{q['question']}\n")

        if q["type"] == "mcq":
            for opt in q["options"]:
                print(opt)
            ans = input("\nChoice (A-D): ").strip().upper()
            if ans == q["answer"]:
                print(f"✅ Correct! +{q['marks']} mark(s)")
                section_score += q["marks"]
            else:
                print(f"X Incorrect. The correct answer was: {q['answer']}")

        elif q["type"] == "verbose":
            user_input = input("Your answer: ").lower()

            # The 'RE' Logic:
            # Join Keywords into a regex pattern: "word1|word2|word3"
            pattern = "|".join(q["keywords"])

            # Find all unique matches
            matches = set(re.findall(pattern, user_input))

            print(f"\n[MODEL ANSWER]: {q['model_answer']}")

            # Award marks proportionally based on keywords hit out of total keywords
            keywords_hit = len(matches)
            total_keywords = len(q["keywords"])
            awarded = round((keywords_hit / total_keywords) * q["marks"])

            if awarded > 0:
                print(f"✅ +{awarded}/{q['marks']} marks. Technical terms used: {', '.join(matches)}")
                section_score += awarded
            else:
                print(
                    f"⚠️ No marks. Keywords found: {keywords_hit}/{total_keywords}."
                )
        time.sleep(1)
        input("\nPress Enter to continue...")
    return section_score, max_score


# --- Main program start ---
clear_screen()
print("=== T-LEVEL DIGITAL ESP: TASK 4 PRACTICE AND REVISION QUIZ ===")
print("Sections: 4a (Development) & 4b (Evaluation)")
time.sleep(1)

# Run Task 4a
score_4a, max_4a = run_quiz_section("Task_4a_questions.json", "TASK 4A: DEVELOPMENT")

# Run Task 4b
score_4b, max_4b = run_quiz_section("Task_4b_questions.json", "TASK 4B: EVALUATION")

# Final results
total_score = score_4a + score_4b
total_max = max_4a + max_4b
print("=== FINAL RESULTS ===")
print(f"Task 4a Score: {score_4a}/{max_4a}")
print(f"Task 4b Score: {score_4b}/{max_4b}")
print(f"OVERALL SCORE: {total_score}/{total_max}")

distinction_threshold = round(total_max * 0.8)
merit_threshold = round(total_max * 0.6)

if total_score >= distinction_threshold:
    print("Grade: Distinction - You are ready for the ESP!")
elif total_score >= merit_threshold:
    print("Grade: Merit - Good, but review the 'Verbose' model answers.")
else:
    print("Grade: Pass/Unclassified - More revision on technical requirements needed.")
