function generatePlan() {
    console.log("✅ Generate button clicked");

    const data = {
        age: document.getElementById("age").value,
        gender: document.getElementById("gender").value,
        height: document.getElementById("height").value,
        weight: document.getElementById("weight").value,
        goal: document.getElementById("goal").value,
        diet: document.getElementById("diet").value
    };

    console.log("📤 Sending data to backend:", data);

    fetch("/generate-plan", {   // ✅ MUST MATCH Flask
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
    console.log("📥 FULL BACKEND RESPONSE:", result);

    if (!result.plan) {
        alert("No plan received from server. Check backend logs.");
        return;
    }

    console.log("📥 PLAN OBJECT:", result.plan);

    if (!result.plan.workouts || !result.plan.meals) {
        alert("Plan is missing workouts or meals. Check logic.py return.");
        return;
    }

    let output = "";
    output += "Age: " + data.age + "\n";
    output += "Gender: " + data.gender + "\n";
    output += "Goal: " + data.goal + "\n";
    output += "Diet: " + data.diet + "\n\n";

    output += "WORKOUT PLAN:\n";
    output += "Calories Burned: " + result.plan.workout_calories + "\n";
    output += "Workouts: " + result.plan.workouts.join(", ") + "\n\n";

    output += "MEAL PLAN:\n";
    output += "Calories: " + result.plan.meal_calories + "\n";
    output += "Meals: " + result.plan.meals.join(", ");

    document.getElementById("result").innerText = output;
    document.getElementById("resultBox").style.display = "block";
})}
