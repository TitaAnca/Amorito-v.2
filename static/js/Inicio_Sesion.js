function startGame() {
    document.getElementById("start-screen").classList.add("hidden");
    document.getElementById("game-screen").classList.remove("hidden");
    loadQuestion();
}

function loadQuestion() {
    const questionContainer = document.getElementById("question");
    const optionsContainer = document.getElementById("options");
    const backButton = document.getElementById("back-button");
    
    questionContainer.textContent = questions[currentQuestionIndex].question;
    optionsContainer.innerHTML = "";
    
    questions[currentQuestionIndex].answers.forEach(answer => {
        const optionElement = document.createElement("div");
        optionElement.classList.add("option");
        optionElement.onclick = () => selectAnswer(optionElement);
        
        const imgElement = document.createElement("img");
        imgElement.src = answer.img;
        imgElement.alt = answer.text;
        
        const textElement = document.createElement("span");
        textElement.textContent = answer.text;
        
        optionElement.appendChild(imgElement);
        optionElement.appendChild(textElement);
        optionsContainer.appendChild(optionElement);
    });

    backButton.classList.toggle("hidden", currentQuestionIndex === 0);
}

function selectAnswer() {
    setTimeout(() => nextQuestion(), 500);
}

function nextQuestion() {
    if (currentQuestionIndex < questions.length - 1) {
        currentQuestionIndex++;
        loadQuestion();
    } else {
        document.getElementById("question").textContent = "Your answers have been submitted! Thank you for replying!";
        document.getElementById("options").innerHTML = "";
        document.getElementById("back-button").classList.add("hidden");
    }
}

function previousQuestion() {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        loadQuestion();
    }
}