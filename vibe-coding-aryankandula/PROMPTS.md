# My Vibe Coding Prompts

## Prompt 1: Initial Build
**What I asked:**
Build me a complete working Number Guessing Game (1-100) in a single HTML file. Include CSS and JavaScript so I can open it locally and play. The game should tell the user "higher" or "lower", count attempts, and have a reset button.

**What the AI did:**
Generated a complete HTML file with inline CSS and JS.

**What worked:**
The file opened and let me guess numbers, and provided higher/lower hints.

**What didn’t work:**
(If any) example: input was not validated / lacked a reset button.

**What I learned:**
AI can produce a working prototype quickly but I must test inputs and edge cases.

---

## Prompt 2: Fix input validation
**What I asked:**
The game accepts non-integer and out-of-range input. Fix the input validation so it only accepts whole numbers 1-100 and shows a helpful error otherwise.

**What the AI did:**
Added validation that checks `Number.isInteger()` and range checks with an error message.

**What worked:**
Now it rejects decimals and out-of-range numbers.

**What didn’t work:**
(If any) example: message wording could be clearer.

**What I learned:**
Ask for precise checks and clear messages.

---

## Prompt 3: Add attempt counter and best score
**What I asked:**
Add an attempts counter and show the best score (fewest attempts) during this session.

**What the AI did:**
Added an attempts display and updated best score when player wins.

**What worked:**
Attempts and best score display correctly.

**What didn’t work:**
(If any) example: best not persisted between page loads (acceptable).

**What I learned:**
Small features are easy to add but persistence needs storage (localStorage).

---

## Prompt 4: Improve accessibility and keyboard use
**What I asked:**
Make sure Enter key submits guesses and messages are accessible (aria-live).

**What the AI did:**
Added Enter handling and `aria-live` on the message container.

**What worked:**
Keyboard users can submit quickly.

**What didn’t work:**
(If any) example: small styling issues.

**What I learned:**
Accessibility details are quick wins.

---

## Prompt 5: Make it presentable / final polish
**What I asked:**
Polish colors, spacing, and add friendly text 'Game started—make a guess' and instructions. Return a final single-file HTML for submission named numberguess-final.html.

**What the AI did:**
Provided a polished single-file HTML.

**What worked:**
Ready-to-submit file that plays and is usable for other people.

**What didn’t work:**
(If any) example: not storing best score between reloads — optional.