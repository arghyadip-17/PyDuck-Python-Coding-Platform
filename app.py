from flask import Flask, render_template, request
from problems import problems
import subprocess
import sys
import tempfile

app = Flask(__name__)

# ---------- UTILITY FUNCTIONS ----------

def normalize(output: str) -> str:
    """Remove extra spaces and normalize newlines"""
    return output.strip().replace("\r\n", "\n")

def run_user_code(code: str, input_data: str):
    """Run user code safely and return output / error"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(code)
        filename = f.name

    try:
        result = subprocess.run(
            [sys.executable, filename],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=2
        )
        return result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return "", "Time Limit Exceeded"

# ---------- ROUTES ----------

@app.route("/")
def index():
    return render_template("index.html", problems=problems)


@app.route("/problem/<pid>", methods=["GET", "POST"])
def problem(pid):
    prob = problems[pid]
    result = None
    user_code = ""   # ⭐ ADD THIS

    if request.method == "POST":
        user_code = request.form["code"]   # ⭐ STORE CODE
        passed = True
        feedback = []

        for test_input, expected_output in prob["tests"]:
            user_output, error = run_user_code(user_code, test_input)

            if error:
                passed = False
                feedback.append(
                    f"❌ Runtime Error\nInput: {test_input}\n{error}"
                )
                break

            if normalize(user_output) != normalize(expected_output):
                passed = False
                feedback.append(
                    f"""❌ Wrong Answer
Input:
{test_input}

Expected:
{expected_output}

Your Output:
{user_output}"""
                )
                break

        if passed:
            result = "✅ Accepted! All test cases passed."
        else:
            result = "\n".join(feedback)

    return render_template(
        "problem.html",
        problem=prob,
        problems=problems,
        result=result,
        user_code=user_code   # ⭐ PASS BACK
    )



if __name__ == "__main__":
    app.run(debug=True)
